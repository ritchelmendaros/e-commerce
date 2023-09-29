from django.db import models
from Account.models import Customer


class Payment(models.Model):
    payment_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)

    amount = models.FloatField()
    payment_date = models.DateField()