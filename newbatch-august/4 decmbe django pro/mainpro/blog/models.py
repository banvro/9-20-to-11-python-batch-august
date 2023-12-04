from django.db import models

# Create your models here.

class SaveDetail(models.Model):
    Name = models.CharField(max_length=150)
    Phone_Number = models.IntegerField()
    Email = models.CharField(max_length=50)
    message = models.TextField()