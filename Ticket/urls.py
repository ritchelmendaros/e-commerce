from django.urls import path
from .views import (customer_support_registration_view, customer_support_login_view, customer_support_index,
                    customer_index, customer_login_view, customer_registration_view)

urlpatterns = [
    path('customer-support-registration/', customer_support_registration_view, name='customer_support_registration'),
    path('customer-support-login/', customer_support_login_view, name='customer_support_login'),
    path('customer-support-index', customer_support_index, name='customer_support_index'),
    path('customer-registration/', customer_registration_view, name='customer_registration'),
    path('customer-login/', customer_login_view, name='customer_login'),
    path('customer-index', customer_index, name='customer_index'),
]
