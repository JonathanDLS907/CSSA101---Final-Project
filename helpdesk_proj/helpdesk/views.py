from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from .models import Ticket
from .forms import TicketForm

class TicketListView(ListView):
    model = Ticket
    template_name = 'helpdesk/ticket_list.html'
    context_object_name = 'tickets'
    paginate_by = 20

    def get_queryset(self):
        qs = Ticket.objects.order_by('-created_at')
        q = self.request.GET.get('q', '').strip()
        pr = self.request.GET.get('priority', '').strip()
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q))
        if pr in dict(Ticket.PRIORITY_CHOICES):
            qs = qs.filter(priority=pr)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['q'] = self.request.GET.get('q', '')
        ctx['selected_priority'] = self.request.GET.get('priority', '')
        return ctx

class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'helpdesk/ticket_detail.html'
    context_object_name = 'ticket'

class TicketCreateView(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'helpdesk/ticket_create.html'
    success_url = reverse_lazy('helpdesk:ticket_list')

    def form_valid(self, form):
        response = super().form_valid(form) 

        ticket_url = self.request.build_absolute_uri(
            reverse('helpdesk:ticket_detail', args=[self.object.pk])
        )

        if self.object.reporter_email:
            subject = f"Ticket #{self.object.pk} received"
            message = (
                f"Hello {self.object.reporter_name},\n\n"
                f"Your ticket has been received.\n\n"
                f"Ticket ID: {self.object.pk}\n"
                f"Title: {self.object.title}\n"
                f"View: {ticket_url}\n\n"
                "We will respond as soon as possible."
            )
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [self.object.reporter_email],
                fail_silently=True,
            )

        return response

