# coding: utf-8

from django.shortcuts import *
from django.contrib.auth.decorators import login_required, user_passes_test
from galleries.forms import PhotoImageForm
from galleries.models import PhotoImage

def images(request):
    all_images = PhotoImage.objects.all().order_by('pub_date')

    return render(
        request,
        'galleries/images.html',
        context_instance = RequestContext(request, locals())
    )

@user_passes_test(lambda u: u.is_superuser)
def add_image(request):
    if request.method == 'POST':
        image_form = PhotoImageForm(request.POST or None, request.FILES or None)

        if image_form.is_valid():
            new_image = image_form.save(commit = False)
            new_image.save()

    return HttpResponseRedirect('/galleries/')

@user_passes_test(lambda u: u.is_superuser)
def delete_image(request, id):
    image = PhotoImage.objects.get(id = id)

    if request.method == 'POST':
        image.delete()

    return HttpResponseRedirect('/galleries/')
