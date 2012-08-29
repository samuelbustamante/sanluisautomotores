# -*- coding: utf-8 -*-

from choices import *
from models import Vehicle
from forms import VehicleForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import redirect_to
from django.views.generic import list_detail
from django.views.generic import create_update

def home(request):
    return list_detail.object_list(
        request,
        queryset=Vehicle.objects.all()[:20],
        template_name='vehicles/home.html',
        extra_context={'vehicles': VEHICLES}
    )

@login_required(redirect_field_name='')
def create_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            model = form.save(commit=False)
            model.user = request.user
            model.save()
            return render_to_response('vehicles/success.html', locals(),\
                context_instance=RequestContext(request))
    else:
        form = VehicleForm()
    return render_to_response('vehicles/vehicle_form.html', locals(),\
        context_instance=RequestContext(request))

def vehicle_detail(request, object_id):
    return list_detail.object_detail(
        request,
        object_id=object_id,
        queryset=Vehicle.objects.all()
    )

def vehicle_list(request, type_vehicle):
    queryset = Vehicle.objects.filter(type_vehicle=type_vehicle)
    return list_detail.object_list(
        request,
        queryset=queryset,
        paginate_by=15,
        page=request.GET.get('pagina')
    )
