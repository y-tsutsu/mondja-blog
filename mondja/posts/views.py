# coding: utf-8

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from posts.models import Post
from posts.forms import PostForm

def detail(request, id):
    post = Post.objects.get(id = id)
    return render(
        request,
        'posts/detail.html',
        context_instance = RequestContext(request,
        {
            'post':post,
        })
    )

def add_entry(request):
    entry_form = PostForm
    return render(
        request,
        'posts/add_entry.html',
        context_instance = RequestContext(request,
        {
            'entry_form':entry_form,
        })
    )
