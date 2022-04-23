from django.test import TestCase
from imoveis.models import Imovel
from users.models import User


class ImoveisMixin:
    def user_create(
        self,
        username='userteste',
        first_name='Teste First',
        last_name='Teste Last',
        email='email@teste.com',
        password='ABCDefgh123'
    ):
        return User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

    def create_imovel(
        self,
        titulo='Titulo teste',
        cep='00000-000',
        rua='Rua Teste',
        bairro='Bairro Teste',
        cidade='Cidade Teste',
        estado='RJ',
        valor_aluguel=500,
        paga_deposito='nao',
        valor_deposito=0,
        paga_iptu='nao',
        valor_iptu=0,
        paga_incendio='nao',
        valor_incendio=0,
        paga_luz='sim',
        paga_agua='sim',
        qtd_quarto=1,
        qtd_banheiro=1,
        qtd_vaga=0,
        idependente='sim',
        aceita_pet='sim',
        aceita_crianca='sim',
        comunidade='nao',
        comunidade_nome='',
        tipo_teto='laje',
        descricao='Descrição de teste',
        disponivel='sim',


    ):

        return Imovel.objects.create(
            titulo=titulo,
            cep=cep,
            rua=rua,
            bairro=bairro,
            cidade=cidade,
            estado=estado,
            valor_aluguel=valor_aluguel,
            paga_deposito=paga_deposito,
            valor_deposito=valor_deposito,
            paga_iptu=paga_iptu,
            valor_iptu=valor_iptu,
            paga_incendio=paga_incendio,
            valor_incendio=valor_incendio,
            paga_luz=paga_luz,
            paga_agua=paga_agua,
            qtd_quarto=qtd_quarto,
            qtd_banheiro=qtd_banheiro,
            qtd_vaga=qtd_vaga,
            idependente=idependente,
            aceita_pet=aceita_pet,
            aceita_crianca=aceita_crianca,
            comunidade=comunidade,
            comunidade_nome=comunidade_nome,
            tipo_teto=tipo_teto,
            descricao=descricao,
            disponivel=disponivel,
            propietario=self.user_create(),
        )


class ImoveisTestBase(TestCase, ImoveisMixin):
    def setUp(self) -> None:
        return super().setUp()
