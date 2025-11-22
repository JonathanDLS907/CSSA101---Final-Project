from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id','title','status','priority','reporter_name','created_at','due_at')
    list_filter = ('status','priority')
    search_fields = ('title','description','reporter_name','reporter_email')
    readonly_fields = ('due_at',)   # computed
    list_editable = ('status','priority')   # optional inline edit
