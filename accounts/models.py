from django.db import models

class Employees(models.Model):
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