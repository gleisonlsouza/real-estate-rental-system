from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import View
from home.forms.contact_form import ContactForm
from imoveis.models import Imovel
from users.models import User

from .models import Chat, Mensagens


class ChatMessages(View):

    def post(self, *args, **kwargs):
        if not self.request.POST:
            raise Http404

        POST = self.request.POST

        locador = User.objects.filter(
            id=POST.get('locador')
        ).first()

        propietario = POST.get('propietario')

        imovel_id = Imovel.objects.filter(
            id=POST.get('imovel_id')
        ).first()

        titulo = POST.get('titulo')
        mensagem = POST.get('mensagem')
        autor = POST.get('autor')
        destinatario = POST.get('destinatario')

        chat = Chat.objects.filter(
            locador=locador,
            propietario=propietario,
            imovel_id=imovel_id,
        ).first()

        if not chat:
            chat = Chat.objects.create(
                locador=locador,
                propietario=propietario,
                imovel_id=imovel_id,
                titulo=titulo,
            )

        msg = Mensagens.objects.create(
            chat=chat,
            autor=autor,
            destinatario=destinatario,
            mensagem=mensagem,
        )
        if msg:
            return redirect(f'/users/dashboard/mensagens/{chat.id}')


class Contato(View):
    def get(self, *args, **kwargs):
        raise Http404

    def post(self, *args, **kwargs):
        if not self.request.POST:
            raise Http404
        POST = self.request.POST
        self.request.session['contact_form_data'] = POST
        form = ContactForm(POST)
        nome = POST.get('nome')
        email = POST.get('email')
        assunto = POST.get('assunto')
        mensagem = f'''
            Nome: { nome } 
            Email: {email}
            
            Assunto: { assunto }

            Mensagem:

            {POST.get('mensagem')}

        '''

        if form.is_valid():
            send_mail(
                subject=assunto,
                message=mensagem,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['gleison.lsouza@gmail.com',
                                settings.EMAIL_HOST_USER]
            )
            messages.success(
                self.request,
                'Mensagem enviada com sucesso!'
            )
            del(self.request.session['contact_form_data'])
        else:
            messages.error(
                self.request,
                'Erro ao enviar mensagem'
            )

        return redirect('/#contato')
