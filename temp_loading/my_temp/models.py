from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    course = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=60, null=True, blank=True)
    imge = models.ImageField(upload_to="profile", null=True, blank=True)


class Course(models.Model):
    course_name = models.CharField(max_length=20, null=True, blank=True)
    fees = models.IntegerField(null=True, blank=True)
    duration = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=20, null=True, blank=True)
    institute = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to="institute", null=True, blank=True)