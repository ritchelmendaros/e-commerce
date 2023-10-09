from django.db import models
from Ticket.models import CustomerTicket


class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20)
    user_address = models.CharField(max_length=50)
    type_choices = [
        ('CS', 'Customer Support'),
        ('S', 'Supplier'),
        ('CU', 'Customer'),
        ('CO', 'Courier'),
    ]
    type = models.CharField(max_length=2, choices=type_choices)


class Supplier(User):
    company_name = models.CharField(max_length=50)

class Customer(User):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)


class Address(models.Model):
    address_id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.SET_NULL, null=True)
    address = models.CharField(max_length=50)


class Courier(User):
    courier_name = models.CharField(max_length=50)
    fee = models.FloatField()


class CustomerSupport(User):
    support_name = models.CharField(max_length=50)
    ticket_id = models.ForeignKey(CustomerTicket, on_delete=models.CASCADE, null=True)

