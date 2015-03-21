# coding: utf-8

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from memo.models import Memo, Tag

class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
