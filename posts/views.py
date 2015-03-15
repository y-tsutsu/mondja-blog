# coding: utf-8

from django.shortcuts import *
from django.http import HttpRequest
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime
from posts.models import Post, Comment
from posts.forms import PostForm, CommentForm

def detail(request, id):
    post = Post.objects.get(id = id)
    comments = Comment.objects.filter(post = post).order_by('pub_date')

    find = False
    new_post = None
    old_post = None
    for p in Post.objects.all().order_by('-pub_date'):
        if find:
            old_post = p
            break

        if p.id == post.id:
            find = True

        if not find: new_post = p

    return render(
        request,
        'posts/detail.html',
        context_instance = RequestContext(request, locals())
    )

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
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

@user_passes_test(lambda u: u.is_superuser)
def delete_entry(request, id):
    post = Post.objects.get(id = id)

    if request.method == 'POST':
        post.delete()

        new_post = PostForm(request.POST or None, instance = post)

        return HttpResponseRedirect('/')

@user_passes_test(lambda u: u.is_superuser)
def comment_entry(request, id):
    if request.method == 'POST':
        post = Post.objects.get(id = id)
        new_comment = CommentForm(request.POST or None)

        if new_comment.is_valid():
            new_comment = new_comment.save(commit = False)
            new_comment.save()

    return HttpResponseRedirect('/posts/detail/{0}/'.format(id))
