# coding: utf-8

from django.conf.urls import patterns, url
from django.conf.urls import include

urlpatterns = patterns('galleries.views',
    url(r'^', 'images', name = 'images'),
)
