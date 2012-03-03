from django.views.generic import DetailView, ListView
from event_generator.models import Event


class EventListView(ListView):
    model = Event
    context_object_name = u'events'


class EventDetailView(DetailView):
    model = Event
    context_object_name = u'event'
