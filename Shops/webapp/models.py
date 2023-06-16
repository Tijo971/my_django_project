from django.db import models

# Create your models here.

class UserDB(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=26, null=True, blank=True)
    mob_num=models.IntegerField(null=True, blank=True)
    img = models.ImageField(upload_to="profile", null=True, blank=True)
    passwd = models.CharField(max_length=20, null=True, blank=True)

class ContactDB(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    phn_no = models.IntegerField(null=True, blank=True)
    msg = models.CharField(max_length=1000, null=True, blank=True)
