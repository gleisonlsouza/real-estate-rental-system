import re

from django.core.exceptions import ValidationError


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'Deve conter ao menos uma letra maiuscula,'
            'uma letra minuscula e um número. '
            'Mínimo de 8 carateres.'
        ),
            code='invalid'
        )


def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr}{attr_new_val}'.strip()


def add_placeholder(field, place_holder_val):
    field.widget.attrs['placeholder'] = place_holder_val
