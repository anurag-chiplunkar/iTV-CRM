from django.db import models


class AgencyDetail(models.Model):
	a_id 		= models.CharField(max_length = 100,primary_key = True, unique = True,default = 'default')
	agency_name = models.CharField(max_length = 200)
	agency_state = models.CharField(max_length = 50)

	def __str__(self):
		return self.a_id

class AgencyContact(models.Model):
	# ac_id 		= models.CharField(max_length = 100,primary_key = True, unique = True, default = 'default')
	firstName 	= models.CharField(max_length = 20)
	lastName 	= models.CharField(max_length = 20)
	designation = models.CharField(max_length = 100)
	email		= models.EmailField()
	phone		= models.CharField(max_length = 11,primary_key = True, unique = True, default = 'default')
	agency_details = models.ForeignKey(AgencyDetail,on_delete = models.CASCADE,default = 'default')

	def __str__(self):
		return self.firstName

# one agency can have many contacts. 
# Thus in AgencyContact I should add a ForeignKey field with the argument as AgencyDetail
