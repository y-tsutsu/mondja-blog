﻿"""
Definition of urls for mondja.
"""

# coding: utf-8

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Top:
    url(r'^$', 'app.views.top', name = 'top'),

    # Posts
    url(r'^posts/', include('posts.urls')),

    # About
    url(r'^about/', 'app.views.about', name = 'about'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'login.html',
        },
        name = 'login'),
    url(r'^logout/$',
        'django.contrib.auth.views.logout',
        {
            'template_name': 'logout.html',
        },
        name = 'logout'),
)