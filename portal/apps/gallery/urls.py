from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('apps.gallery.views',
    url(r'^$', 'list_albuns', name='albuns')
)
