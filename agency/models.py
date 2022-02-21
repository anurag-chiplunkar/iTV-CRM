from django.db import models


class AgencyDetail(models.Model):
	a_id 				= models.CharField(max_length = 100,primary_key = True, unique = True,default = 'default')
	agency_name 		= models.CharField(max_length = 200)
	agency_officeno		= models.CharField(max_length = 10)
	agency_street		= models.CharField(max_length = 100)
	agency_state 		= models.CharField(max_length = 50)
	agency_landmark		= models.CharField(max_length = 100,null = True, blank = True)
	agency_city			= models.CharField(max_length = 100)
	agency_pin			= models.IntegerField(max_length = 10)
	
	def __str__(self):
		return self.agency_name + ' -' + self.agency_state

class AgencyContact(models.Model):
	pri_firstName 	= models.CharField(max_length = 20)
	pri_lastName 	= models.CharField(max_length = 20)
	pri_designation = models.CharField(max_length = 100)
	pri_email		= models.EmailField()
	pri_phone		= models.CharField(max_length = 11,primary_key = True, unique = True)
	pri_landline	= models.CharField(max_length = 20)
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
	sec_landline	= models.CharField(max_length = 20,null = True,blank = True)
	sec_flatno		= models.CharField(max_length = 10,null = True, blank = True)
	sec_street		= models.CharField(max_length = 100,null = True, blank = True)
	sec_landmark	= models.CharField(max_length = 100,null = True, blank = True)
	sec_city		= models.CharField(max_length = 100,null = True, blank = True)
	sec_pin			= models.CharField(max_length = 10,null = True, blank = True)
	
	agency_details = models.ForeignKey(AgencyDetail,on_delete = models.CASCADE,default = 'default')

	def __str__(self):
		return self.pri_firstName

# one agency can have many contacts. 
# Thus in AgencyContact I should add a ForeignKey field with the argument as AgencyDetail
