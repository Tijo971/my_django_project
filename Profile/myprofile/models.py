from django.db import models

# Create your models here.
class images(models.Model):
    name=models.CharField(max_length=50, null=True, blank=True)
    image=models.ImageField(upload_to="profile", null=True, blank=True)

class datas(models.Model):
    n=models.CharField(max_length=50, null=True, blank=True)
    add=models.CharField(max_length=100, null=True, blank=True)
    mob=models.IntegerField(null=True, blank=True)
    em=models.CharField(max_length=50, null=True, blank=True)
    cour=models.CharField(max_length=50, null=True, blank=True)
    img=models.ImageField(upload_to="images", null=True, blank=True)

class Employe(models.Model):
    nme=models.CharField(max_length=20, null=True, blank=True)
    mobi=models.IntegerField(null=True,blank=True)
    ema=models.EmailField(max_length=40, null=True, blank=True)
    comp=models.CharField(max_length=20, null=True, blank=True)
    sal=models.IntegerField(null=True, blank=True)
    img=models.ImageField(upload_to="emp_pic", null=True, blank=True)

