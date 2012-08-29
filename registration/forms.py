# -*- coding: utf-8 -*-

import time
import datetime
from django import forms
from myproject.profile.models import Profile
from django.template.loader import render_to_string
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

regex_username = r'^[a-z]{1}[\w_]+[a-z]{1}$'

class LoginForm(AuthenticationForm):
    username = forms.RegexField(
        label=u'Nombre de usuario : ', regex=regex_username, max_length=30,
        help_text=u'Ingrese su nombre de usuario (requiere registración y activación de cuenta).',
        error_messages={
            'required': u'Este campo es obligatorio.',
        }
    )

    password = forms.CharField(
        label=u'Contraseña : ', widget=forms.PasswordInput,
        help_text=u'Ingrese su contraseña.',
        error_messages={
            'required': u'Este campo es obligatorio.'
        }
    )

class RegisterUserForm(forms.Form):
    username = forms.RegexField(
        label=u'Nombre de usuario : ', regex=regex_username, max_length=30,
        help_text=u'Ingrese su nombre de usuario (puede utilizar letras minúsculas, números y guiones bajos) para identificarse en SanLuisEmpleos.',
        error_messages={
            'required': u'Este campo es obligatorio.',
            'invalid': u'Valores inválidos.',
        }
    )
    email = forms.EmailField(
        label='Dirección de email : ',
        help_text=u'Ingrese una dirección válida, ya que le enviaremos un email con las instrucciones para validar su registración en SanLuisEmpleos.',
        error_messages={
            'required': u'Este campo en obligatorio.',
            'invalid': u'Email inválido.'
        }
    )
    password = forms.CharField(
        label=u'Contraseña : ', widget=forms.PasswordInput,
        help_text=u'Escribe algo que sea dificil de descifrar.',
        error_messages={
            'required': u'Este campo es obligatorio.'
        }
    )

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        error = u'Ya existe otro usuario con este nombre.'
        raise forms.ValidationError(error)

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            return self.cleaned_data['email']
        error = u'Ya existe otro usuario con esta dirección de email.'
        raise forms.ValidationError(error)

class RegisterCommonUserForm(RegisterUserForm):

    def save(self):
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            email = self.cleaned_data['email']
            profile = Profile()
            profile.create_common_user(username, email, password)
            to = u'SanLuisAutomotores <no-reply@sanluisautomotores.com>'
            subject = u'¡Activá tu cuenta en SanLuisAutomotores!'
            t_html = 'registration/email_activation_common_user.html'
            t_txt = 'registration/email_activation_common_user.txt'
            data = {'key': profile.activation_key,\
                    'email': profile.user.email,\
                    'username': profile.user.username}
            text_content = render_to_string(t_txt, data)
            html_content = render_to_string(t_html, data)
            profile.send_email(to, subject, text_content, html_content)


class RegisterCompanyUserForm(RegisterUserForm):

    def save(self):
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            email = self.cleaned_data['email']
            profile = Profile()
            profile.create_company_user(username, email, password)
            to = u'SanLuisAutomotores <no-reply@sanluisautomotores.com>'
            subject = u'¡Activá tu cuenta en SanLuisAutomotores!'
            t_html = 'registration/email_activation_company_user.html'
            t_txt = 'registration/email_activation_company_user.txt'
            data = {'key': profile.activation_key,\
                    'email': profile.user.email,\
                    'username': profile.user.username}
            text_content = render_to_string(t_txt, data)
            html_content = render_to_string(t_html, data)
            profile.send_email(to, subject, text_content, html_content)
