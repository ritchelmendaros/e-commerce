from django.db import models
from Account.models import Courier
from Payment.models import Payment
from Review.models import Review


class Order(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    courier_id = models.ForeignKey(Courier, on_delete=models.SET_NULL)
    payment_id = models.ForeignKey(Payment, on_delete=models.SET_NULL)
    choices = [
        ("PR", "Preparing Shipment"),
        ("PE", "Pending"),
        ("DE", "Delivered"),
    ]
    status = models.CharField(max_length=2, choices=choices)


class OrderItem(models.Model):
    order_item_id = models.BigAutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    review_id = models.ForeignKey(Review, on_delete=models.SET_NULL)



