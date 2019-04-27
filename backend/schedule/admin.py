from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import ScheduleItem, Room


@admin.register(ScheduleItem)
class ScheduleItemAdmin(admin.ModelAdmin):
    list_display = ('conference', 'start', 'end', 'type', 'title', 'submission')
    ordering = ('conference', 'start',)
    fieldsets = (
        (_('Event'), {
            'fields': ('conference', 'type', 'title', 'description', 'submission')
        }),
        (_('Schedule'), {
            'fields': ('start', 'end', 'rooms')
        }),
    )
    autocomplete_fields = ('submission',)
    filter_horizontal = ('rooms',)
    search_fields = ('type', 'title',)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'conference')
    list_filter = ('conference',)
