from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'news.views.all'),
    url(r'^(.+)/$', 'news.views.one'),
)
