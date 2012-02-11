from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django.conf import settings
import os.path

#enable admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'testassignment.views.index', name='index'),
    url(r'^edit/$', 'testassignment.views.editmodel', name='edit'),
    url(r'^editform/$', 'testassignment.views.editform', name='editform'),
    url(r'^editmodel/$', 'testassignment.views.editmodel', name='editmodel'),

    url(r'^requests/$', 'testassignment.views.requests', name='requests'),
    url(r'^settings/$', 'testassignment.views.settings', name='settings'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'testassignment.views.logout', name='logout'),
    url(r'^accounts/profile/$', redirect_to, {'url': '/edit/'}), #after logging go to edit-page
    url(r'^accounts/login/$', redirect_to, {'url': '/login/'}),

    url(r'^js/([\w\.\-]+)/([\w\.\-]+)/$', 'testassignment.views.javascript', name='javascript'),



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
