# -*- coding: utf-8 -*-

from myproject.profile.decorators import not_authenticated_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from myproject.profile.models import Profile
from forms import RegisterCommonUserForm, RegisterCompanyUserForm

@not_authenticated_required
def register_common_user(request, template_name):
    if request.method == 'POST':
        form = RegisterCommonUserForm(request.POST)
        if form.is_valid():
            form.save()
            successful_registration = True
    else:
        form = RegisterCommonUserForm()
    return render_to_response(template_name, locals(),\
           context_instance=RequestContext(request))

@not_authenticated_required
def register_company_user(request, template_name):
    if request.method == 'POST':
        form = RegisterCompanyUserForm(request.POST)
        if form.is_valid():
            form.save()
            successful_registration = True
    else:
        form = RegisterCompanyUserForm()
    return render_to_response(template_name, locals(),\
           context_instance=RequestContext(request))

@not_authenticated_required
def confirmation(request, activation_key, template_name):
    try:
        profile = Profile.objects.get(activation_key=activation_key)
        profile.activate()
        activate = True
    except Profile.DoesNotExist:
        activate = False
    return render_to_response(template_name, locals(),\
           context_instance=RequestContext(request))
