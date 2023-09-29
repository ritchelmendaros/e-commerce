from django.db import models
from Account.models import Supplier, Customer


class Category(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=50)


class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL)
    user_id = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    order_item = models.ForeignKey('Order.OrderItem', on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)


class Wishlist(models.Model):
    wishlist_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
