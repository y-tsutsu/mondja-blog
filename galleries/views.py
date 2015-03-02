# coding: utf-8

from django.shortcuts import *

def images(request):
    return render(
        request,
        'galleries/images.html',
        context_instance = RequestContext(request, locals())
    )