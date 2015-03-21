# coding: utf-8

from django.conf.urls import patterns, url
from django.conf.urls import include

urlpatterns = patterns('memo.views',
    url(r'^$', 'memo', name = 'memo'),
    url(r'^add/$', 'add_memo', name = 'add_memo'),
)
