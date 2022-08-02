# from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Phonenumber(models.Model):
    phonenumber = models.CharField(max_length=30)
    check1 = models.BooleanField(default=False)

    def __str__(self):

class VendorModel(models.model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=30)
    residence = models.CharField(max_length=30)
    experience = models.Charfield(max_length=30)
    lga = models.CharField(max_length=30)
    categories = models.Charfield(max_length=30)

    def __str__(self):
        return self.name + self.categories