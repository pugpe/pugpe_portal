from django.contrib import admin
from event_generator.models import Event, Location, EventLecture


class EventLectureInline(admin.StackedInline):
    model = EventLecture
    extra = 1


class EventAdmin(admin.ModelAdmin):
    inlines = (EventLectureInline,)


admin.site.register(Event, EventAdmin)
admin.site.register(Location)
