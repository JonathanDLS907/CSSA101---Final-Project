from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'reporter_name', 'created_at')
    list_filter = ('status',)
    search_fields = ('title', 'description')

# Register your models here.
