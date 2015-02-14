# coding: utf-8

from django.shortcuts import *
from django.http import HttpRequest
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
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

@login_required
def add_entry(request):
    entry_form = PostForm

    if request.method == 'POST':
        entry = PostForm(request.POST or None)
        if entry.is_valid():
            new_entry = entry.save(commit = False)
            new_entry.save()

            return HttpResponseRedirect('/')

    return render(
        request,
        'posts/add_entry.html',
        context_instance = RequestContext(request,
        {
            'entry_form':entry_form,
        })
    )

@login_required
def edit_entry(request, id):
    post = Post.objects.get(id = id)

    if request.method == 'POST':
        new_post = PostForm(request.POST or None, instance = post)

        if new_post.is_valid():
            newest_post = new_post.save(commit = False)
            newest_post.save()

            return HttpResponseRedirect('/posts/detail/{0}/'.format(id))

    return render(
        request,
        'posts/edit_entry.html',
        context_instance = RequestContext(request, locals())
    )

@login_required
def delete_entry(request, id):
    post = Post.objects.get(id = id)

    if request.method == 'POST':
        post.delete()

        new_post = PostForm(request.POST or None, instance = post)

        return HttpResponseRedirect('/')
