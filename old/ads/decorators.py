# -*- conding: utf-8 -*-

from myproject.cash.models import Cash
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import TypeAd

def enough_cash(function):
    def wrapper(request, TypeAd, *args, **kwargs):
        user = request.user.get_profile()
        cash = user.cash
        if cash.cash >= TypeAd.price:
            return function(request, TypeAd, *args, **kwargs)
        else:
            return render_to_response('ads/required.html',\
                   context_instance=RequestContext(request))
    return wrapper
