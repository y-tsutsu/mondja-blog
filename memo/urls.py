# coding: utf-8

from django.conf.urls import patterns, url
from django.conf.urls import include

urlpatterns = patterns('memo.views',
    url(r'^$', 'memo', name = 'memo'),
    url(r'^add/$', 'add_memo', name = 'add_memo'),
    url(r'^edit/(?P<id>.*)/$', 'edit_memo', name = 'edit_memo'),
    url(r'^delete/(?P<id>.*)/$', 'delete_memo', name = 'delete_memo'),
)
