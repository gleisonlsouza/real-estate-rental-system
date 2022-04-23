import locale
from collections import defaultdict

from django import forms

from ..models import Imovel, ImovelFoto


class ImovelNewEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)

        self.fields.get('titulo').widget.attrs['class'] = 'form-control'
        self.fields.get(
            'titulo').widget.attrs['placeholder'] = 'Digite um título'
        self.fields.get(
            'titulo').widget.attrs['aria-label'] = 'Título do anúncio'

        self.fields.get('cep').widget.attrs['class'] = 'form-control'
        self.fields.get('cep').widget.attrs['id'] = 'cep'
        self.fields.get(
            'cep').widget.attrs['placeholder'] = '00000-000'
        self.fields.get('cep').widget.attrs['data-mask'] = '00000-000'
        self.fields.get(
            'cep'
        ).widget.attrs['aria-label'] = 'CEP do imóvel'

        self.fields.get('rua').widget.attrs['class'] = 'form-control'
        self.fields.get(
            'rua').widget.attrs['placeholder'] = 'Digite o nome da rua'
        self.fields.get('rua').widget.attrs['id'] = 'rua'
        self.fields.get(
            'rua'
        ).widget.attrs['aria-label'] = 'Rua onde se localiza o imóvel'

        self.fields.get('bairro').widget.attrs['class'] = 'form-control'
        self.fields.get('bairro').widget.attrs['id'] = 'bairro'
        self.fields.get(
            'bairro'
        ).widget.attrs['aria-label'] = 'Bairro onde se localiza o imóvel'

        self.fields.get('cidade').widget.attrs['class'] = 'form-control'
        self.fields.get('cidade').widget.attrs['id'] = 'cidade'

        self.fields.get(
            'cidade'
        ).widget.attrs['aria-label'] = 'Cidade onde se localiza o imóvel'

        self.fields.get(
            'estado').widget.attrs['class'] = 'form-control text-uppercase'
        self.fields.get('estado').widget.attrs['id'] = 'estado'
        self.fields.get('estado').widget.attrs['maxlength'] = '2'
        self.fields.get(
            'estado'
        ).widget.attrs['aria-label'] = 'Estado onde se localiza o imóvel'

        self.fields.get('valor_aluguel').widget.attrs['class'] = 'form-control'

        self.fields.get('valor_aluguel').widget.localize = True
        self.fields.get(
            'valor_aluguel').help_text = (
                'Mínimo R$ 100,00 Máximo R$ 1000,00')
        self.fields.get(
            'valor_aluguel').widget.attrs['placeholder'] = 'Ex.: 600,00'
        self.fields.get(
            'valor_aluguel').widget.attrs['aria-label'] = 'Valor do aluguel'

        self.fields.get('paga_deposito').widget.attrs['class'] = 'form-select'
        self.fields.get(
            'paga_deposito'
        ).widget.attrs['aria-label'] = 'Paga depósito?'

        self.fields.get(
            'valor_deposito').widget.attrs['class'] = 'form-control'
        self.fields.get('valor_deposito').widget.localize = True
        self.fields.get(
            'valor_deposito').widget.attrs['placeholder'] = 'Ex.: 600,00'
        self.fields.get(
            'valor_deposito').widget.attrs['aria-label'] = 'Valor do depósito'

        self.fields.get('paga_iptu').widget.attrs['class'] = 'form-select'
        self.fields.get(
            'paga_iptu'
        ).widget.attrs['aria-label'] = 'Paga IPTU?'

        self.fields.get(
            'valor_iptu').widget.attrs['class'] = 'form-control'
        self.fields.get('valor_iptu').widget.localize = True
        self.fields.get(
            'valor_iptu').widget.attrs['placeholder'] = 'Ex.: 600,00'
        self.fields.get(
            'valor_iptu').widget.attrs['aria-label'] = 'Valor do IPTU'

        self.fields.get('paga_incendio').widget.attrs['class'] = 'form-select'
        self.fields.get(
            'paga_incendio'
        ).widget.attrs['aria-label'] = 'Paga taxa de incêncio?'

        self.fields.get(
            'valor_incendio').widget.attrs['class'] = 'form-control'
        self.fields.get('valor_incendio').widget.localize = True
        self.fields.get(
            'valor_incendio').widget.attrs['placeholder'] = 'Ex.: 600,00'
        self.fields.get(
            'valor_incendio'
        ).widget.attrs['aria-label'] = 'Valor da taxa de incêncio'

        self.fields.get('paga_luz').widget.attrs['class'] = 'form-select'
        self.fields.get(
            'paga_luz'
        ).widget.attrs['aria-label'] = 'Paga luz?'

        self.fields.get('paga_agua').widget.attrs['class'] = 'form-select'
        self.fields.get(
            'paga_agua'
        ).widget.attrs['aria-label'] = 'Paga água?'

        self.fields.get('qtd_quarto').widget.attrs['class'] = 'form-select'
        self.fields.get(
            'qtd_quarto'
        ).widget.attrs['aria-label'] = 'Quantidade de quartos'

        self.fields.get('qtd_banheiro').widget.attrs['class'] = 'form-select'
        self.fields.get(
            'qtd_banheiro'
        ).widget.attrs['aria-label'] = 'Quantidade de banheiros'

        self.fields.get('qtd_vaga').widget.attrs['class'] = 'form-select'
        self.fields.get(
            'qtd_vaga'
        ).widget.attrs['aria-label'] = 'Quantidade de vagas na garagem'

        self.fields.get('idependente').widget.attrs['class'] = 'form-select'
        self.fields.get(
            'idependente'
        ).widget.attrs['aria-label'] = 'A casa é idependente?'

        self.fields.get('aceita_pet').widget.attrs['class'] = 'form-select'
        self.fields.get(
            'aceita_pet'
        ).widget.attrs['aria-label'] = 'Aceita pet?'

        self.fields.get('aceita_crianca').widget.attrs['class'] = 'form-select'
        self.fields.get(
            'aceita_crianca'
        ).widget.attrs['aria-label'] = 'Aceita criança?'

        self.fields.get('comunidade').widget.attrs['class'] = 'form-select'
        self.fields.get(
            'comunidade'
        ).widget.attrs['aria-label'] = 'É comunidade?'

        self.fields.get(
            'comunidade_nome').widget.attrs['class'] = 'form-control'
        self.fields.get(
            'comunidade_nome').widget.attrs['placeholder'] = 'Nome da comunidade'  # noqa
        self.fields.get(
            'comunidade_nome'
        ).widget.attrs['aria-label'] = 'Nome da comunidade, caso seja em comunidade'  # noqa

        self.fields.get('tipo_teto').widget.attrs['class'] = 'form-select'
        self.fields.get(
            'tipo_teto'
        ).widget.attrs['aria-label'] = 'Tipo do teto da casa'

        self.fields.get(
            'descricao').widget.attrs['class'] = 'form-control'
        self.fields.get(
            'descricao').widget.attrs['placeholder'] = 'Digite uma breve descrição do seu imóvel'  # noqa
        self.fields.get(
            'descricao'
        ).widget.attrs['aria-label'] = 'Descrição do imóvel'  # noqa

        self.fields.get('disponivel').widget.attrs['class'] = 'form-select'
        self.fields.get(
            'disponivel'
        ).widget.attrs['aria-label'] = 'Está disponível para locação?'

    class Meta:
        model = Imovel
        fields = [
            'id',
            'titulo',
            'cep',
            'rua',
            'bairro',
            'cidade',
            'estado',
            'valor_aluguel',
            'paga_deposito',
            'valor_deposito',
            'paga_iptu',
            'valor_iptu',
            'paga_incendio',
            'valor_incendio',
            'paga_luz',
            'paga_agua',
            'qtd_quarto',
            'qtd_banheiro',
            'qtd_vaga',
            'idependente',
            'aceita_pet',
            'aceita_crianca',
            'comunidade',
            'comunidade_nome',
            'tipo_teto',
            'descricao',
            'disponivel',
        ]

    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)

        cleanded_data = self.cleaned_data

        titulo = cleanded_data.get('titulo')
        estado = cleanded_data.get('estado')
        cidade = cleanded_data.get('cidade')
        bairro = cleanded_data.get('bairro')
        valor_aluguel = cleanded_data.get('valor_aluguel')
        paga_deposito = cleanded_data.get('paga_deposito')
        valor_deposito = cleanded_data.get('valor_deposito')
        paga_iptu = cleanded_data.get('paga_iptu')
        valor_iptu = cleanded_data.get('valor_iptu')
        paga_incendio = cleanded_data.get('paga_incendio')
        valor_incendio = cleanded_data.get('valor_incendio')
        comunidade = cleanded_data.get('comunidade')
        comunidade_nome = cleanded_data.get('comunidade_nome')

        if len(titulo) < 10 or len(titulo) > 65:
            self._my_errors['titulo'].append(
                'Precisa ter entre 10 e 65 caracteres')

        if not estado:
            self._my_errors['estado'].append(
                'Selecione um estado')

        if not cidade:
            self._my_errors['cidade'].append(
                'Selecione uma cidade')

        if not bairro:
            self._my_errors['bairro'].append(
                'Selecione um bairro')

        if not valor_aluguel:
            self._my_errors['valor_aluguel'].append(
                'Digite o valor do aluguel')

        if (valor_aluguel < 100) or (valor_aluguel > 1000):
            self._my_errors['valor_aluguel'].append(
                'O valor mínimo é R$ 100,00 e o máximo R$ 1.000,00')

        if paga_deposito == 'sim':
            deposito = valor_aluguel * 3
            if valor_deposito < valor_aluguel or valor_deposito > deposito:
                self._my_errors['valor_deposito'].append(
                    'Você marcou que paga depósito, '
                    'então defina um valor entre '
                    f'{locale.currency(valor_aluguel)} e {locale.currency(deposito)}'  # noqa
                    ' (3 Meses de aluguel)')

        if paga_deposito == 'nao' and valor_deposito > 0:
            self._my_errors['valor_deposito'].append(
                'Você disse que não paga depósito. '
                'Então o valor deve ser zerado.')

        if paga_iptu == 'sim':
            if valor_iptu < 1:
                self._my_errors['valor_iptu'].append(
                    'Você marcou que paga IPTU, '
                    'então informe um valor.')

        if paga_iptu == 'nao' and valor_iptu != 0:
            self._my_errors['valor_iptu'].append(
                'Você disse que não paga IPTU. '
                'Então o valor deve ser zerado')

        if paga_incendio == 'sim':
            if valor_incendio < 1:
                self._my_errors['valor_incendio'].append(
                    'Você marcou que paga taxa de incêndio, '
                    'então informe um valor.')

        if paga_incendio == 'nao' and valor_incendio != 0:
            self._my_errors['valor_incendio'].append(
                'Você disse que não paga taxa de incêndio. '
                'Então o valor deve ser zerado')

        if comunidade == 'nao' and comunidade_nome:
            self._my_errors['comunidade_nome'].append(
                'Você disse que não é comunidade. '
                'Então o nome deve estar em branco')

        if comunidade == 'sim' and not comunidade_nome:
            self._my_errors['comunidade_nome'].append(
                'Você disse que é comunidade. '
                'Então informe o nome da comunidade')

        if self._my_errors:
            raise forms.ValidationError(self._my_errors)

        return super_clean


class ImovelNewEditFotoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields.get(
            'foto').widget.attrs['class'] = 'form-control'

    class Meta:
        model = ImovelFoto
        fields = [
            'id',
            'foto'
        ]
