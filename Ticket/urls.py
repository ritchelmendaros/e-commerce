from django.urls import path
from . import views

urlpatterns = [
    path('customer-support-registration/', views.CustomerSupportRegistrationView.as_view(),
         name='customer_support_registration'),
    path('customer-support-login/', views.CustomerSupportLoginView.as_view(), name='customer_support_login'),
    path('customer-support-index/', views.customer_support_index, name='customer_support_index'),
    path('customer-registration/', views.CustomerRegistrationView.as_view(), name='customer_registration'),
    path('customer-login/', views.CustomerLoginView.as_view(), name='customer_login'),
    path('customer-index/', views.customer_index, name='customer_index'),
    path('ticket-login/', views.TicketLoginView.as_view(), name='ticket_login'),
]
