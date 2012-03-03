from django.views.generic import DetailView
from event_generator.models import Event


class EventDetailView(DetailView):
    model = Event
    context_object_name = u'event'
