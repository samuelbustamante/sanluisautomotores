# -*- coding: utf-8 -*-

from django import forms
from models import Message

class MessageForm(forms.ModelForm):

    full_name = forms.CharField(
        label=u'Nombre : ',
        max_length=100,
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid': u'Ingrese un valor válido.',
            'max_length': u'Este campo recibe como máximo 100 caracteres.'
        }
    )
    email = forms.EmailField(
        label='Email : ',
        error_messages={
            'required': u'Este campo en obligatorio.',
            'invalid': u'Email inválido.'
        }
    )

    phone = forms.CharField(
        label=u'Telefono : ',
        max_length=20,
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid': u'Ingrese un valor válido.',
            'max_length': u'Este campo recibe como máximo 30 caracteres.'
        }
    )

    message = forms.CharField(
        label=u'Mensaje : ',
        widget=forms.Textarea,
        error_messages={
            'invalid': u'Ingrese un comentario válido.'
        }
    )

    offer = forms.BooleanField(required=False,
        label=u'Acepto recibir ofertas',
        initial=True,
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Seleccione una opción válida.'
        }
    )

    class Meta:
        model = Message
