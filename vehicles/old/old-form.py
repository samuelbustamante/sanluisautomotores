# -*- coding: utf-8 -*-

from django import forms
from models import Mark, Upholstery, Roof, Direction, Transmission,\
                   Used, Doors, Fuel, Car, EquipmentVehicle, Vehicle
from myproject.choices.models import Location, Year, Currency

class CarForm(forms.ModelForm):

    title = forms.CharField(
        label=u'Título : ', max_length=50,
        help_text='Ingrese el título con el que se publicará el anuncio de tu automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid': u'Ingrese un valor válido.',
            'max_length': u'Este campo recibe como máximo 30 caracteres.'
        }
    )

    mark = forms.ModelChoiceField(
        label=u'Marca :',
        queryset=Mark.objects.filter(vehicle__str_type='car').all(),
        help_text='Seleccione la marca de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Ingrese un opción válida.',
        }
    )

    model = forms.CharField(
        label=u'Modelo : ', max_length=30,
        help_text='Ingrese el modelo de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid': u'Ingrese un valor válido.',
            'max_length': u'Este campo recibe como máximo 30 caracteres.'
        }
    )

    version = forms.CharField(
        label=u'Version : ', max_length=30,
        help_text='Ingrese la versión del modelo de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid': u'Ingrese un valor válido.',
            'max_length': u'Este campo recibe como máximo 30 caracteres.'
        }
    )

    year = forms.ModelChoiceField(
        label=u'Año : ',
        queryset=Year.objects.all(),
        help_text=u'Seleccione el año de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Seleccione una opción válida.'
        }
    )

    # Hacer una validación del color que solo sean letras y números.
    color = forms.CharField(
        label=u'Color : ', max_length=6,
        help_text='Ingrese el color de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid': u'Ingrese un valor válido.',
            'max_length': u'Este campo recibe como máximo 6 caracteres.'
        }
    )

    upholstery = forms.ModelChoiceField(
        label=u'Tapizado : ',
        queryset=Upholstery.objects.filter(vehicle__str_type='car').all(),
        help_text=u'Seleccione el tipo de tapizado de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Seleccione una opción válida.'
        }
    )

    roof = forms.ModelChoiceField(
        label=u'Techo : ',
        queryset=Roof.objects.filter(vehicle__str_type='car').all(),
        help_text=u'Seleccione el tipo de techo de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Seleccione una opción válida.'
        }
    )

    direction = forms.ModelChoiceField(
        label=u'Dirección : ',
        queryset=Direction.objects.filter(vehicle__str_type='car').all(),
        help_text=u'Seleccione el tipo de dirección de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Seleccione una opción válida.'
        }
    )

    transmission = forms.ModelChoiceField(
        label=u'Transmisión : ',
        queryset=Transmission.objects.filter(vehicle__str_type='car').all(),
        help_text=u'Seleccione el tipo de transmisión de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Seleccione una opción válida.'
        }
    )

    doors = forms.ModelChoiceField(
        label=u'Nº de puertas : ',
        queryset=Doors.objects.filter(vehicle__str_type='car').all(),
        help_text=u'Seleccione el número de puertas de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Seleccione una opción válida.'
        }
    )

    fuel = forms.ModelChoiceField(
        label=u'Combustible : ',
        queryset=Fuel.objects.filter(vehicle__str_type='car').all(),
        help_text=u'Seleccione el tipo de combustible que usa su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Seleccione una opción válida.'
        }
    )

    used = forms.ModelChoiceField(
        label=u'Uso : ',
        queryset=Used.objects.filter(vehicle__str_type='car').all(),
        help_text=u'Seleccione la cantidad de Km. recorridos por su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Seleccione una opción válida.'
        }
    )

    location = forms.ModelChoiceField(
        label=u'Ubicación : ',
        queryset=Location.objects.all(),
        help_text=u'Seleccione la ubicación de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Seleccione una opción válida.'
        }
    )

    price = forms.IntegerField(
        label=u'Precio : ', min_value=1, max_value=999999,
        help_text=u'Ingrese el precio de venta de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid': u'Ingrese un valor válido (solo números).',
            'max_value': u'Ingrese un precio mayor a 1.',
            'min_value': u'Ingrese un precio menor a 1.000.000.'
        }
    )

    currency = forms.ModelChoiceField(
        label=u'Moneda : ',
        queryset=Currency.objects.all(),
        help_text=u'Seleccione el tipo de moneda de venta de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Seleccione una opción válida.'
        }
    )

    description = forms.CharField(required=False,
        label=u'Descripción : ', widget=forms.Textarea,
        help_text='Si desea puede ingresar descripcion ó información extra de su automovil.',
        error_messages={
            'invalid': u'Ingrese un comentario válido.'
        }
    )

    equipment = forms.ModelMultipleChoiceField(
        label=u'Equipamiento : ',
        queryset=EquipmentVehicle.objects.all(),
        help_text=u'Seleccione el equipamiento que posee su automovil (mantega presionado Ctrl para seleccionar).',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Seleccione una opción válida.'
        }
    )

    class Meta:
        model = Car
        exclude = ('gallery',)

class MotorcycleForm(forms.ModelForm):

    title = forms.CharField(
        label=u'Título : ', max_length=50,
        help_text='Ingrese el título con el que se publicará el anuncio de tu automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid': u'Ingrese un valor válido.',
            'max_length': u'Este campo recibe como máximo 30 caracteres.'
        }
    )

    mark = forms.ModelChoiceField(
        label=u'Marca :',
        queryset=Mark.objects.filter(vehicle__str_type='motorcycle').all(),
        help_text='Seleccione la marca de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Ingrese un opción válida.',
        }
    )

    model = forms.CharField(
        label=u'Modelo : ', max_length=30,
        help_text='Ingrese el modelo de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid': u'Ingrese un valor válido.',
            'max_length': u'Este campo recibe como máximo 30 caracteres.'
        }
    )

    version = forms.CharField(
        label=u'Version : ', max_length=30,
        help_text='Ingrese la versión del modelo de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid': u'Ingrese un valor válido.',
            'max_length': u'Este campo recibe como máximo 30 caracteres.'
        }
    )

    year = forms.ModelChoiceField(
        label=u'Año : ',
        queryset=Year.objects.all(),
        help_text=u'Seleccione el año de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Seleccione una opción válida.'
        }
    )

    # Hacer una validación del color que solo sean letras y números.
    color = forms.CharField(
        label=u'Color : ', max_length=6,
        help_text='Ingrese el color de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid': u'Ingrese un valor válido.',
            'max_length': u'Este campo recibe como máximo 6 caracteres.'
        }
    )

    upholstery = forms.ModelChoiceField(
        label=u'Tapizado : ',
        queryset=Upholstery.objects.filter(vehicle__str_type='motorcycle').all(),
        help_text=u'Seleccione el tipo de tapizado de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Seleccione una opción válida.'
        }
    )

    direction = forms.ModelChoiceField(
        label=u'Dirección : ',
        queryset=Direction.objects.filter(vehicle__str_type='motorcycle').all(),
        help_text=u'Seleccione el tipo de dirección de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Seleccione una opción válida.'
        }
    )

    transmission = forms.ModelChoiceField(
        label=u'Transmisión : ',
        queryset=Transmission.objects.filter(vehicle__str_type='motorcycle').all(),
        help_text=u'Seleccione el tipo de transmisión de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Seleccione una opción válida.'
        }
    )

    fuel = forms.ModelChoiceField(
        label=u'Combustible : ',
        queryset=Fuel.objects.filter(vehicle__str_type='motorcycle').all(),
        help_text=u'Seleccione el tipo de combustible que usa su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Seleccione una opción válida.'
        }
    )

    used = forms.ModelChoiceField(
        label=u'Uso : ',
        queryset=Used.objects.filter(vehicle__str_type='motorcycle').all(),
        help_text=u'Seleccione la cantidad de Km. recorridos por su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Seleccione una opción válida.'
        }
    )

    location = forms.ModelChoiceField(
        label=u'Ubicación : ',
        queryset=Location.objects.all(),
        help_text=u'Seleccione la ubicación de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Seleccione una opción válida.'
        }
    )

    price = forms.IntegerField(
        label=u'Precio : ', min_value=1, max_value=999999,
        help_text=u'Ingrese el precio de venta de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid': u'Ingrese un valor válido (solo números).',
            'max_value': u'Ingrese un precio mayor a 1.',
            'min_value': u'Ingrese un precio menor a 1.000.000.'
        }
    )

    currency = forms.ModelChoiceField(
        label=u'Moneda : ',
        queryset=Currency.objects.all(),
        help_text=u'Seleccione el tipo de moneda de venta de su automovil.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Seleccione una opción válida.'
        }
    )

    description = forms.CharField(required=False,
        label=u'Descripción : ', widget=forms.Textarea,
        help_text='Si desea puede ingresar descripcion ó información extra de su automovil.',
        error_messages={
            'invalid': u'Ingrese un comentario válido.'
        }
    )

    equipment = forms.ModelMultipleChoiceField(
        label=u'Equipamiento : ',
        queryset=EquipmentVehicle.objects.filter(vehicle__str_type='motorcycle').all(),
        help_text=u'Seleccione el equipamiento que posee su automovil (mantega presionado Ctrl para seleccionar).',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid_choice': u'Seleccione una opción válida.'
        }
    )

    class Meta:
        model = Vehicle
        exclude = ('gallery', 'vehicle')
