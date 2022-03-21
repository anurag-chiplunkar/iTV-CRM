from django.db import models
from django.core.exceptions import ValidationError

class Employees(models.Model):
	"""Model for Employee Registration
		
		:variable emp_fname: Employee's First Name
		:variable emp_lname: Employee's Last Name
		:variable emp_email: Employee's Email id
		:variable emp_phone: Employee's Phone Number
		:variable emp_desgn: Employee's Designation
		:variable emp_reporting_mgr: Employee's Reporting Manager
		:variable emp_pass1: Employee's Password
		:variable emp_pass2: Employee's Confirm Password"""
		
	emp_fname 			= models.CharField(max_length = 50)
	emp_lname 			= models.CharField(max_length = 50)
	emp_email			= models.EmailField()	
	emp_phone			= models.CharField(max_length = 10,primary_key = True, unique = True)  
	emp_desgn			= models.CharField(max_length = 100)
	emp_reporting_mgr 	= models.CharField(max_length = 100)
	emp_pass1 			= models.CharField(max_length = 100)
	emp_pass2 			= models.CharField(max_length = 100)


	def __str__(self):
		return self.emp_fname