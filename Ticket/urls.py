from django.urls import path
from . import views

urlpatterns = [
    path('customer-support-registration/', views.CustomerSupportRegistrationView.as_view(),
         name='customer_support_registration'),
    path('customer-support-login/', views.CustomerSupportLoginView.as_view(), name='customer_support_login'),
    path('customer-support-inquiry/', views.customer_support_inquiry, name='customer_support_inquiry'),
    path('customer-registration/', views.CustomerRegistrationView.as_view(), name='customer_registration'),
    path('customer-login/', views.CustomerLoginView.as_view(), name='customer_login'),
    path('customer-helpdesk/', views.CustomerHelpdeskView.as_view(), name='customer_helpdesk'),
    path('customer-ticket-history/', views.customer_ticket_history, name='customer_ticket_history'),
    path('ticket-login/', views.TicketLoginView.as_view(), name='ticket_login'),
    # path('submit_ticket/', views.submit_ticket, name='submit_ticket'),
]
