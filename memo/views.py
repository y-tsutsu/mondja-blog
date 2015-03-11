# coding: utf-8

from django.shortcuts import *
from django.contrib.auth.decorators import login_required, user_passes_test

def memo(request):
    return render(
        request,
        'memo/memo.html',
        context_instance = RequestContext(request, locals())
    )
