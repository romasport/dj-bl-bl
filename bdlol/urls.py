from django.conf.urls import patterns, include, url
from django.contrib import admin
from robots_txt.views import RobotsTextView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bdlol.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', include('news.urls')),
    url(r'^auth/', include('accounts.urls')),
    url(r'^users/', include('users.urls', 'users')),

    url(r'^captcha/', include('captcha.urls')),

    url(r'^robots.txt$', RobotsTextView.as_view()),

    url(r'^', include('perl.urls')),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()