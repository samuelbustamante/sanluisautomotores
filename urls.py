# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url, include
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('myproject.vehicles.urls')),
    url(r'^', include('myproject.contact.urls')),
    url(r'^', include('myproject.registration.urls')),
    url(r'^administrador/', include(admin.site.urls)),
    url(r'^terminos_y_condiciones/$', direct_to_template, {'template': 'statics/terms.html'}, name='terms'),
    url(r'^politicas_de_privacidad/$', direct_to_template,{'template': 'statics/policies.html'}, name='policies'),
    url(r'^sobre_nosotros/$', direct_to_template, {'template': 'statics/about_us.html'}, name='about_us'),

)
