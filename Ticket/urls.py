from django.urls import path
from .views import customer_support_registration_view

urlpatterns = [
    path('customer-support-registration/', customer_support_registration_view, name='customer_support_registration'),
]
