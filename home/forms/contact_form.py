from django import forms


class ContactForm(forms.Form):

    choice_subject = (
        ('Dúvidas', 'Dúvidas'),
        ('Sugestões', 'Sugestões'),
        ('Criticas', 'Criticas'),
        ('Elogios', 'Elogios'),
        ('Outros assuntos', 'Outros assuntos'),
    )

    nome = forms.CharField(
        max_length=65,
        min_length=3,
        error_messages={
            'required': 'Nome é obrigatório',
            'max_length': 'Seu nome não pode ter mais de 65 caracteres',
            'min_length': 'Seu nome não pode ter menos de 3 caracteres',
        },
        required=True,
        label='Nome completo',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'nome',
                'type': 'text',
                'placeholder': 'Seu nome completo',
                'aria-label': 'Informe seu nome',
            }
        ),
    )

    email = forms.EmailField(
        max_length=200,
        min_length=10,
        error_messages={
            'required': 'E-mail obrigatório',
            'max_length': 'Seu e-mail não pode ultrapassar 200 caracteres',
            'min_length': 'Seu e-mail não pode ter menos de 10 caracteres',
        },
        required=True,
        label='Seu e-mail',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'email',
                'type': 'email',
                'placeholder': 'seu@email.com',
                'aria-label': 'Informe seu email',
            }
        ),
    )

    assunto = forms.ChoiceField(
        choices=choice_subject,
        error_messages={'required': 'Assunto obrigatório'},
        required=True,
        label='Assunto',
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'id': 'assunto',
                'aria-label': 'Selecione o assunto',
            }
        ),
    )

    mensagem = forms.CharField(
        max_length=600,
        min_length=50,
        error_messages={
            'required': 'Mensagem obrigatória',
            'max_length': 'Sua mensagem não pode ultrapassar 600 caracteres',
            'min_length': 'Sua mensagem deve ter no mínimo 50 caracteres',
        },
        required=True,
        label='Mensagem',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'id': 'mensagem',
                'placeholder': 'Escreva sua mensagem',
                'aria-label': 'Escreva sua mensagem',
            }
        )
    )
