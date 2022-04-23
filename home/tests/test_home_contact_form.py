from unittest import TestCase

from django.test import TestCase as DjangoTestCase
from django.urls import reverse
from home.forms.contact_form import ContactForm
from parameterized import parameterized


class HomeContactFormTest(TestCase):
    @parameterized.expand([
        ('nome', 'Seu nome completo'),
        ('email', 'seu@email.com'),
        ('mensagem', 'Escreva sua mensagem'),

    ])
    def test_fields_placeholder(self, field, placeholder):
        form = ContactForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        self.assertEqual(current_placeholder, placeholder)

    @parameterized.expand([
        ('nome', 'Informe seu nome'),
        ('email', 'Informe seu email'),
        ('assunto', 'Selecione o assunto'),
        ('mensagem', 'Escreva sua mensagem'),

    ])
    def test_fields_arialabel(self, field, arialabel):
        form = ContactForm()
        current_aria_label = form[field].field.widget.attrs['aria-label']
        self.assertEqual(current_aria_label, arialabel)

    @parameterized.expand([
        ('nome', 'Nome completo'),
        ('email', 'Seu e-mail'),
        ('assunto', 'Assunto'),
        ('mensagem', 'Mensagem'),

    ])
    def test_fields_label(self, field, label):
        form = ContactForm()
        current_label = form[field].field.label
        self.assertEqual(current_label, label)


class HomeContactFormIntegrationTest(DjangoTestCase):

    def setUp(self):
        self.form_data = {
            'nome': 'Nome Teste',
            'email': 'email@email.com',
            'assunto': 'Elogios',
            'mensagem': 'Esse é um teste de mensagem',
        }

        return super().setUp()

    @parameterized.expand([
        ('nome', 'Nome é obrigatório'),
        ('email', 'E-mail obrigatório'),
        ('assunto', 'Assunto obrigatório'),
        ('mensagem', 'Mensagem obrigatória'),
    ])
    def test_field_cannot_be_empty(self, field, errormsg):
        self.form_data[field] = ''
        url = reverse('mensagem:email_contato')

        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(errormsg, response.content.decode('utf-8'))
        self.assertIn(errormsg, response.context['form'].errors.get(field))

    def test_nome_field_max_length_65(self):
        self.form_data['nome'] = 'a' * 66
        url = reverse('mensagem:email_contato')

        msg = 'Seu nome não pode ter mais de 65 caracteres'
        response = self.client.post(url, self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('nome'))

    def test_nome_field_min_length_3(self):
        self.form_data['nome'] = 'a'
        url = reverse('mensagem:email_contato')

        msg = 'Seu nome não pode ter menos de 3 caracteres'
        response = self.client.post(url, self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('nome'))

    def test_email_field_max_length_200(self):
        self.form_data['email'] = 'a' * 201
        url = reverse('mensagem:email_contato')

        msg = 'Seu e-mail não pode ultrapassar 200 caracteres'
        response = self.client.post(url, self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('email'))

    def test_email_field_min_length_10(self):
        self.form_data['email'] = 'a'
        url = reverse('mensagem:email_contato')

        msg = 'Seu e-mail não pode ter menos de 10 caracteres'
        response = self.client.post(url, self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('email'))

    def test_mensagem_field_max_length_600(self):
        self.form_data['mensagem'] = 'a' * 601
        url = reverse('mensagem:email_contato')

        msg = 'Sua mensagem não pode ultrapassar 600 caracteres'
        response = self.client.post(url, self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('mensagem'))

    def test_mensagem_field_min_length_50(self):
        self.form_data['mensagem'] = 'a'
        url = reverse('mensagem:email_contato')

        msg = 'Sua mensagem deve ter no mínimo 50 caracteres'
        response = self.client.post(url, self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('mensagem'))
