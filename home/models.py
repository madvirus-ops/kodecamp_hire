from django.db import models

# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phonecode = models.CharField(max_length=7)
    phone = models.CharField(max_length=30)
    message = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.message