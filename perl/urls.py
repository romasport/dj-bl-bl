from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',

    url(r'^$', 'perl.views.perls'),
    url(r'^perl/plus/$', 'perl.views.plus'),
    url(r'^perl/minus/$', 'perl.views.minus'),
    url(r'^perl/comment_minus/$', 'perl.views.comment_minus'),
    url(r'^perl/comment_plus/$', 'perl.views.comment_plus'),
    url(r'^addcomment/(.+)/$', 'perl.views.addcomment'),
    url(r'^(.+)/$', 'perl.views.perl')

)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
