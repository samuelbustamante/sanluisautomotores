# -*- coding: utf-8 -*-

from models import Vehicle
from django.views.generic import list_detail
from django.views.generic import create_update

def home(request):
    return list_detail.object_list(
        request,
        queryset=Vehicle.objects.all()[0:30],
        template_name='properties/departament_rent_list.html'
    )
































from django.contrib.auth.decorators import login_required
from myproject.gallery.models import Gallery
from myproject.gallery.forms import ImageForm, create_gallery
from myproject.contact.forms import MessageForm
from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from myproject.ads.models import TypeAd, Ad
from myproject.ads.decorators import enough_cash
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

@login_required
@enough_cash
def create_vehicle(request, TypeAd, template_name, Form):
    #-- Gallery --
    ImageFormSet = formset_factory(ImageForm, extra=TypeAd.number_images)

    if request.method == 'POST':
        form = Form(request.POST)
        image_formset = ImageFormSet(request.POST, request.FILES)
        if form.is_valid() and image_formset.is_valid():
            model = form.save(commit=False)
            user = request.user.get_profile()
            #-- Profile --#
            model.profile = user
            #---- Ad -----#
            ad = Ad(type=TypeAd)
            ad.save()
            ad.update_finished()
            model.ad = ad
            #---- Cash ----#
            user.cash.subtract_cash(TypeAd.price)
            #-- Gallery ---#
            model.gallery = create_gallery(image_formset)
            #--- Save ----#
            model.save()
            return render_to_response(template_name, locals(),\
                   context_instance=RequestContext(request))
    else:
        form = Form()
        image_formset = ImageFormSet()
    return render_to_response(template_name, locals(),\
           context_instance=RequestContext(request))

def show_vehicle(request, id, template_name, Model):
    if request.method == 'POST':
        contact_form = MessageForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            send_message = True
    else:
        contact_form = MessageForm()
    vehicle = get_object_or_404(Model, id=id)
    sponsors = range(0,6)
    return render_to_response(template_name, locals(),\
           context_instance=RequestContext(request))

def list_vehicle(request, page, template, queryset):
    sponsors = range(0,6)

    #--- Paginator ---#

    paginator = Paginator(queryset, 30)
    try:
        vehicles = paginator.page(page)
    except PageNotAnInteger:
        vehicles = paginator.page(1)
    except EmptyPage:
        vehicles = paginator.page(paginator.num_pages)

    return render_to_response(template, locals(),\
           context_instance=RequestContext(request))
