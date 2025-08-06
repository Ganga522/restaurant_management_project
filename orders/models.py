from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from products.models import Menu

class Order(models.Model):
    STATUS_CHOICES=[
        ('PENDING','Pending'),
        ('CONFIRMED','Confirmed'),
        ('DELIVERED','Delivered'),
        ('CANCELLED','Cancelled'),
    ]

    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    order_item=models.ForeignKey(Menu,on_delete=models.CASCADE)
    total_amount=models.DecimalField(max_length=8,decimal_places=2)
    order_status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='PENDING')
    order_date=models.DateTimeField(auto_now_add=True)