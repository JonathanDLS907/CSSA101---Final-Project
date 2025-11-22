from django.urls import path
from . import views

app_name = "helpdesk"

urlpatterns = [
    path("", views.TicketListView.as_view(), name="ticket_list"),
    path("ticket/<int:pk>/", views.TicketDetailView.as_view(), name="ticket_detail"),
    path("ticket/create/", views.TicketCreateView.as_view(), name="ticket_create"),
]
