from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    place = models.CharField(max_length=20, null=True, blank=True)
    course = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to='stud_pic', null=True, blank=True)