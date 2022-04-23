from django import forms


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields.get('username').widget.attrs['class'] = 'form-control'
        self.fields.get('username').widget.attrs['id'] = 'username'
        self.fields.get(
            'username').widget.attrs['placeholder'] = 'Digite seu usuário'
        self.fields.get(
            'username').widget.attrs['aria-label'] = 'Digite seu usuário'

        self.fields.get('password').widget.attrs['class'] = 'form-control'
        self.fields.get('password').widget.attrs['id'] = 'password'
        self.fields.get(
            'password').widget.attrs['placeholder'] = 'Digite sua senha'
        self.fields.get(
            'password').widget.attrs['aria-label'] = 'Digite sua senha'

    username = forms.CharField(max_length=150)
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
