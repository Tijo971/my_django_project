from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=20, null=True, blank=True)
    age=models.IntegerField(null=True, blank=True)