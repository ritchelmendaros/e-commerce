from django.urls import path
from . import views


urlpatterns = [
    path('customer-support-registration/', views.customer_support_registration_view,
         name='customer_support_registration'),
    path('customer-support-login/', views.customer_support_login_view, name='customer_support_login'),
    path('customer-support-index/', views.customer_support_index, name='customer_support_index'),
    path('customer-registration/', views.customer_registration_view, name='customer_registration'),
    path('customer-login/', views.customer_login_view, name='customer_login'),
    path('customer-index/', views.customer_index, name='customer_index'),
]
