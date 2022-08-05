# from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Phonenumber(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=30)
    check1 = models.BooleanField(default=False)

    def __str__(self):
        return self.phonenumber 

class VendorModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=30)
    residence = models.CharField(max_length=30)
    experience = models.CharField(max_length=30)
    lga = models.CharField(max_length=30)
    categories = models.CharField(max_length=30)

    def __str__(self):
        return self.name + " the "+ self.categories