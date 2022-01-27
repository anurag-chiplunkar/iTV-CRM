from django.db import models


# Create your models here.
class bill(models.Model):
	cust_name = models.CharField(max_length=100)
	phone = models.IntegerField(max_length=2000)
	items = models.CharField(max_length=100,blank=True,null=True)
	price_unit = models.IntegerField(max_length=100,blank=True,null=True)
	quantity = models.IntegerField(max_length=100,blank=True,null=True)
	total = models.IntegerField(max_length=100,blank=True,null=True)
	amt = models.IntegerField(max_length=100,blank=True,null=True)

