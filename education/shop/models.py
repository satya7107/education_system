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

class sorder(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=90)
    address=models.CharField(max_length=90)
    city=models.CharField(max_length=90)
    state=models.CharField(max_length=90)
    Zip_code=models.CharField(max_length=90)
    phone=models.CharField(max_length=90,default="")
    def __str__(self):
        return self.name

class order_update(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self. update_desc[0:7]+ "..."
