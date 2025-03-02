from django.contrib import admin
from .models import Event, Group, EventParticipant

# Register your models here.
class EventParticipantInline(admin.TabularInline):  
    model = EventParticipant  
    extra = 1  
    readonly_fields = ('user', 'status')  

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'date', 'created_by', 'accepted_count', 'pending_count', 'declined_count')
    search_fields = ('title', 'created_by__username')
    list_filter = ('event_type', 'date')
    inlines = [EventParticipantInline] 

    def accepted_count(self, obj):
        return EventParticipant.objects.filter(event=obj, status='accepted').count()
    accepted_count.short_description = "Accepted"

    def pending_count(self, obj):
        return EventParticipant.objects.filter(event=obj, status='pending').count()
    pending_count.short_description = "Pending"

    def declined_count(self, obj):
        return EventParticipant.objects.filter(event=obj, status='declined').count()
    declined_count.short_description = "Declined"

admin.site.register(Event, EventAdmin)
admin.site.register(Group)  