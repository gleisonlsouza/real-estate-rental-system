from django.http import JsonResponse
from django.views.generic import TemplateView
from imoveis.models import Imovel

from .forms.contact_form import ContactForm


class HomeView(TemplateView):
    template_name = 'home/pages/home.html'

    def get(self, *args, **kwargs):

        contact_form_data = self.request.session.get(
            'contact_form_data', None)

        form = ContactForm(contact_form_data)

        return self.render_to_response({
            'context': self.get_context_data(**kwargs),
            'form': form,
        })


# Função que retornar valores ao autocomplete
def AutoComplete(request):
    uf = request.GET.get('uf')
    cidade = request.GET.get('cidade')
    bairro = request.GET.get('bairro')
    payload = []

    if uf:
        retorno_ufs = Imovel.objects.filter(estado__icontains=uf)

        for retorno_uf in retorno_ufs:
            payload.append(retorno_uf.estado)

    if cidade:
        retorno_cidades = Imovel.objects.filter(cidade__icontains=cidade)

        for retorno_cidade in retorno_cidades:
            payload.append(retorno_cidade.cidade)

    if bairro:
        retorno_bairros = Imovel.objects.filter(bairro__icontains=bairro)

        for retorno_bairro in retorno_bairros:
            payload.append(retorno_bairro.bairro)

    payload = list(dict.fromkeys(payload))
    return JsonResponse({'status': 200, 'data': payload})
