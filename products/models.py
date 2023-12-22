from django.db import models
from users.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    title = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    specification = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Carts(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="carts")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
    cart_quantity = models.IntegerField(default=1)
    cart_total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.user.username} wish to buy {self.product.title}"