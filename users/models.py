# from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from PIL import Image
import os
from uuid import uuid4


def RenameImage(instance, filename):
    upload_to = 'profile_pics'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

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


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg',upload_to=RenameImage)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)