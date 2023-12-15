from django.db import models

# Create your models here.

class TodoData(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    desc = models.TextField()
    added_date = models.DateTimeField(auto_now=True)





    