from collections import defaultdict

from django import forms


class FilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._my_errors = defaultdict(list)

        self.fields.get(
            'uf').widget.attrs['class'] = 'form-control text-uppercase'
        self.fields.get('uf').widget.attrs['id'] = 'uf'
        self.fields.get(
            'uf').widget.attrs['placeholder'] = 'Ex.: RJ'
        self.fields.get('uf').widget.attrs['maxlength'] = '2'
        self.fields.get(
            'uf').widget.attrs['aria-label'] = 'Selecionar estado'

        self.fields.get(
            'cidade').widget.attrs['class'] = 'form-control text-uppercase'
        self.fields.get('cidade').widget.attrs['id'] = 'cidade'
        self.fields.get(
            'cidade').widget.attrs['placeholder'] = 'Ex.: Duque de Caxias'
        self.fields.get('cidade').widget.attrs['maxlength'] = '65'
        self.fields.get(
            'cidade').widget.attrs['aria-label'] = 'Selecionar a cidade'

        self.fields.get(
            'bairro').widget.attrs['class'] = 'form-control text-uppercase'
        self.fields.get('bairro').widget.attrs['id'] = 'bairro'
        self.fields.get(
            'bairro').widget.attrs['placeholder'] = 'Ex.: Pilar'
        self.fields.get('bairro').widget.attrs['maxlength'] = '65'
        self.fields.get(
            'bairro').widget.attrs['aria-label'] = 'Selecionar o bairro'

        self.fields.get(
            'minaluguel').widget.attrs['class'] = 'form-select  form-select-xl'
        self.fields.get('minaluguel').widget.attrs['id'] = 'minaluguel'
        self.fields.get(
            'minaluguel'
        ).widget.attrs['aria-label'] = 'Selecione o valor inicial'

        self.fields.get(
            'maxaluguel').widget.attrs['class'] = 'form-select  form-select-xl'
        self.fields.get('maxaluguel').widget.attrs['id'] = 'maxaluguel'
        self.fields.get(
            'maxaluguel'
        ).widget.attrs['aria-label'] = 'Selecione o valor final'

        self.fields.get(
            'deposito').widget.attrs['class'] = 'form-select  form-select-xl'
        self.fields.get('deposito').widget.attrs['id'] = 'deposito'
        self.fields.get(
            'deposito'
        ).widget.attrs['aria-label'] = 'Selecione se paga depósito ou não'

        self.fields.get(
            'iptu').widget.attrs['class'] = 'form-select  form-select-xl'
        self.fields.get('iptu').widget.attrs['id'] = 'iptu'
        self.fields.get(
            'iptu'
        ).widget.attrs['aria-label'] = 'Selecione se paga IPTU ou não'

        self.fields.get(
            'incendio').widget.attrs['class'] = 'form-select  form-select-xl'
        self.fields.get('incendio').widget.attrs['id'] = 'incendio'
        self.fields.get(
            'incendio'
        ).widget.attrs['aria-label'] = 'Selecione se paga taxa de incêndio'

        self.fields.get(
            'agua').widget.attrs['class'] = 'form-select  form-select-xl'
        self.fields.get('agua').widget.attrs['id'] = 'agua'
        self.fields.get(
            'agua'
        ).widget.attrs['aria-label'] = 'Selecione se paga água'

        self.fields.get(
            'luz').widget.attrs['class'] = 'form-select  form-select-xl'
        self.fields.get('luz').widget.attrs['id'] = 'luz'
        self.fields.get(
            'luz'
        ).widget.attrs['aria-label'] = 'Selecione se paga luz'

        self.fields.get(
            'quartos').widget.attrs['class'] = 'form-select  form-select-xl'
        self.fields.get('quartos').widget.attrs['id'] = 'quartos'
        self.fields.get(
            'quartos'
        ).widget.attrs['aria-label'] = 'Selecione a quantidade de quartos'

        self.fields.get(
            'banheiros').widget.attrs['class'] = 'form-select  form-select-xl'
        self.fields.get('banheiros').widget.attrs['id'] = 'banheiros'
        self.fields.get(
            'banheiros'
        ).widget.attrs['aria-label'] = 'Selecione a quantidade de banheiros'

        self.fields.get(
            'vagas').widget.attrs['class'] = 'form-select  form-select-xl'
        self.fields.get('vagas').widget.attrs['id'] = 'vagas'
        self.fields.get(
            'vagas'
        ).widget.attrs['aria-label'] = 'Selecione a quantidade de vagas na garagem'  # noqa

        self.fields.get(
            'independente').widget.attrs['class'] = 'form-select  form-select-xl'  # noqa
        self.fields.get('independente').widget.attrs['id'] = 'independente'
        self.fields.get(
            'independente'
        ).widget.attrs['aria-label'] = 'Selecione se a casa é independente ou não'  # noqa

        self.fields.get(
            'pet').widget.attrs['class'] = 'form-select  form-select-xl'  # noqa
        self.fields.get('pet').widget.attrs['id'] = 'pet'
        self.fields.get(
            'pet'
        ).widget.attrs['aria-label'] = 'Selecione se aceeita pet ou não'  # noqa

        self.fields.get(
            'crianca').widget.attrs['class'] = 'form-select  form-select-xl'  # noqa
        self.fields.get('crianca').widget.attrs['id'] = 'crianca'
        self.fields.get(
            'crianca'
        ).widget.attrs['aria-label'] = 'Selecione se aceeita criança ou não'  # noqa

        self.fields.get(
            'comunidade').widget.attrs['class'] = 'form-select  form-select-xl'  # noqa
        self.fields.get('comunidade').widget.attrs['id'] = 'comunidade'
        self.fields.get(
            'comunidade'
        ).widget.attrs['aria-label'] = 'Selecione se é comunidade ou não'  # noqa

        self.fields.get(
            'teto').widget.attrs['class'] = 'form-select  form-select-xl'  # noqa
        self.fields.get('teto').widget.attrs['id'] = 'teto'
        self.fields.get(
            'teto'
        ).widget.attrs['aria-label'] = 'Selecione o tipo de teto'  # noqa

    choice_min_aluguel = (
        (100, 'R$ 100,00'),
        (200, 'R$ 200,00'),
        (300, 'R$ 300,00'),
        (400, 'R$ 400,00'),
        (500, 'R$ 500,00'),
        (600, 'R$ 600,00'),
        (700, 'R$ 700,00'),
        (800, 'R$ 800,00'),
        (900, 'R$ 900,00'),

    )

    choice_max_aluguel = (
        (1000, 'R$ 1000,00'),
        (900, 'R$ 900,00'),
        (800, 'R$ 800,00'),
        (700, 'R$ 700,00'),
        (600, 'R$ 600,00'),
        (500, 'R$ 500,00'),
        (400, 'R$ 400,00'),
        (300, 'R$ 300,00'),
        (200, 'R$ 200,00'),

    )

    choice_no_yes = (
        ('', 'Todos'),
        ('nao', 'Não'),
        ('sim', 'Sim'),
    )

    choice_yes_no = (
        ('', 'Todos'),
        ('sim', 'Sim'),
        ('nao', 'Não'),
    )

    choice_1_to_4 = (
        ('', 'Todos'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    )

    choice_0_to_3 = (
        ('', 'Todos'),
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
    )

    choice_teto = (
        ('', 'Todos'),
        ('laje', 'Laje'),
        ('telhado', 'Telhado'),
        ('ambos', 'Ambos'),
    )

    uf = forms.CharField(max_length=2, required=False, initial='')
    cidade = forms.CharField(max_length=65, required=False, initial='')
    bairro = forms.CharField(max_length=65, required=False, initial='')
    minaluguel = forms.ChoiceField(choices=choice_min_aluguel)
    maxaluguel = forms.ChoiceField(choices=choice_max_aluguel)
    deposito = forms.ChoiceField(choices=choice_no_yes, required=False)
    iptu = forms.ChoiceField(choices=choice_no_yes, required=False)
    incendio = forms.ChoiceField(choices=choice_no_yes, required=False)
    agua = forms.ChoiceField(choices=choice_yes_no, required=False)
    luz = forms.ChoiceField(choices=choice_yes_no, required=False)
    quartos = forms.ChoiceField(choices=choice_1_to_4, required=False)
    banheiros = forms.ChoiceField(choices=choice_1_to_4, required=False)
    vagas = forms.ChoiceField(choices=choice_0_to_3, required=False)
    independente = forms.ChoiceField(choices=choice_yes_no, required=False)
    pet = forms.ChoiceField(choices=choice_yes_no, required=False)
    crianca = forms.ChoiceField(choices=choice_yes_no, required=False)
    comunidade = forms.ChoiceField(choices=choice_no_yes, required=False)
    teto = forms.ChoiceField(choices=choice_teto, required=False)

    fields = [
        'uf',
        'cidade',
        'bairro',
        'minaluguel',
        'maxaluguel',
        'deposito',
        'iptu',
        'incendio',
        'agua',
        'luz',
        'quartos',
        'banheiros',
        'vagas',
        'independente',
        'pet',
        'crianca',
        'comunidade',
        'teto',
    ]

    def clean(self):
        super_clean = super().clean()

        cleanded_data = self.cleaned_data

        minaluguel = cleanded_data.get('minaluguel')
        maxaluguel = cleanded_data.get('maxaluguel')

        if float(minaluguel) > float(maxaluguel):
            self._my_errors['minaluguel'].append(
                'O valor mínimo não pode ser maior que o máximo'
            )

        if self._my_errors:
            raise forms.ValidationError(self._my_errors)

        return super_clean
