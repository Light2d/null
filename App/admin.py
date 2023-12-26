from django.contrib import admin
from .models import Direction, Event, Participant

@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator')
    search_fields = ('title', 'creatorfull__name', 'creator__email')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'direction')
    search_fields = ('title', 'direction__title')

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('event', 'participant')
    search_fields = ('event__title', 'participant__full_name', 'participant__email')
