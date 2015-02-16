"""
Definition of views.
"""

# coding: utf-8

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from django .core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from posts.models import Post

def top(request):
    all_posts = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(all_posts, 5)
    page = request.GET.get('page')

    try:
        all_posts = paginator.page(page)
    except PageNotAnInteger:
        all_posts = paginator.page(1)
    except EmptyPage:
        all_posts = paginator.page(paginator.num_pages)

    return render(
        request,
        'top.html',
        context_instance = RequestContext(request,
        {
            'all_posts':all_posts,
        })
    )

def about(request):
    """Renders the about page."""
    return render(
        request,
        'about.html',
        context_instance = RequestContext(request,
        {
        })
    )
