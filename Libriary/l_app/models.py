from django.db import models

# Create your models here.
class books(models.Model):
    b_nme=models.CharField(max_length=50, null=True, blank=True)
    a_nme=models.CharField(max_length=50, null=True, blank=True)
    pri=models.IntegerField(null=True, blank=True)

class users(models.Model):
    nme=models.CharField(max_length=50, null=True, blank=True)
    eml=models.CharField(max_length=50, null=True, blank=True)
    age=models.IntegerField(null=True, blank=True)
    mob=models.IntegerField(null=True, blank=True)
    pri=models.IntegerField(null=True, blank=True)