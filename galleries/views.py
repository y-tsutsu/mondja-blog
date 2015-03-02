# coding: utf-8

from django.shortcuts import *
from galleries.forms import PhotoImageForm

def images(request):
    form = PhotoImageForm()

    return render(
        request,
        'galleries/images.html',
        context_instance = RequestContext(request, locals())
    )