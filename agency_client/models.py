from django.db import models


		
class CustomerType(models.Model):
	""" Registration of Customer Type (Government, retail, corporate and barter)

	:customer_type: saves customer type
 
	:CharField: customer_type
	:Primary Key: customer_type
	"""
	customer_type 	= 	models.CharField(max_length = 30, primary_key = True, unique = True)

	def __str__(self):
		return self.customer_type


class CustomerName(models.Model):
	"""Saves Customer Name
	
	:creg_no: saves registration number of Client
	:cname: saves name of client
	:brand_name: saves brand name of client
	:ref_customertype: saving customer type from CustomerType model
	:created_at: saves date and time of client registration
	
	:CharField: creg_no,cname,brand_name
	:Foreign key: ref_customertype
	:Unique Key: creg_no
	:Primary Key: creg_no
	:DateTimeField: create_at"""

	creg_no = 			models.CharField(max_length = 255, unique=True, primary_key = True)
	cname = 			models.CharField(max_length = 200)
	brand_name = 		models.CharField(max_length = 200, blank = True, null = True)
	ref_customertype =	models.ForeignKey(CustomerType, models.SET_NULL, null=True)
	
	create_at 			= models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.creg_no

class CustomerContact(models.Model):
	""" Saves client contacts
	:pri_fname: saves first name from primary contact
	:pri_lname: saves last name from  primary contact
	:pri_desg: saves designation from  primary contact
	:pri_email: saves email from primary contact
	:pri_phone: saves phone number from primary contact
	:pri_landline: saves landline number from primary contact
	:pri_flatno: saves flotno from primary contact
	:pri_streetname: saves streetname from primary contact
	:pri_landmark: saves landmark from primary contact
	:pri_city: saves city from primary contact
	:pri_pincode: saves pincode from primary contact
	:sec_fname: saves first name from secondary contact
	:sec_lname: saves last name from secondary contact
	:sec_desg: saves designation from secondary contact
	:sec_email: saves email from secondary contact
	:sec_phone: saves phone number from secondary contact
	:sec_landline: saves landline number from secondary contact
	:sec_flatno: saves flat number from secondary contact
	:sec_streetname: saves streetname from secondary contact
	:sec_landmark: saves landmark from secondary contact
	:sec_city: saves city from secondary contact
	:sec_pincode: saves pincode from secondary contact
	:ref_creg_no: saves client registration number from CustomerName model

	:CharField: pri_fname, pri_lname, pri_desg, pri_phone, pri_landline, pri_flatno, pri_streetname, pri_landmark, pri_city, pri_pincode,
				sec_fname, sec_lname, sec_desg, sec_phone, sec_landline, sec_flatno, sec_streetname, sec_landmark, sec_city, sec_pincode
	:EmailField: pri_email, sec_email
	:Foreign key: ref_creg_no
	:Primary key: pri_phone
	:Unique key: pri_phone
	"""
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

	# ref_cname = 			models.ForeignKey(CustomerName, on_delete = models.CASCADE, default = 'default', related_name='cust_name', null=True)
	ref_creg_no = 			models.ForeignKey(CustomerName, on_delete = models.CASCADE, default = 'default', related_name='cust_ref')

	def __str__(self):
		return self.pri_fname + ' ' + self.pri_lname


class AgencyDetail(models.Model):
	"""Saves agency details
	:a_id: saves agency id
	:agency_name: saves agency name
	:agency_officeno: saves agency office number
	:agency_street: saves agency street name
	:agency_state: saves state of agency
	:agency_landmark: saves landmark of agency
	:agency_city: saves city of agency
	:agency_pin: saves pincode of agency
	:ccreg_no: saves registraion number from CustomerName
	:created_at: saves date and time when all the details are added
	
	:CharField: a_id, agency_name, agency_officeno, agency_street, agency_state, agency_landmark, agency_city
	:Primary Key: a_id
	:Foreign Key: ccreg_no
	:Unique Key: a_id 
	:DateTimeField: create_at"""
	a_id 				= models.CharField(max_length = 100,primary_key = True, unique = True,default = 'default')
	agency_name 		= models.CharField(max_length = 200)
	agency_officeno		= models.CharField(max_length = 10)
	agency_street		= models.CharField(max_length = 100)
	agency_state 		= models.CharField(max_length = 50)
	agency_landmark		= models.CharField(max_length = 100,null = True, blank = True)
	agency_city			= models.CharField(max_length = 100)
	agency_pin			= models.IntegerField()
	ccreg_no 			= models.ForeignKey(CustomerName, on_delete = models.CASCADE, default = 'default')
	create_at 			= models.DateTimeField(auto_now_add = True)
	
	def __str__(self):
		return self.agency_name + ' -' + self.agency_state


class AgencyContact(models.Model):
	"""Saves Agency contact
	
	:pri_fname: saves first name from primary contact
	:pri_lname: saves last name from  primary contact
	:pri_desg: saves designation from  primary contact
	:pri_email: saves email from primary contact
	:pri_phone: saves phone number from primary contact
	:pri_landline: saves landline number from primary contact
	:pri_flatno: saves flotno from primary contact
	:pri_streetname: saves streetname from primary contact
	:pri_landmark: saves landmark from primary contact
	:pri_city: saves city from primary contact
	:pri_pincode: saves pincode from primary contact
	:sec_fname: saves first name from secondary contact
	:sec_lname: saves last name from secondary contact
	:sec_desg: saves designation from secondary contact
	:sec_email: saves email from secondary contact
	:sec_phone: saves phone number from secondary contact
	:sec_landline: saves landline number from secondary contact
	:sec_flatno: saves flat number from secondary contact
	:sec_streetname: saves streetname from secondary contact
	:sec_landmark: saves landmark from secondary contact
	:sec_city: saves city from secondary contact
	:sec_pincode: saves pincode from secondary contact
	:agency_details: saves agency details from AgencyDetail model

	:CharField: pri_fname, pri_lname, pri_desg, pri_phone, pri_landline, pri_flatno, pri_streetname, pri_landmark, pri_city, pri_pincode,
				sec_fname, sec_lname, sec_desg, sec_phone, sec_landline, sec_flatno, sec_streetname, sec_landmark, sec_city, sec_pincode
	:EmailField: pri_email, sec_email
	:Foreign key: AgencyDetail
	:Primary key: pri_phone
	:Unique key: pri_phone
	"""
	pri_firstName 	= models.CharField(max_length = 20)
	pri_lastName 	= models.CharField(max_length = 20)
	pri_designation = models.CharField(max_length = 100)
	pri_email		= models.EmailField()
	pri_phone		= models.CharField(max_length = 11,primary_key = True, unique = True)
	pri_landline	= models.CharField(max_length = 8)
	pri_flatno		= models.CharField(max_length = 10)
	pri_street		= models.CharField(max_length = 100)
	pri_landmark	= models.CharField(max_length = 100,null = True, blank = True)
	pri_city		= models.CharField(max_length = 100)
	pri_pin			= models.CharField(max_length = 10)

	sec_firstName 	= models.CharField(max_length = 20,null = True,blank = True)
	sec_lastName 	= models.CharField(max_length = 20,null = True,blank = True)
	sec_designation = models.CharField(max_length = 100,null = True,blank = True)
	sec_email		= models.EmailField(null = True,blank = True)
	sec_phone		= models.CharField(max_length = 11,null = True,blank = True)
	sec_landline	= models.CharField(max_length = 8,null = True,blank = True)
	sec_flatno		= models.CharField(max_length = 10,null = True, blank = True)
	sec_street		= models.CharField(max_length = 100,null = True, blank = True)
	sec_landmark	= models.CharField(max_length = 100,null = True, blank = True)
	sec_city		= models.CharField(max_length = 100,null = True, blank = True)
	sec_pin			= models.CharField(max_length = 10,null = True, blank = True)
	create_at 		= models.DateTimeField(auto_now_add = True)

	
	agency_details = models.ForeignKey(AgencyDetail,on_delete = models.CASCADE,default = 'default')

	def __str__(self):
		return self.pri_firstName


# class CustomerType(models.Model):
# 	customer_type 	= 	models.CharField(max_length = 30, primary_key = True, unique = True)

# 	def __str__(self):
# 		return self.customer_type


# class CustomerName(models.Model):
# 	creg_no 			= models.CharField(max_length = 255, unique=True, primary_key = True)
# 	cname 				= models.CharField(max_length = 200)
# 	brand_name 			= models.CharField(max_length = 200, blank = True, null = True)
# 	ref_customertype 	= models.ForeignKey(CustomerType, models.SET_NULL, null=True)
# 	create_at 			= models.DateTimeField(auto_now_add = True)


# 	def __str__(self):
# 		return self.creg_no




# class CustomerContact(models.Model):


# 	pri_fname = 			models.CharField(max_length = 50)
# 	pri_lname = 			models.CharField(max_length = 50)
# 	pri_desg = 				models.CharField(max_length = 50)
# 	pri_email = 			models.EmailField()
# 	pri_phone = 			models.CharField(max_length = 10, primary_key = True, unique = True)
# 	pri_landline = 			models.CharField(max_length = 8)
# 	pri_flatno = 			models.CharField(max_length = 10)
# 	pri_streetname = 		models.CharField(max_length = 100)
# 	pri_landmark = 			models.CharField(max_length = 100)
# 	pri_city = 				models.CharField(max_length = 50)
# 	pri_pincode = 			models.CharField(max_length = 10)

# 	sec_fname = 			models.CharField(max_length = 50, blank = True, null = True)
# 	sec_lname = 			models.CharField(max_length = 50, blank = True, null = True)
# 	sec_desg = 				models.CharField(max_length = 50, blank = True, null = True)
# 	sec_email = 			models.EmailField(blank = True, null = True)
# 	sec_phone = 			models.CharField(max_length = 10, blank = True, null = True)
# 	sec_landline = 			models.CharField(max_length = 8, blank = True, null = True)
# 	sec_flatno = 			models.CharField(max_length = 10, blank = True, null = True)
# 	sec_streetname = 		models.CharField(max_length = 100, blank = True, null = True)
# 	sec_landmark = 			models.CharField(max_length = 100, blank = True, null = True)
# 	sec_city = 				models.CharField(max_length = 50, blank = True, null = True)
# 	sec_pincode = 			models.CharField(max_length = 10, blank = True, null = True)
# 	create_at 			= models.DateTimeField(auto_now_add = True)


# 	# ref_cname = 			models.ForeignKey(CustomerName, on_delete = models.CASCADE, default = 'default', related_name='cust_name', null=True)
# 	ref_creg_no = 			models.ForeignKey(CustomerName, on_delete = models.CASCADE, default = 'default', related_name='cust_ref')

# 	def __str__(self):
# 		return self.pri_fname + ' ' + self.pri_lname
