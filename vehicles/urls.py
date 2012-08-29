# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url, include
from views import *

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^publicar/$', create_vehicle, name="create_vehicle"), 
    url(r'^(?P<object_id>\d+)/([-\w]+)/$', vehicle_detail, name='vehicle_detail'),
    url(r'^(?P<type_vehicle>\d+)/ver/([-\w]+)/$', vehicle_list, name='vehicle_list'),
)
