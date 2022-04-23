import json
import os
import random
import string
import urllib

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import Q
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, View
from imoveis.models import Imovel
from mensagem.models import Chat

from .forms.login_form import LoginForm
from .forms.register_form import (LoginEditForm, RegisterEditForm,
                                  RegisterForm, ResetPasswordForm)
from .models import PasswordReset, User


def re_captcha(POST):

    captcha_private_key = os.environ.get("RECAPTCHA_PRIVATE_KEY")

    # Captcha Verification start
    recaptcha_response = POST.get('g-recaptcha-response')
    url = 'https://www.google.com/recaptcha/api/siteverify'
    values = {
        'secret': captcha_private_key,
        'response': recaptcha_response
    }
    data = urllib.parse.urlencode(values).encode()
    req = urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode())
    # End Capatcha verification
    if result['success']:
        return True
    else:
        return False


class UsersLogin(TemplateView):
    template_name = 'users/pages/login.html'

    def get(self, *args, **kwargs):

        form = LoginForm()
        captcha_public_key = os.environ.get("RECAPTCHA_PUBLIC_KEY")
        context = self.get_context_data(**kwargs)
        return self.render_to_response({
            **context,
            'form': form,
            'captcha_public_key': captcha_public_key,
        })

    def post(self,  *args, **kwargs):
        if not self.request.POST:
            raise Http404
        form = LoginForm(self.request.POST)
        POST = self.request.POST
        next_page = self.request.POST.get('next')

        if form.is_valid():

            if re_captcha(POST):
                authenticade_user = authenticate(
                    username=form.cleaned_data.get('username', ''),
                    password=form.cleaned_data.get('password', ''),
                )

                if authenticade_user is not None:
                    login(self.request, authenticade_user)
                    if next_page:
                        return redirect(next_page)
                    return redirect(reverse('users:users_login'))

                else:
                    messages.error(self.request, 'Erro de usuário ou senha')
                    return redirect(reverse('users:users_login'))
            else:
                messages.error(self.request, 'Erro na verificação do captcha')
                return redirect(reverse('users:users_login'))
        else:
            messages.error(self.request, 'Erro de usuário ou senha')
            return redirect(reverse('users:users_login'))


class PassRecovery(View):

    def get(self, *args, **kwargs):
        template = 'users/pages/recupera_senha.html'
        captcha_public_key = os.environ.get("RECAPTCHA_PUBLIC_KEY")

        return render(
            self.request,
            template,
            context={
                'captcha_public_key': captcha_public_key,
            }
        )

    def post(self, *args, **kwargs):
        if not self.request.POST:
            raise Http404

        def random_generator(size=100, chars=string.ascii_lowercase + string.digits):  # noqa
            return ''.join(random.choice(chars) for _ in range(size))

        POST = self.request.POST
        email = POST.get('email')

        user = User.objects.filter(
            email=email,
        ).first()

        if user:
            if re_captcha(POST):
                link = random_generator()
                reset_info = PasswordReset.objects.create(
                    email=email,
                    user_id=user.id,
                    ip=self.request.META.get('REMOTE_ADDR'),
                    link=link,
                )
                reset_info.save()
                # flake8: noqa
                mensagem = f'''
                Olá {user.first_name} !

                Você está recebendo este email pois foi solicitada uma recuperação de senha.
                Para redefinir sua senha basta clicar no link e seguir as instruções.        


                Esse link é válido por 3 dias

                Link para redefinição de senha:

                { self.request.META['HTTP_HOST'] }/users/passreset/{email}/{link}
                
                '''

                send_mail(
                    subject='Redefinição de senha',
                    message=mensagem,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email]
                )

                messages.success(
                    self.request,
                    'Verifique sua caixa de e-mail e siga as instruções, caso não esteja '
                    'encontrando, verifique também a caixa de spam.'
                )
            else:
                messages.error(
                    self.request,
                    'Erro na verificação do captcha'
                )
        else:
            messages.error(
                self.request,
                f'O email ( {email} ) não consta em nossa base de dados'
            )

        return redirect('users:users_passrecovery')


class NewPassWord(View):
    def get(self, *args, **kwargs):
        resetpwd_form_data = self.request.session.get(
            'resetpwd_form_data', None)
        email = self.kwargs['email']
        link = self.kwargs['link']

        reset_info = PasswordReset.objects.filter(
            email=email,
            link=link,
            recuperado='nao',
        ).first()

        if reset_info:
            if reset_info.validade >= timezone.now():
                user = User.objects.filter(
                    email=email,
                    id=reset_info.user_id,
                ).first()

                form = ResetPasswordForm(resetpwd_form_data)
                return render(
                    self.request,
                    'users/pages/password_reset.html',
                    context={
                        'form': form,
                    }
                )
            else:
                messages.error(
                    self.request,
                    'O link para redefinição expirou'
                )
            return redirect('users:users_users_passrecovery')
        else:
            messages.error(
                self.request,
                'Não foi possível utilizar o link de redefinição'
            )
            return redirect('users:users_passrecovery')

    def post(self, *args, **kwargs):
        if not self.request.POST:
            raise Http404

        email = self.kwargs['email']
        link = self.kwargs['link']

        reset_info = PasswordReset.objects.filter(
            email=email,
            link=link,
        ).first()

        user = User.objects.filter(
            id=reset_info.user_id,
            email=email,
        ).first()

        print(user.first_name)

        POST = self.request.POST
        self.request.session['resetpwd_form_data'] = POST

        form = ResetPasswordForm(
            data=POST or None,
            instance=user)

        if form.is_valid():
            alterpass = form.save(commit=False)
            alterpass.set_password(alterpass.password)
            alterpass.save()

            reset_info = PasswordReset.objects.filter(
                email=alterpass.email,
                user_id=alterpass.id,
            ).first()

            reset_info.recuperado = 'sim'
            reset_info.save()

            messages.success(
                self.request,
                'Sua senha foi alterada com sucesso'
            )
            return redirect('users:users_login')

        messages.error(
            self.request,
            'Houve um erro na sua solicitação'
        )
        return redirect(POST.get('returnpage', 'users:users_login'))


@method_decorator(
    login_required(
        login_url='users:users_login',
        redirect_field_name='next'
    ),
    name='dispatch'
)
class UserLogout(View):

    def post(self, *args, **kwargs):
        if not self.request.POST:
            messages.error(self.request, 'Solicitação inválida para o logout')
            return redirect(reverse('users:users_login'))

        if self.request.POST.get('username') != self.request.user.username:
            messages.error(self.request, 'Solicitação inválida para o usuário')
            return redirect(reverse('users:users_login'))

        messages.error(self.request, 'Logout efetuado com sucesso!')
        logout(self.request)
        return redirect(reverse('users:users_login'))


class UserRegister(TemplateView):
    template_name = 'users/pages/register.html'

    def get(self, *args, **kwargs):
        register_form_data = self.request.session.get(
            'register_form_data', None)
        form = RegisterForm(register_form_data)
        captcha_public_key = os.environ.get("RECAPTCHA_PUBLIC_KEY")

        context = self.get_context_data(**kwargs)

        return self.render_to_response({
            **context,
            'form': form,
            'captcha_public_key': captcha_public_key,
        })

    def post(self, *args, **kwargs):
        if not self.request.POST:
            raise Http404
        POST = self.request.POST
        self.request.session['register_form_data'] = POST
        form = RegisterForm(POST)

        if form.is_valid():

            if re_captcha(POST):
                user = form.save(commit=False)
                user.set_password(user.password)
                user.save()
                messages.success(
                    self.request,
                    'Seu cadastro foi criado com sucesso!'
                    'Por favor faça o login'
                )
                del(self.request.session['register_form_data'])
                return redirect(reverse('users:users_login'))
            else:
                messages.error(
                    self.request,
                    'Erro na verificação do captcha'
                )

        return redirect('users:users_register')


@method_decorator(
    login_required(
        login_url='users:users_login',
        redirect_field_name='next'
    ),
    name='dispatch'
)
class UserDashboard(View):
    template_name = 'users/pages/dashboard.html'

    def render_dashborad(self, conteudo, idmsg=None, imoveis=None, form=None):
        chats = Chat.objects.filter(
            Q(propietario=self.request.user.id) |
            Q(locador_id=self.request.user.id),
        ).order_by('-id')

        if idmsg:
            onechat = chats.filter(id=idmsg).first()
            if not onechat:
                raise Http404
            for chat in onechat.chatmensagens.filter(
                destinatario=self.request.user.id,
                lida='nao',
            ):
                chat.lida = 'sim'
                chat.save()

        else:
            onechat = None

        return render(
            self.request,
            'users/pages/dashboard.html',
            context={
                'conteudo': conteudo,
                'chats': chats,
                'onechat': onechat,
                'imoveis': imoveis,
                'form': form,
            }
        )

    def get(self, request, *args, **kwargs):

        conteudo = {
            'pagina': 'users/partials/inicial.html',
            'subtitulo': 'Esse é o seu painel de controle, veja abaixo '
            'tudo que poderá fazer por aqui',
        }

        return self.render_dashborad(conteudo)


class DashBoardImoveis(UserDashboard):

    def get(self, *args, **kwargs):
        imoveis = Imovel.objects.filter(
            propietario=self.request.user,
        )
        conteudo = {
            'pagina': 'users/partials/imoveis.html',
            'subtitulo': 'Veja todos os seus imóveis cadastrados',
        }

        return UserDashboard.render_dashborad(
            self,
            conteudo=conteudo,
            imoveis=imoveis,
        )


class DashBoardDadosPessoais(UserDashboard):
    def get(self, *args, **kwargs):
        user = User.objects.filter(
            id=self.request.user.id,
        ).first()

        if not user:
            raise Http404

        form = RegisterEditForm(instance=user)

        conteudo = {
            'pagina': 'users/partials/useredit.html',
            'subtitulo': 'Edite seus dados pessoais',
        }

        return UserDashboard.render_dashborad(
            self,
            conteudo=conteudo,
            form=form,
        )


class DashBoardDadosLogin(UserDashboard):
    def get(self, *args, **kwargs):
        user = User.objects.filter(
            id=self.request.user.id,
        ).first()

        if not user:
            raise Http404

        form = LoginEditForm(instance=user)

        conteudo = {
            'pagina': 'users/partials/loginedit.html',
            'subtitulo': 'Edite seus dados de login',
        }

        return UserDashboard.render_dashborad(
            self,
            conteudo=conteudo,
            form=form,
        )


class DashBoardMensagens(UserDashboard):
    def get(self, *args, **kwargs):
        idmsg = self.kwargs.get('idmsg', None)
        conteudo = {
            'pagina': 'users/partials/mensagens.html',
            'subtitulo': 'Suas mensagens',
        }

        if idmsg:
            conteudo = {
                'pagina': 'users/partials/mensagem.html',
                'subtitulo': 'Mensagem',
            }

        return UserDashboard.render_dashborad(
            self,
            conteudo=conteudo,
            idmsg=idmsg,
        )


@method_decorator(
    login_required(
        login_url='users:users_login',
        redirect_field_name='next'
    ),
    name='dispatch'
)
class DeleteImovel(View):
    def post(self, *args, **kwargs):

        imovel = Imovel.objects.filter(
            propietario=self.request.user,
            id=self.request.POST.get('imovelid')
        ).first()

        if imovel:
            imovel.delete()
            messages.success(
                self.request,
                'Imóvel  apagado com sucesso'
            )
        else:
            messages.error(
                self.request,
                'Não foi possível excluir o imóvel'
            )

        return redirect('users:dashboard_imoveis')


@method_decorator(
    login_required(
        login_url='users:users_login',
        redirect_field_name='next'
    ),
    name='dispatch'
)
class UserEdit(View):
    def post(self, *args, **kwargs):
        if not self.request.POST:
            raise Http404

        user = User.objects.filter(
            id=self.request.user.id,
        ).first()

        if not user:
            raise Http404

        POST = self.request.POST

        form = RegisterEditForm(
            data=POST or None,
            instance=user
        )

        if form.is_valid():
            form.save()
            messages.success(
                self.request,
                'Seu cadastro foi atualizado com sucesso'
            )
        else:
            messages.error(
                self.request,
                'Erro ao atualizar seu cadastro'
            )

        return redirect('users:dashboard_dadospessoais')


@method_decorator(
    login_required(
        login_url='users:users_login',
        redirect_field_name='next'
    ),
    name='dispatch'
)
class LoginEdit(View):
    def post(self, *args, **kwargs):
        if not self.request.POST:
            raise Http404

        user = User.objects.filter(
            id=self.request.user.id,
        ).first()

        if not user:
            raise Http404

        POST = self.request.POST

        form = LoginEditForm(
            data=POST or None,
            instance=user
        )

        emailExists = User.objects.filter(
            ~Q(id=user.id),
            email=self.request.POST.get('email'),
        ).exists()

        userExists = User.objects.filter(
            ~Q(id=user.id),
            username=self.request.POST.get('username'),
        ).exists()

        if emailExists:
            messages.error(
                self.request,
                'Já existe um cadastro para o endereço e email'
            )
            return redirect('users:dashboard_dadoslogin')

        if userExists:
            messages.error(
                self.request,
                'Usuário escolhido não está disponível'
            )
            return redirect('users:dashboard_dadoslogin')

        if self.request.POST.get('email') != self.request.POST.get('email2'):
            messages.error(
                self.request,
                'Os emails devem ser iguais'
            )
            return redirect('users:dashboard_dadoslogin')

        if self.request.POST.get('password') != self.request.POST.get('password2'):  # noqa
            messages.error(
                self.request,
                'As senhas devem ser iguais'
            )
            return redirect('users:dashboard_dadoslogin')

        if form.is_valid():
            edituser = form.save(commit=False)
            edituser.set_password(edituser.password)
            edituser.save()
            messages.success(
                self.request,
                'Seu cadastro foi atualizado com sucesso'
            )
        else:
            messages.error(
                self.request,
                'Erro ao atualizar seu cadastro. '
                'A senhha deve conter ao menos uma letra maiuscula, '
                'uma letra minuscula e um número. Mínimo de 8 carateres'
            )

        return redirect('users:dashboard_dadoslogin')
