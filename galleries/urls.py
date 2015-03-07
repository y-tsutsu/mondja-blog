# coding: utf-8

from django.conf.urls import patterns, url
from django.conf.urls import include

urlpatterns = patterns('galleries.views',
    url(r'^$', 'images', name = 'images'),
    url(r'^add/$', 'add_image', name = 'add_image'),
    url(r'^delete/(?P<id>.*)/$', 'delete_image', name = 'delete_image'),
)
