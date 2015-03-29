# coding: utf-8

from django.shortcuts import *
from django.contrib.auth.decorators import login_required, user_passes_test
from memo.models import Memo, Tag
from memo.forms import MemoForm, TagForm
from app.pydenticon_wrapper import create_identicon

def memo(request):
    all_memo = Memo.objects.all().order_by('-pub_date')[:100]

    for item in all_memo:
        create_identicon(item.user.username)

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
    return len(tag) <= 32

def clear_notused_tag():
    ''' 不要なtagを削除 '''
    for tag in Tag.objects.all():
        if len(tag.memo_set.all()) == 0:
            tag.delete()
