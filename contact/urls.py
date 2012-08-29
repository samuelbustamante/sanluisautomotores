# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url, include
from django.views.generic.simple import direct_to_template
from views import create_message

urlpatterns = patterns('',
    url(r'^contactenos/$', create_message, name='contact_us'),
    url(r'^mensaje-enviado/$', direct_to_template, {'template': 'contact/success.html'}),
)
