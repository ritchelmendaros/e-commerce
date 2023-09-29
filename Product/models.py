from django.db import models
from Account.models import User

class Category(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=50)

class Product(models.Model):
    category_id = models.ForeignKey(Category)
    user_id = models.ForeignKey(User)
    order_item = models.ForeignKey(order_item)

    product_id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()

class Wishlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    wishlist_id = models.BigAutoField(primary_key=True)
