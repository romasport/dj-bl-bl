from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',

  #  url(r'^login/$', 'accounts.views.login'),
    url(r'^logout/$', 'accounts.views.logout'),
    url(r'^registr/$', 'accounts.views.registr')

)