from django.db import models
from Ticket.models import CustomerTicket
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_id = models.BigAutoField(primary_key=True)
    mobile_number = models.CharField(max_length=20)
    user_address = models.CharField(max_length=50)
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(blank=False)

    type_choices = [
        ('CS', 'Customer Support'),
        ('S', 'Supplier'),
        ('CU', 'Customer'),
        ('CO', 'Courier'),
    ]
    user_type = models.CharField(max_length=2, choices=type_choices)

    class Meta:
        verbose_name = 'User'


class Supplier(User):
    company_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Supplier'


class Customer(User):
    age = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Customer'


class Address(models.Model):
    address_id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.SET_NULL, null=True)
    address = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Address"


class Courier(User):
    courier_name = models.CharField(max_length=50)
    fee = models.FloatField()

    class Meta:
        verbose_name = 'Courier'


class CustomerSupport(User):
    support_name = models.CharField(max_length=50)
    ticket_id = models.ForeignKey(CustomerTicket, models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Customer Support'
