# coding: utf-8

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from galleries.models import PhotoImage

class PhotoImageForm(forms.ModelForm):
    class Meta:
        fields = "__all__" 
        model = PhotoImage
