from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'reporter_name', 'reporter_email']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }
