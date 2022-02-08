from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from . models import Employees

User = get_user_model()

class Employee_registration(forms.ModelForm):
	class Meta:
		model = Employees
		fields = '__all__'
		exclude = ('emp_desgn',)

		widgets = {
		'emp_fname' 		: forms.TextInput(attrs={'class': 'form-control bg-white border-left-0 border-md', 'placeholder':'First Name'}),
		'emp_lname' 		: forms.TextInput(attrs={'class': 'form-control bg-white border-left-0 border-md', 'placeholder':'Last Name'}),
		'emp_email' 		: forms.EmailInput(attrs={'class': 'form-control bg-white border-left-0 border-md', 'placeholder':'Email Id'}),
		'emp_phone' 		: forms.TextInput(attrs={'class': 'form-control bg-white border-left-0 border-md', 'placeholder':'Mobile Number'}),
		'emp_desgn'			: forms.TextInput(attrs={'class': 'form-control bg-white border-left-0 border-md', 'placeholder':'Designation'}),
		'emp_reporting_mgr' : forms.TextInput(attrs={'class': 'form-control bg-white border-left-0 border-md pl-3', 'placeholder':'Your Reporting Manager'}),

		'emp_pass1'			: forms.PasswordInput(attrs={'class': 'form-control bg-white border-left-0 border-md', 'placeholder':'Create Password'}),
		'emp_pass2'			: forms.PasswordInput(attrs={'class': 'form-control bg-white border-left-0 border-md', 'placeholder':'Confirm Password'})
		}

	def clean_email(self):
		email= self.cleaned_data.get("emp_email")
		if not "cognitioworld.com" in email:
			raise forms.ValidationError("Enter valid gmail ID")
		return email

	##to check that created and confirmed passwords match 
	def confirm_pass(self):
		pass1 = self.cleaned_data.get('emp_pass1')
		pass2 = self.cleaned_data.get('emp_pass2')
		if pass1 != pass2:
			raise forms.ValidationError("Pass 1 and Pass2 do not match")
		else:
			pass
		return pass1

	##to check if the email already exists 
	def confirm_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(emp_email = email)
		print(qs)
		if qs.exists():
			raise forms.ValidationError("Email already exists")
		else:
			return email



class Employee_login(forms.ModelForm):
	class Meta:
		model = Employees
		fields = ['emp_email','emp_pass1']

		widgets = {
		'emp_email' 	: forms.EmailInput(attrs={'class': 'form-control'}),
		'emp_pass1'		: forms.PasswordInput(attrs={'class': 'form-control'})

		}

	##To check if the email already exists
	def confirm_email(self):
		email = self.cleaned_data.get('emp_email')
		qs = User.objects.filter(emp_email = email)
		print(qs)
		if qs.exists():
			raise forms.ValidationError("Email already exists")
		else:
			return email

	##To check if the password already exists
	def confirm_password(self):
		password = self.cleaned_data.get('emp_pass1')
		qs = User.objects.filter(emp_pass1 = password)
		print(qs)
		if qs.exists():
			raise forms.ValidationError("Password already exists")
		else:
			return password