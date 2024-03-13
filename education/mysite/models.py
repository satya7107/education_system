from django.db import models

# Create your models here.
class employee(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField(max_length=20,unique=True)
    def __str__(self):
        return self.firstname
    
class student(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField(max_length=20,unique=True)
    image=models.ImageField(upload_to='images')
    def __str__(self):
        return self.firstname
    
class user(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    designation=models.CharField(max_length=20)
    email=models.EmailField(max_length=20,unique=True)
    image=models.ImageField(upload_to='images')
    def __str__(self):
        return self.firstname 

#Experties_models_
class all_experties(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    designation=models.CharField(max_length=200)
    email=models.EmailField(max_length=20,unique=True)
    image=models.ImageField(upload_to='images')
    def __str__(self):
        return self.firstname

class all_experties_ceo(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    designation=models.CharField(max_length=200)
    email=models.EmailField(max_length=20,unique=True)
    image=models.ImageField(upload_to='images')
    message = models.CharField(max_length=1000)
    def __str__(self):
        return self.firstname 
    
class all_experties_chanc(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    designation=models.CharField(max_length=200)
    email=models.EmailField(max_length=20,unique=True)
    image=models.ImageField(upload_to='images')
    message = models.CharField(max_length=1000)
    def __str__(self):
        return self.firstname
    
class all_experties_prince(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    designation=models.CharField(max_length=200)
    email=models.EmailField(max_length=20,unique=True)
    image=models.ImageField(upload_to='images')
    message = models.CharField(max_length=1000)
    def __str__(self):
        return self.firstname 

class all_experties_vice(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    designation=models.CharField(max_length=200)
    email=models.EmailField(max_length=20,unique=True)
    image=models.ImageField(upload_to='images')
    message = models.CharField(max_length=1000)
    def __str__(self):
        return self.firstname


class all_experties_fact(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    designation=models.CharField(max_length=200)
    email=models.EmailField(max_length=20,unique=True)
    image=models.ImageField(upload_to='images')
    message = models.CharField(max_length=1000)
    def __str__(self):
        return self.firstname                                  

class uregister(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50,unique=True)
    image=models.ImageField(upload_to='images')
    password=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username
    
class main_register(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50,unique=True)
    image=models.ImageField(upload_to='images')
    rollname=models.CharField(max_length=50)
    contact=models.CharField(max_length=10)
    password=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username    


