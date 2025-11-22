from django.db import models

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('O', 'Open'),
        ('C', 'Closed'),
    ]

    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    reporter_name = models.CharField(max_length=100)
    reporter_email = models.EmailField(blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')  # NEW
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"#{self.pk} {self.title}"

