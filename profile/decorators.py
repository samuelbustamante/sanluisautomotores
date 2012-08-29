# -*- conding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Profile

def not_authenticated_required(function):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return function(request, *args, **kwargs)
        else:
            return render_to_response('profile/required.html',\
                   context_instance=RequestContext(request))
    return wrapper

def common_user_required(function): 
    def wrapper(request, *args, **kwargs):
        profile = request.user.get_profile()
        if profile.is_common_user():
            return function(request, *args, **kwargs)         
        else:                
            return render_to_response('profile/required.html',\
                   context_instance=RequestContext(request))
    return wrapper

def company_user_required(function):
    def wrapper(request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        if profile.is_company_user():
            return function(request, *args, **kwargs)
        else:
            return render_to_response('profile/required.html',\
                   context_instance=RequestContext(request))
    return wrapper
