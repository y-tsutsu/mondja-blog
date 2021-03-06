﻿# coding: utf-8

from datetime import datetime
from django.conf.urls import patterns, url
from django.conf.urls import include

urlpatterns = patterns('posts.views',
    url(r'^detail/(?P<id>.*)/', 'detail', name = 'detail'),
    url(r'^entry/', 'add_entry', name = 'add_entry'),
    url(r'^edit/(?P<id>.*)/$', 'edit_entry', name = 'edit_entry'),
    url(r'^delete/(?P<id>.*)/$', 'delete_entry', name = 'delete_entry'),
    url(r'^comment/(?P<id>.*)/$', 'comment_entry', name = 'comment_entry'),
)
