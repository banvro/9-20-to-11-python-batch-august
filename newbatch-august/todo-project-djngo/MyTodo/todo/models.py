from django.db import models

# Create your models here.

class TodoData(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    added_date = models.DateTimeField(auto_now=True)
    My_Image = models.ImageField(upload_to="savedImages", null=True, blank=True)



