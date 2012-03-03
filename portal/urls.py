# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'django.views.generic.simple.direct_to_template',
        {'template': 'index.html'}, name='home'),
    url(r'^layout/$', 'django.views.generic.simple.direct_to_template',
        {'template': 'guideline.html'}, name='layout'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}, name='login'),
    # url(r'^portal/', include('portal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('portal.apps.blog.urls')),
    url(r'^gallery/', include('portal.apps.gallery.urls')),
    url(r'^badges/', include('portal.apps.badges.urls')),
    url(r'^home/$', 'portal.views.home', name='home'),
)

if settings.DEBUG:
        urlpatterns += patterns('django.views.static',
                        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
                            )

