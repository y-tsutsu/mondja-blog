# coding: utf-8

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from posts.models import Post, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        fields = "__all__" 
        model = Comment

class PostForm(forms.ModelForm):
    class Meta:
        fields = "__all__" 
        model = Post
