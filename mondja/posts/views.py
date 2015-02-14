# coding: utf-8

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from posts.models import Post

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
