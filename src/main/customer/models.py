from django.db import models

# Create your models here.
class CustomerType(models.Model):
	customer_type 	= 	models.CharField(max_length = 30)

	def __str__(self):
		return self.customer_type


class CustomerName(models.Model):
	cname = 			models.CharField(max_length = 200)
	ref_customertype =	models.ForeignKey(CustomerType, on_delete = models.CASCADE, default = 'default')


class CustomerContact(models.Model):
	cc_fname = 			models.CharField(max_length = 50)
	cc_lname = 			models.CharField(max_length = 50)
	cc_designation = 	models.CharField(max_length = 50)
	cc_email = 			models.EmailField()
	phone = 			models.IntegerField(max_length = 10, primary_key = True, unique = True, default = 'default')
	ref_cname = 		models.ForeignKey(CustomerName, on_delete = models.CASCADE, default = 'default')

	def __str__(self):
		return self.ref_cname