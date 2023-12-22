from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Orders(models.Model):
    PENDING = "pending"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    SHIPPED = "shipped"
    ORDER_STATUS = {
        (PENDING, "pending"),
        (DELIVERED, "delivered"),
        (CANCELLED, "cancelled"),
        (SHIPPED, "shipped"),
    }
    tracking_id = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    house_number = models.CharField(max_length=100)
    message = models.CharField(max_length=500, null=True)
    order_total = models.FloatField()
    products = models.JSONField()
    status = models.CharField(max_length=50, default=PENDING, choices=ORDER_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)