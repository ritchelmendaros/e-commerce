from django.urls import path
from .views import CustomerSupportView

urlpatterns = [
    path('customer-support/', CustomerSupportView.as_view(), name='customer_support_form'),
]
