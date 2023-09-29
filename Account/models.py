from django.db import models


class User(models.Model):
    pass


class Supplier(User):
    pass


class Customer(User):
    pass


class Courier(User):
    pass

