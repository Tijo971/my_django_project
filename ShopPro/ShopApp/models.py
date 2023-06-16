from django.db import models

# Create your models here.
class Shopdb(models.Model):
    na=models.CharField(max_length=20, null=True, blank=True)
    ow_nm=models.CharField(max_length=20, null=True, blank=True)
    mobile=models.IntegerField(null=True, blank=True)
    locat=models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to='shop_pic', null=True, blank=True)


class Productdb(models.Model):
    p_na=models.CharField(max_length=20, null=True, blank=True)
    qty=models.IntegerField(null=True, blank=True)
    price=models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='product_pic', null=True, blank=True)
