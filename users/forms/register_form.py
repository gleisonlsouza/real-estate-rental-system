from django import forms
from django.core.exceptions import ValidationError
from utils.django_forms import strong_password

from ..models import User


class RegisterForm(forms.ModelForm):

    choices_locador_proprietario = (
        ('locador', 'Locador'),
        ('proprietario', 'Proprietário')
    )

    username = forms.CharField(
        error_messages={'required': 'Informe um usuário'},
        required=True,
        label='Usuário',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'aria-label': 'Informe um usuário',
                'placeholder': 'Informe um usuário'
            }
        ),
    )

    first_name = forms.CharField(
        error_messages={'required': 'Informe seu primeiro nome'},
        required=True,
        label='Primeiro nome',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'aria-label': 'Informe seu primeiro nome',
            }
        ),
    )

    last_name = forms.CharField(
        error_messages={'required': 'Informe seu sobrenome'},
        required=True,
        label='Sobrenome',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'aria-label': 'Informe seu sobrenome',
            }
        ),
    )

    email = forms.CharField(
        error_messages={'required': 'Informe seu email'},
        required=True,
        label='E-mail',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'email',
                'aria-label': 'Informe seu email',
                'placeholder': 'seu@email.com',
            }
        ),
    )

    email2 = forms.CharField(
        error_messages={'required': 'Repita seu email'},
        required=True,
        label='Repita o E-mail',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'email',
                'aria-label': 'Repita seu email',
                'placeholder': 'seu@email.com',
            }
        ),
    )

    password = forms.CharField(
        error_messages={'required': 'Informe uma senha'},
        required=True,
        label='Senha',
        validators=[strong_password],
        help_text=(
            'Deve conter ao menos uma letra maiuscula,'
            'uma letra minuscula e um número. '
            'Mínimo de 8 carateres'
        ),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type': 'password',
                'aria-label': 'Informe uma senha',
                'placeholder': 'Informe uma senha',
            }
        ),
    )

    password2 = forms.CharField(
        error_messages={'required': 'Repita a senha'},
        required=True,
        label='Repita a senha',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type': 'password',
                'aria-label': 'Repita a senha',
                'placeholder': 'Repita a senha',
            }
        ),
    )

    celular = forms.CharField(
        error_messages={'required': 'Informe um celular'},
        required=True,
        label='Celular',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'tel',
                'aria-label': 'Informe um celular',
                'placeholder': '(00) 00000-0000',
            }
        ),
    )

    tipo_usuario = forms.CharField(
        error_messages={'required': 'Selecione uma opção'},
        required=True,
        label='Eu sou',
        widget=forms.Select(
            choices=choices_locador_proprietario,
            attrs={
                'class': 'form-select',
            }
        ),
    )

    termos = forms.BooleanField(
        error_messages={'required': 'Você precisa aceitar o contrato'},
        required=True,
        label='Aceite dos termos',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input primary-color',
                'type': 'checkbox',
                'aria-label': 'Aceite dos termos',
            }
        ),
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'celular',
            'tipo_usuario'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'Já existe um cadastro com esse email', code='invalid',
            )

        return email

    def clean_email2(self):
        email = self.cleaned_data.get('email', '')
        email2 = self.cleaned_data.get('email2', '')

        if email != email2:
            raise ValidationError(
                'Os emails devem ser iguais'
            )

        return email2

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError({
                'password2': 'As senhas devem ser iguais',
            })


class RegisterEditForm(forms.ModelForm):

    choices_locador_proprietario = (
        ('locador', 'Locador'),
        ('proprietario', 'Proprietário')
    )

    first_name = forms.CharField(
        error_messages={'required': 'Informe seu primeiro nome'},
        required=True,
        label='Primeiro nome',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'aria-label': 'Informe seu primeiro nome',
            }
        ),
    )

    last_name = forms.CharField(
        error_messages={'required': 'Informe seu sobrenome'},
        required=True,
        label='Sobrenome',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'aria-label': 'Informe seu sobrenome',
            }
        ),
    )

    celular = forms.CharField(
        error_messages={'required': 'Informe um celular'},
        required=True,
        label='Celular',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'tel',
                'aria-label': 'Informe um celular',
                'placeholder': '(00) 00000-0000',
            }
        ),
    )

    tipo_usuario = forms.CharField(
        error_messages={'required': 'Selecione uma opção'},
        required=True,
        label='Eu sou',
        widget=forms.Select(
            choices=choices_locador_proprietario,
            attrs={
                'class': 'form-select',
            }
        ),
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'celular',
            'tipo_usuario'
        ]


class LoginEditForm(forms.ModelForm):

    username = forms.CharField(
        error_messages={'required': 'Informe um usuário'},
        required=True,
        label='Usuário',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'aria-label': 'Informe um usuário',
                'placeholder': 'Informe um usuário'
            }
        ),
    )

    email = forms.CharField(
        error_messages={'required': 'Informe seu email'},
        required=True,
        label='E-mail',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'email',
                'aria-label': 'Informe seu email',
                'placeholder': 'seu@email.com',
            }
        ),
    )

    email2 = forms.CharField(
        error_messages={'required': 'Repita seu email'},
        required=True,
        label='Repita o E-mail',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'email',
                'aria-label': 'Repita seu email',
                'placeholder': 'seu@email.com',
            }
        ),
    )

    password = forms.CharField(
        error_messages={'required': 'Informe uma senha'},
        required=True,
        label='Senha',
        validators=[strong_password],
        help_text=(
            'Deve conter ao menos uma letra maiuscula,'
            'uma letra minuscula e um número. '
            'Mínimo de 8 carateres'
        ),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type': 'password',
                'aria-label': 'Informe uma senha',
                'placeholder': 'Informe uma senha',
            }
        ),
    )

    password2 = forms.CharField(
        error_messages={'required': 'Repita a senha'},
        required=True,
        label='Repita a senha',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type': 'password',
                'aria-label': 'Repita a senha',
                'placeholder': 'Repita a senha',
            }
        ),
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]


class ResetPasswordForm(forms.ModelForm):

    password = forms.CharField(
        error_messages={'required': 'Informe uma senha'},
        required=True,
        label='Senha',
        validators=[strong_password],
        help_text=(
            'Deve conter ao menos uma letra maiuscula,'
            'uma letra minuscula e um número. '
            'Mínimo de 8 carateres'
        ),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type': 'password',
                'aria-label': 'Informe a nova senha',
                'placeholder': 'Informe a nova senha',
            }
        ),
    )

    password2 = forms.CharField(
        error_messages={'required': 'Repita a senha'},
        required=True,
        label='Repita a senha',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type': 'password',
                'aria-label': 'Repita a senha',
                'placeholder': 'Repita a senha',
            }
        ),
    )

    class Meta:
        model = User
        fields = [
            'password',
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError({
                'password2': 'As senhas devem ser iguais',
            })
