from django.db import models

# Create your models here.
class stud_table(models.Model):
    name=models.CharField(max_length=50, null=True, blank=True)
    age =models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True)

class Employee(models.Model):
    emp_name=models.CharField(max_length=50, null=True, blank=True)
    company = models.CharField(max_length=20, null=True, blank=True)
    salary = models.IntegerField(null=True,blank=True)

