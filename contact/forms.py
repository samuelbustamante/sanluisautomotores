# -*- coding: utf-8 -*-

from django import forms
from models import Message

class MessageForm(forms.ModelForm):

    full_name = forms.CharField(
        label=u'Nombre : ', max_length=100,
        help_text=u'Por favor ingrese su nombre.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid': u'Ingrese un valor válido.',
            'max_length': u'Este campo recibe como máximo 100 caracteres.'
        }
    )
    email = forms.EmailField(
        label='Dirección de email : ',
        help_text=u'Por favor ingrese su dirección de email, será usado para ponernos en contacto con usted.',
        error_messages={
            'required': u'Este campo en obligatorio.',
            'invalid': u'Email inválido.'
        }
    )
    message = forms.CharField(
        label=u'Mensaje : ',
        help_text=u'Por favor ingrese su comentario, sugerencia o duda.',
        widget=forms.Textarea,
        error_messages={
            'invalid': u'Ingrese un comentario válido.'
        }
    )

    class Meta:
        model = Message
