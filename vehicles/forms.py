# -*- coding: utf-8 -*-

from choices import *
from django import forms
from models import Vehicle

class VehicleForm(forms.ModelForm):
    type_vehicle = forms.ChoiceField(
        label=u'Categoría :', choices=VEHICLES,
        help_text='Seleccione la categoría de su automotor.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Ingrese un opción válida.',
        }
    )
    mark = forms.CharField(
        label=u'Marca : ', max_length=30,
        help_text='Ingrese la marca de su automotor.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid': u'Ingrese un valor válido.',
            'max_length': u'Este campo recibe como máximo 30 caracteres.'
        }
    )
    model = forms.CharField(
        label=u'Modelo : ', max_length=30,
        help_text='Ingrese el modelo de su automotor.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid': u'Ingrese un valor válido.',
            'max_length': u'Este campo recibe como máximo 30 caracteres.'
        }
    )
    year = forms.IntegerField(
        label=u'Año : ', min_value=1940, max_value=2013,
        help_text=u'Ingrese el año de su automotor.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid': u'Ingrese un año válido (solo números).',
            'max_value': u'Ingrese un año menor ó igual que 2013.',
            'min_value': u'Ingrese un año mayor ó igual que 1940.'
        }
    )
    description = forms.CharField(
        label=u'Descripción : ', widget=forms.Textarea,
        help_text='Ingrese una descripcion ó información extra de su automotor.',
        error_messages={
            'invalid': u'Ingrese un comentario válido.',
            'required': u'Este campo es obligatorio.'
        }
    )
    location = forms.ChoiceField(
        label=u'Categoría :', choices=LOCATIONS,
        help_text='Seleccione la localidad de su automotor.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Ingrese un opción válida.',
        }
    )
    price = forms.IntegerField(
        label=u'Precio : ', min_value=1, max_value=1000000,
        help_text=u'Ingrese el precio de su automotor.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid': u'Ingrese un año válido (solo números).',
            'max_value': u'Ingrese un valor menor ó igual que 1000000.',
            'min_value': u'Ingrese un valor mayor ó igual que 1.'
        }
    )
    contact = forms.CharField(
        label=u'Contacto : ', max_length=30,
        help_text='Ingrese su teléfono de contacto.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid': u'Ingrese un valor válido.',
            'max_length': u'Este campo recibe como máximo 30 caracteres.'
        }
    )


    class Meta:
        model = Vehicle
        exclude = ('user', 'image2', 'image3', 'image4')
