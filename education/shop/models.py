from django.db import models

# Create your models here.

class products(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    price = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
