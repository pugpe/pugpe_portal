from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.badges.views',
    url(r'^$', 'list_badges', name='badges'),
)
