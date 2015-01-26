# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from . import forms

urlpatterns = patterns('django.contrib.auth.views',
    #url('^login/$', 'login', {'template_name': 'users/login.html', 'authentication_form': forms.AuthenticationForm}, 'login'),
)

urlpatterns += patterns('users.views',

    url(r'^login/$', 'login'),
    url(r'^logout/$', 'logout'),
    url(r'^registr/$', 'registr'),
    url(r'^(.+)/$', 'profile'),

)