# -*- coding: utf-8 -*-

from models import Vehicle
from forms import VehicleForm
from views import create_vehicle, show_vehicle, list_vehicle
from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('',

    url(r'^/publicar/auto/gratis/$', create_vehicle,
        {'template_name': 'vehicles/create_vehicle.html',
        'Form': CarForm,
        'TypeAd' : TypeAd.objects.get(name='gratis')},
        name='create_free_car'
    ),

    url(r'^/publicar/auto/destacado/$', create_vehicle,
        {'template_name': 'vehicles/create_vehicle.html',
        'Form': CarForm,
        'TypeAd' : TypeAd.objects.get(name='silver')},
        name='create_silver_car'
    ),

    url(r'^/publicar/auto/premium/$', create_vehicle,
        {'template_name': 'vehicles/create_vehicle.html',
        'Form': CarForm,
        'TypeAd' : TypeAd.objects.get(name='gold')},
        name='create_gold_car'
    ),

    url(r'^/ver/automovil/(?P<id>\d+)/([-\w]+)/([-\w]+)/$', show_vehicle,
        {'template_name': 'vehicles/show_vehicle.html',
        'Model': Car},
        name='show_vehicle'
    ),

    url(r'^/ver/autos/$', list_vehicle,
        {'template': 'vehicles/list_vehicle.html',
        'queryset': Car.objects.all(),
        'page': 1},
        name='list_vehicle'
    ),

    url(r'^/publicar/moto/gratis/$', create_vehicle,
        {'template_name': 'vehicles/create_vehicle.html',
        'Form': MotorcycleForm,
        'TypeAd' : TypeAd.objects.get(name='gratis')},
        name='create_free_motorcycle'
    ),

    url(r'^/publicar/moto/destacado/$', create_vehicle,
        {'template_name': 'vehicles/create_vehicle.html',
        'Form': MotorcycleForm,
        'TypeAd' : TypeAd.objects.get(name='silver')},
        name='create_silver_motorcycle'
    ),

    url(r'^/publicar/moto/premium/$', create_vehicle,
        {'template_name': 'vehicles/create_vehicle.html',
        'Form': MotorcycleForm,
        'TypeAd' : TypeAd.objects.get(name='gold')},
        name='create_gold_motorcycle'
    ),

)
