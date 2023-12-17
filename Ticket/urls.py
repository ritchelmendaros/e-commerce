from django.urls import path
from . import views

urlpatterns = [
    path('customer-support-registration/', views.CustomerSupportRegistrationView.as_view(),
         name='customer_support_registration'),
    path('customer-support-inquiry/<str:username>/', views.CustomerSupportInquiry.as_view(),
         name='customer_support_inquiry'),
    path('customer-registration/', views.CustomerRegistrationView.as_view(), name='customer_registration'),
    path('customer-helpdesk/', views.CustomerHelpdeskView.as_view(), name='customer_helpdesk'),
    path('customer-ticket-history/<str:username>/', views.CustomerTicketHistoryView.as_view(),
         name='customer_ticket_history'),
    path('ticket-login/', views.TicketLoginView.as_view(), name='ticket_login'),
    path('ticket-customer-threaded/<int:ticket_id>/<str:ticket_description>/<str:issue_status>/<str:username>/',
         views.CustomerThreadedDiscussionView.as_view(), name='ticket_customer_threaded'),
    path('ticket-support-threaded/<int:ticket_id>/<str:ticket_description>/<str:email>/<str:issue_status>',
         views.SupportThreadedDiscussionView.as_view(), name='ticket_support_threaded'),
]
