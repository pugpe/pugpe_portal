from django.conf.urls.defaults import patterns, include, url
from event_generator.views import EventDetailView, EventListView

urlpatterns = patterns('apps.gallery.views',
    url(r'^$', EventListView.as_view(), name='events'),
    url(r'^(?P<slug>[-\w]+)/$', EventDetailView.as_view(), name='event'),
)
