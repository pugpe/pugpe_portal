from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portal.views.home', name='home'),
    # url(r'^portal/', include('portal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^gallery/', include('portal.apps.gallery.urls')),
)


if settings.DEBUG:
        urlpatterns += patterns('django.views.static',
                        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
                            )

