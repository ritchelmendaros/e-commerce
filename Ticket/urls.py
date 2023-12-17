from django.urls import path
from . import views

urlpatterns = [
    path('customer-support-registration/', views.CustomerSupportRegistrationView.as_view(),
         name='customer_support_registration'),
    path('customer-support-inquiry/', views.customer_support_inquiry, name='customer_support_inquiry'),
    path('customer-registration/', views.CustomerRegistrationView.as_view(), name='customer_registration'),
    path('customer-helpdesk/', views.CustomerHelpdeskView.as_view(), name='customer_helpdesk'),
    path('customer-ticket-history/<str:username>/', views.CustomerTicketHistoryView.as_view(),
         name='customer_ticket_history'),
    path('ticket-login/', views.TicketLoginView.as_view(), name='ticket_login'),
]
