# coding: utf-8

from django.contrib import admin
from galleries.models import PhotoImage

class PhotoImageAdmin(admin.ModelAdmin):
    list_display = ('description', 'pub_date', 'image')
    class Meta:
        model = PhotoImage

admin.site.register(PhotoImage, PhotoImageAdmin)
