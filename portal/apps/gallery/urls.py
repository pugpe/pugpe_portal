from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('apps.gallery.views',
    url(r'^$', 'list_albuns', name='albuns'),
    url(r'^album/(?P<album_slug>[-\w]+)/$', 'view_album', name='album'),
    url(r'^my/$', 'my_albuns', name='act_my_albuns'),
    url(r'^edit/(?P<slug>[-\w]+)/$', 'edit', name='act_edit'),
    url(r'^post/$', 'post_album', name='act_post_album'),

)

