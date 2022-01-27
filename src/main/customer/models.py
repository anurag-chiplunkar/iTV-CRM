from django.db import models


class CustomerType(models.Model):
	ctype_id 	  = models.CharField(max_length = 30, primary_key = True,unique = True,default = 'default')
	customer_type = models.CharField(max_length = 50)

	def __str__(self):
		return self.customer_type

class CustomerName(models.Model):
	cust_id 	 = models.CharField(max_length = 10, primary_key = True,unique = True,default = 'default')
	name 		 = models.CharField(max_length = 200)
	customertype = models.ForeignKey(CustomerType,on_delete = models.CASCADE,default = 'default')

	def __str__(self):
		return self.name

class CustomerContact(models.Model):
	cc_id		= models.CharField(max_length = 100, primary_key = True,unique = True,default = 'default')
	firstName 	= models.CharField(max_length = 20)
	lastName 	= models.CharField(max_length = 20)
	designation = models.CharField(max_length = 100)
	email		= models.EmailField()
	phone		= models.CharField(max_length = 11)
	customername = models.ForeignKey(CustomerName,on_delete = models.CASCADE, default = 'default')

	def __str__(self):
		return self.firstName
