# coding: utf-8

from datetime import datetime
from django.conf.urls import patterns, url
from django.conf.urls import include

urlpatterns = patterns('posts.views',
    url(r'^detail/(?P<id>.*)/', 'detail', name='detail'),
)
