from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django.conf import settings

#enable admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'testassignment.person.views.index', name='index'),
    url(r'^edit/$', 'testassignment.person.views.edit', name='edit'),

    url(r'^requests/$', 'testassignment.logger.views.requests', name='requests'),
    url(r'^settings/$', 'testassignment.person.views.settings', name='settings'),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'},
        name='login'),

    url(r'^logout/$', 'testassignment.person.views.logout', name='logout'),

    #after logging in - go to edit-page
    url(r'^accounts/profile/$', redirect_to, {'url': '/edit/'}),
    url(r'^accounts/login/$', redirect_to, {'url': '/login/'}),

    url(r'^admin/', include(admin.site.urls)),

    )

#static & media data
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$',
            'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

        (r'^media/(?P<path>.*)$',
            'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
