from django.db import models


# Create your models here.


    


class todoregisternew(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
    rol_name=models.CharField(max_length=40)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username
    
