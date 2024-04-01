from django.db import models

# Create your models here.

class products(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category=models.CharField(max_length=100,default="")
    subcategory = models.CharField(max_length=100,default="")
    desc = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images',default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product_name
class scontact(models.Model):
    msg_id = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30,unique=True)
    desc=models.TextField(max_length=2000)
    phone=models.CharField(max_length=20,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
