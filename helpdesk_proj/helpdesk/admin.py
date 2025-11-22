from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'reporter_name', 'created_at')
    list_filter = ('status',)
    search_fields = ('title', 'description', 'reporter_name', 'reporter_email')
    list_editable = ('status',)   # allows changing status directly in list view