from django.db import models

class CustomerType(models.Model):
	customer_type 	= 	models.CharField(max_length = 30, primary_key = True, unique = True)

	def __str__(self):
		return self.customer_type


class CustomerName(models.Model):
	creg_no = 			models.CharField(max_length = 255, unique=True, primary_key = True)
	cname = 			models.CharField(max_length = 200)
	brand_name = 		models.CharField(max_length = 200, blank = True, null = True)
	ref_customertype =	models.ForeignKey(CustomerType, models.SET_NULL, null=True)

	def __str__(self):
		return self.creg_no


class CustomerContact(models.Model):


	pri_fname = 			models.CharField(max_length = 50)
	pri_lname = 			models.CharField(max_length = 50)
	pri_desg = 				models.CharField(max_length = 50)
	pri_email = 			models.EmailField()
	pri_phone = 			models.CharField(max_length = 10, primary_key = True, unique = True)
	pri_landline = 			models.CharField(max_length = 15)
	pri_flatno = 			models.CharField(max_length = 10)
	pri_streetname = 		models.CharField(max_length = 100)
	pri_landmark = 			models.CharField(max_length = 100)
	pri_city = 				models.CharField(max_length = 50)
	pri_pincode = 			models.CharField(max_length = 10)

	sec_fname = 			models.CharField(max_length = 50, blank = True, null = True)
	sec_lname = 			models.CharField(max_length = 50, blank = True, null = True)
	sec_desg = 				models.CharField(max_length = 50, blank = True, null = True)
	sec_email = 			models.EmailField(blank = True, null = True)
	sec_phone = 			models.CharField(max_length = 10, blank = True, null = True)
	sec_landline = 			models.CharField(max_length = 15, blank = True, null = True)
	sec_flatno = 			models.CharField(max_length = 10, blank = True, null = True)
	sec_streetname = 		models.CharField(max_length = 100, blank = True, null = True)
	sec_landmark = 			models.CharField(max_length = 100, blank = True, null = True)
	sec_city = 				models.CharField(max_length = 50, blank = True, null = True)
	sec_pincode = 			models.CharField(max_length = 10, blank = True, null = True)

	ref_creg_no = 			models.ForeignKey(CustomerName, on_delete = models.CASCADE, default = 'default', related_name='cust_ref')
	ref_cname = 			models.ForeignKey(CustomerName, on_delete = models.CASCADE, default = 'default', related_name='cust_name')

	def __str__(self):
		return self.pri_fname + ' ' + self.pri_lname
