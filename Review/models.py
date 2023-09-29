from django.db import models
from Account.models import Customer
from Product.models import Product


class Review(models.Model):
    review_id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    comment = models.CharField(max_length=100)
