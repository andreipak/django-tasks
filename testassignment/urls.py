from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
import os.path

#enable admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'testassignment.views.index', name='index'),
    url(r'^requests/$', 'testassignment.views.requests', name='requests'),
    url(r'^settings/$', 'testassignment.views.settings', name='settings'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {
            'document_root': \
            os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static')
        }),
    )
