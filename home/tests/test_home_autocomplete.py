from django.urls import reverse
from imoveis.tests.test_imoveis_base import ImoveisTestBase


class HomeAutoCompleteTest(ImoveisTestBase):
    def test_uf_return_autocomplete(self):
        self.create_imovel(estado='SP')
        url = reverse('home:autocomplete')
        response = self.client.get(url+'?uf=sp')
        self.assertIn('SP', response.content.decode('utf-8'))

    def test_cidade_return_autocomplete(self):
        self.create_imovel(cidade='Rio de Janeiro')
        url = reverse('home:autocomplete')
        response = self.client.get(url+'?cidade=Rio de Janeiro')
        self.assertIn('Rio de Janeiro', response.content.decode('utf-8'))

    def test_bairro_return_autocomplete(self):
        self.create_imovel(bairro='Pilar')
        url = reverse('home:autocomplete')
        response = self.client.get(url+'?bairro=Pilar')
        self.assertIn('Pilar', response.content.decode('utf-8'))
