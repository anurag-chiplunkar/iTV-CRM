from django.db import models

class Employees(models.Model):
	username	= models.CharField(max_length = 20,default = 'default')
	firstName 	= models.CharField(max_length = 20)
	lastName 	= models.CharField(max_length = 20)
	designation = models.CharField(max_length = 100)
	department	= models.CharField(max_length = 100)
	email		= models.EmailField()
	phone		= models.CharField(max_length = 10)

	def __str__(self):
		return self.firstName
