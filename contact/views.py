# -*- coding: utf-8 -*-

from forms import MessageForm
from django.views.generic import create_update

def create_message(request):
    return create_update.create_object(
        request,
        form_class=MessageForm,
        post_save_redirect='/mensaje-enviado/',
    )
