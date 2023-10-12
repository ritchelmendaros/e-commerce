from django.urls import path
from .views import (CustomerSupportRegistrationView, CustomerRegistrationView, CustomerLoginView,
                    CustomerSupportLoginView, customer_support_index, customer_index)


urlpatterns = [
    path('customer-support-registration/', CustomerSupportRegistrationView.as_view(),
         name='customer_support_registration'),
    path('customer-registration/', CustomerRegistrationView.as_view(), name='customer_registration'),
    path('customer-login/', CustomerLoginView.as_view(), name='customer_login'),
    path('customer-support-login/', CustomerSupportLoginView.as_view(), name='customer_support_login'),
    path('customer-support-index/', customer_support_index, name='customer_support_index'),
    path('customer-index/', customer_index, name='customer_index'),
    # path('ticket-login/', views.ticket_login_view, name='ticket_login'),
]
