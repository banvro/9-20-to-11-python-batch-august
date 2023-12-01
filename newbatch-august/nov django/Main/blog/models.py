from django.db import models

# Create your models here.

class ContactUs(models.Model):
    Name = models.CharField(max_length = 150)
    Email = models.CharField(max_length=150)
    Phone_Number = models.IntegerField()
    Message = models.TextField()



# python manage.py makemigrations


# python manage.py migrate
