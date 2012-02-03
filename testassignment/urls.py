from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
import os.path

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'testassignment.views.home', name='home'),
    url(r'^requests/$', 'testassignment.views.requests', name='requests'),
    # url(r'^testassignment/', include('testassignment.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
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
