from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import timedelta

class Ticket(models.Model):
    STATUS_CHOICES = [('P','Pending'),('O','Open'),('R','Resolved'),('C','Closed')]
    PRIORITY_CHOICES = [('L','Low'),('M','Medium'),('H','High')]

    title = models.CharField(max_length=200)
    description = models.TextField()
    reporter_name = models.CharField(max_length=100)
    reporter_email = models.EmailField(blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')  # if already added in 1.1
    sla_hours = models.PositiveIntegerField(default=48)   # NEW: SLA window in hours
    due_at = models.DateTimeField(null=True, blank=True)  # NEW: computed

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # set due_at when creating (only if not set)
        if not self.pk and not self.due_at:
            self.due_at = timezone.now() + timedelta(hours=self.sla_hours)
        super().save(*args, **kwargs)

    def is_overdue(self):
        return self.due_at and timezone.now() > self.due_at and self.status not in ('R','C')
    
    def get_absolute_url(self):
        return reverse('helpdesk:ticket_detail', args=[str(self.pk)])
