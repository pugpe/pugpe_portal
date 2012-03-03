from django.conf.urls.defaults import patterns, include, url
from event_generator.views import EventDetailView

urlpatterns = patterns('apps.gallery.views',
    #url(r'^$', 'list_events', name='albuns'),
    url(r'^(?P<slug>[-\w]+)/$', EventDetailView.as_view(), name='event'),
)
