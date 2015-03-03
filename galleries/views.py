# coding: utf-8

from django.shortcuts import *
from galleries.forms import PhotoImageForm
from galleries.models import PhotoImage

def images(request):
    form = PhotoImageForm()

    all_images = PhotoImage.objects.all()

    if request.method == 'POST':
        image_form = PhotoImageForm(request.POST or None, request.FILES or None)

        if image_form.is_valid():
            new_image_form = image_form.save(commit = False)
            new_image_form.save()

    return render(
        request,
        'galleries/images.html',
        context_instance = RequestContext(request, locals())
    )