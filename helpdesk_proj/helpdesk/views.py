from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Ticket
from .forms import TicketForm

class TicketListView(ListView):
    model = Ticket
    template_name = 'helpdesk/ticket_list.html'
    context_object_name = 'tickets'
    queryset = Ticket.objects.order_by('-created_at')  # newest first

class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'helpdesk/ticket_detail.html'
    context_object_name = 'ticket'

class TicketCreateView(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'helpdesk/ticket_create.html'
    success_url = reverse_lazy('helpdesk:ticket_list')

