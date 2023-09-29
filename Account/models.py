from django.db import models


class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)


class Supplier(User):
    company_name = models.CharField(max_length=50)


class Customer(User):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)


class Address(models.Model):
    address_id = models.BigAutoField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)


class Courier(User):
    courier_name = models.CharField(max_length=50)
    fee = models.FloatField()

