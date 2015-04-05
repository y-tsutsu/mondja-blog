﻿# coding: utf-8

from django.shortcuts import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import models as usermodels
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist
from memo.models import Memo, Tag
from memo.forms import MemoForm, TagForm
from mondja.pydenticon_wrapper import create_identicon

def memo(request):
    types = request.GET.get('types')

    if types == 'sort':
        sort_item = request.GET.get('sort_item')
        if sort_item is not '' and request.GET.get('sort_op') == 'desc':
            sort_item = '-' + sort_item
        
        sort_tag_id = request.GET.get('sort_tag_id')
        all_memo = Memo.objects.all() if sort_tag_id is '' else Tag.objects.get(id = sort_tag_id).memo_set.all()

        sort_user_id = request.GET.get('sort_user_id')
        if sort_user_id is not '':
            all_memo = all_memo.filter(user = usermodels.User.objects.get(id = sort_user_id))

        if sort_item is '':
            all_memo = all_memo.order_by('-pub_date')
        else:
            all_memo = all_memo.order_by(sort_item)

    elif types == 'search':
        search_title = request.GET.get('search_title')
        search_content = request.GET.get('search_content')
        search_tag = request.GET.get('search_tag')
        search_user = request.GET.get('search_user')

        if search_tag is '':
            all_memo = Memo.objects.all()
        else:
            try:
                all_memo = Tag.objects.get(name = search_tag).memo_set.all()
            except ObjectDoesNotExist:
                all_memo = Memo.objects.filter(title = '')

        if search_user is not '':
            try:
                user = usermodels.User.objects.get(username = search_user)
                all_memo = all_memo.filter(user = user)
            except ObjectDoesNotExist:
                all_memo = Memo.objects.filter(title = '')

        if search_title is not '' and search_content is not '':
            all_memo = all_memo.filter(title__icontains = search_title, content__icontains = search_content)
        elif search_title is not '':
            all_memo = all_memo.filter(title__icontains = search_title)
        elif search_content is not '':
            all_memo = all_memo.filter(content__icontains = search_content)
        else:
            pass

        all_memo = all_memo.order_by('-pub_date')

    elif types == 'tags':
        memos = []
        for tid in request.GET.getlist('select_tag'):
            tag = Tag.objects.get(id = tid)
            for memo in tag.memo_set.all():
                memos.append(memo)
        all_memo = sorted(set(memos), key = lambda x: x.pub_date)
        all_memo.reverse()

    else:
         all_memo = Memo.objects.all().order_by('-pub_date')

    all_memo = all_memo[:100]

    for item in all_memo:
        create_identicon(item.user.username)

    all_tags = Tag.objects.annotate(count_memos = Count('memo')).order_by('-count_memos', '-pub_date')
    all_users = usermodels.User.objects.annotate(count_memos = Count('memo')).order_by('-count_memos')

    return render(
        request,
        'memo/memo.html',
        context_instance = RequestContext(request, locals())
    )

@user_passes_test(lambda u: u.is_superuser)
def add_memo(request):
    if request.method == 'POST':
        memo_form = MemoForm(request.POST or None)

        if memo_form.is_valid():
            new_memo = memo_form.save(commit = False)
            new_memo.save()

            tags = request.POST['tags-text']

            for stag in [s.rstrip() for s in tags.split()]:

                if len(Tag.objects.filter(name = stag)) == 0:
                    tag = Tag(name = stag, user = request.user)
                    tag_form = TagForm(instance = tag)

                    if is_valid_tag(stag):
                        new_tag = tag_form.save(commit = False)
                        new_tag.save()
                        new_memo.tags.add(new_tag)
                        new_memo.save()
                else:
                    tag = Tag.objects.get(name = stag)
                    new_memo.tags.add(tag)
                    new_memo.save()

    return HttpResponseRedirect('/memo/')

@user_passes_test(lambda u: u.is_superuser)
def edit_memo(request, id):
    memo = Memo.objects.get(id = id)

    if request.method == 'POST':
        memo_form = MemoForm(request.POST or None, instance = memo)

        if memo_form.is_valid():
            new_memo = memo_form.save(commit = False)
            new_memo.save()
            new_memo.tags.clear()
            new_memo.save()

            tags = request.POST['tags-text']

            for stag in [s.rstrip() for s in tags.split()]:
                
                if len(Tag.objects.filter(name = stag)) == 0:
                    tag = Tag(name = stag, user = request.user)
                    tag_form = TagForm(instance = tag)

                    if is_valid_tag(stag):
                        new_tag = tag_form.save(commit = False)
                        new_tag.save()
                        new_memo.tags.add(new_tag)
                        new_memo.save()
                else:
                    tag = Tag.objects.get(name = stag)
                    new_memo.tags.add(tag)
                    new_memo.save()

            clear_notused_tag()

    return HttpResponseRedirect('/memo/')

@user_passes_test(lambda u: u.is_superuser)
def delete_memo(request, id):
    memo = Memo.objects.get(id = id)

    if request.method == 'POST':
        memo.delete()

        clear_notused_tag()

    return HttpResponseRedirect('/memo/')

def is_valid_tag(tag):
    ''' tagの文字長チェック '''
    return len(tag) <= 10

def clear_notused_tag():
    ''' 不要なtagを削除 '''
    for tag in Tag.objects.all():
        if len(tag.memo_set.all()) == 0:
            tag.delete()
