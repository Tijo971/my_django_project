from django.db import models

# Create your models here.

class stud_reg(models.Model):
    name=models.CharField(max_length=50, null=True, blank=True)
    email=models.CharField(max_length=50, null=True, blank=True)
    mobile= models.IntegerField(null=True, blank=True)
    address=models.CharField(max_length=100, null=True, blank=True)

