from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    msg = models.TextField()