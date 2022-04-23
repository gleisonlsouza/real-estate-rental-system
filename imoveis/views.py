from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum
from django.forms.models import inlineformset_factory
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView

from .forms.imovel_filter_form import FilterForm
from .forms.imovel_new_form import ImovelNewEditForm, ImovelNewEditFotoForm
from .models import Imovel, ImovelFoto


class ImoveisViewList(ListView):
    model = Imovel
    paginate_by = 9
    context_object_name = 'imoveis'
    template_name = 'imoveis/pages/imoveis_list.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            disponivel='sim',
        ).order_by('valor_aluguel')

        return qs

    def get(self, request, *args, **kwargs):
        form_data = {}

        GET = request.GET

        if not GET:
            if form_data:
                del(request.session['form_data'])
        else:
            request.session['form_data'] = GET
            form_data = request.session.get('form_data', None)

        form = FilterForm()
        if form_data:
            form = FilterForm(form_data)

        self.object_list = self.get_queryset()

        uf = request.GET.get('uf', '').strip()
        cidade = request.GET.get('cidade', '').strip()
        bairro = request.GET.get('bairro', '').strip()
        minaluguel = request.GET.get('minaluguel', '100').strip()
        maxaluguel = request.GET.get('maxaluguel', '1000').strip()
        deposito = request.GET.get('deposito', '').strip()
        iptu = request.GET.get('iptu', '').strip()
        incendio = request.GET.get('incendio', '').strip()
        agua = request.GET.get('agua', '').strip()
        luz = request.GET.get('luz', '').strip()
        quartos = request.GET.get('quartos', '').strip()
        banheiros = request.GET.get('banheiros', '').strip()
        vagas = request.GET.get('vagas', '').strip()
        independente = request.GET.get('independente', '').strip()
        pet = request.GET.get('pet', '').strip()
        crianca = request.GET.get('crianca', '').strip()
        comunidade = request.GET.get('comunidade', '').strip()
        teto = request.GET.get('teto', '').strip()

        if float(minaluguel) < float(maxaluguel):
            self.object_list = self.object_list.filter(
                disponivel='sim',
                estado__icontains=uf,
                cidade__icontains=cidade,
                bairro__icontains=bairro,
                valor_aluguel__range=(minaluguel, maxaluguel),
                paga_deposito__icontains=deposito,
                paga_iptu__icontains=iptu,
                paga_incendio__icontains=incendio,
                paga_agua__icontains=agua,
                paga_luz__icontains=luz,
                qtd_quarto__icontains=quartos,
                qtd_banheiro__icontains=banheiros,
                qtd_vaga__icontains=vagas,
                idependente__icontains=independente,
                aceita_pet__icontains=pet,
                aceita_crianca__icontains=crianca,
                comunidade__icontains=comunidade,
                tipo_teto__icontains=teto,

            )
        else:
            messages.error(request,
                           'O valor do aluguel inicial não pode ser menor que o valor final'
                           )

        context = self.get_context_data(**kwargs)
        return self.render_to_response({
            **context,
            'form': form,
        })


class ImoveisViewDetail(DetailView):
    model = Imovel
    context_object_name = 'imovel'
    template_name = 'imoveis/pages/imoveis_detail.html'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            disponivel='sim',
        ).annotate(total_mensal=Sum(F('valor_aluguel') + F('valor_iptu') + F('valor_incendio')))

        return qs


@method_decorator(
    login_required(
        login_url='users:users_login',
        redirect_field_name='next'
    ),
    name='dispatch'
)
class ImovelFotoUpload(View):

    def post(self, request, imovelID=None):
        imovel = Imovel.objects.get(
            propietario=self.request.user,
            pk=imovelID,
        )

        if not imovel:
            raise Http404

        fotos = request.FILES.getlist('images')

        if not fotos:
            messages.error(
                request, 'Você precisa selecionar pelo menos uma foto')

        else:
            i = 0
            for foto in fotos:
                # flake8: noqa
                NovaFoto = ImovelFoto.objects.create(
                    imovel=imovel,
                    foto=foto,
                )
                i += 1
            if i == 1:
                messages.success(
                    request, f'{i} nova foto foi adicionada')
            else:
                messages.success(
                    request, f'{i} novas fotos foram adicionadas')

        return redirect('imoveis:imoveis_edit', imovelID)


@method_decorator(
    login_required(
        login_url='users:users_login',
        redirect_field_name='next'
    ),
    name='dispatch'
)
class ImovelFotoDelete(View):

    def post(self, request, imovelID=None, fotoID=None):
        imovel = Imovel.objects.get(
            propietario=self.request.user,
            pk=imovelID,
        )

        if not imovel:
            raise Http404

        if imovel:
            foto = ImovelFoto.objects.filter(
                imovel_id=imovelID,
                pk=fotoID,
            ).first()
            if not foto:
                raise Http404
            foto.delete()

            return redirect('imoveis:imoveis_edit', imovelID)


@method_decorator(
    login_required(
        login_url='users:users_login',
        redirect_field_name='next'
    ),
    name='dispatch'
)
class ImoveisAddEdit(View):
    def get_imovel(self, pk=None):
        imovel = None
        if pk:
            imovel = Imovel.objects.filter(
                propietario=self.request.user,
                pk=pk,
            ).first()

            if not imovel:
                raise Http404()
        return imovel

    def render_imovel(self, form, fotos):
        return render(
            self.request,
            'imoveis/pages/imoveis_new_edit.html',
            context={
                'form': form,
                'fotos': fotos,
            }
        )

    def get(self, rquest, pk=None):
        imovel = self.get_imovel(pk)
        foto_formset = inlineformset_factory(
            Imovel, ImovelFoto,
            form=ImovelNewEditFotoForm, extra=1, can_delete=True)

        fotos = foto_formset(instance=imovel)
        form = ImovelNewEditForm(instance=imovel)

        return self.render_imovel(form, fotos)

    def post(self, request, pk=None):
        imovel = self.get_imovel(pk)

        foto_formset = inlineformset_factory(
            Imovel, ImovelFoto,
            form=ImovelNewEditFotoForm, extra=1, can_delete=True)

        fotos = foto_formset(instance=imovel)

        form = ImovelNewEditForm(
            data=request.POST or None,
            files=request.FILES or None,
            instance=imovel,
        )

        if form.is_valid():
            imovel = form.save(commit=False)

            imovel.propietario = request.user
            imovel.save()

            messages.success(
                request,
                'Seu imóvel foi cadastrado/atualizado com sucesso!'
            )

            return redirect(reverse(
                'imoveis:imoveis_edit',
                args=(imovel.pk,),
            )
            )
        messages.error(
            request,
            'Corrija os erros do formulário'
        )
        return self.render_imovel(form, fotos)
