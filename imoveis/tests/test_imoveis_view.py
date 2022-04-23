
from django.urls import resolve, reverse
from imoveis import views

from .test_imoveis_base import ImoveisTestBase


class ImoveisViewListTest(ImoveisTestBase):

    def test_imoveis_view_list_function_is_correct(self):
        view = resolve(reverse('imoveis:imoveis_view_list'))
        self.assertIs(view.func.view_class, views.ImoveisViewList)

    def test_show_alert_if_not_imovel_found(self):
        url = reverse('imoveis:imoveis_view_list')

        response = self.client.get(url)
        mensagem = 'Parece que não conseguimos encontrar um imóvel como você deseja'  # noqa
        self.assertIn(mensagem, response.content.decode('utf-8'))

    def test_if_load_imoveis_in_template(self):
        self.create_imovel(titulo='Minha casa', bairro='Pilar',
                           cidade='Duque de Caxias', estado='RJ')
        response = self.client.get(reverse('imoveis:imoveis_view_list'))
        self.assertIn('Minha casa', response.content.decode('utf-8'))
        self.assertIn('Pilar,Duque de Caxias-RJ',
                      response.content.decode('utf-8'))
