from django.db import models
from django.core.exceptions import ValidationError

# creating a phone validator function
# def validate_phone(value):
# 	if int(value) < 10: 		##10 is in quotes because the value stored in "value" is a str and we cannot compare str with int
# 		print("Invalid phone")
# 		raise ValidationError("Enter a valid phone number")
# 	else:
# 		return value

# # # creating an email validator function
# def validate_email(value1):
# 	if "@cognitioworld.com" not in value1:
# 		raise ValidationError("Enter a valid email id")
# 	else:
# 		return value1

class Employees(models.Model):
	emp_fname 			= models.CharField(max_length = 50)
	emp_lname 			= models.CharField(max_length = 50)
	emp_email			= models.EmailField()		##validators = [validate_email]
	emp_phone			= models.CharField(max_length = 10,primary_key = True, unique = True)  ##validators =[validate_phone])
	emp_desgn			= models.CharField(max_length = 100)
	emp_reporting_mgr 	= models.CharField(max_length = 100)
	emp_pass1 			= models.CharField(max_length = 100,help_text = "Password should be Alphanumeric")
	emp_pass2 			= models.CharField(max_length = 100,help_text = "Password should be Alphanumeric")


	def __str__(self):
		return self.emp_fname