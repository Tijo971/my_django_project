from django.db import models

# Create your models here.
class categorys(models.Model):
    c_name = models.CharField(max_length=20, null=True, blank=True)
    c_img = models.ImageField(upload_to="category_img", null=True, blank=True)
    c_description = models.CharField(max_length=50, null=True, blank=True)


class product(models.Model):
    category = models.CharField(max_length=20, null=True, blank=True)
    p_name = models.CharField(max_length=20, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    brand = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to="products", null=True, blank=True)
