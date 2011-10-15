from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('portal.apps.blog.views',
    url(r'^$', 'posts', name='posts'),
    url(r'^(?P<slug>[\w_-]+)/$', 'post', name='post'),
)
