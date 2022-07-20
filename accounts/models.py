from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_Number(models.Model):
    
    number = models.CharField(max_length=30)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    terms = models.CharField(max_length=10)
    
    def __str__(self):
        return self.user.first_name + ' ' + 'phone number'

class Vendor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phonecode = models.CharField(max_length=5)
    phone = models.CharField(max_length=30)
    categories = models.CharField(max_length=50)
    address = models.CharField(max_length=1000)
    statec= models.CharField(max_length=50)
    lga = models.CharField(max_length=50)
    experience = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
