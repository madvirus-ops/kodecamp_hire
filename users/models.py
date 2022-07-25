from django.db import models

# Create your models here.

class Phonenumber(models.Model):
    phonenumber = models.CharField(max_length=30)
    check1 = models.BooleanField(default=False)