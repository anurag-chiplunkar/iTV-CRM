from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class Emp_signup(forms.Form):
	# username = forms.CharField(
	# widget = forms.TextInput(
	# 	attrs = {
	# 		"class":"form-control",
	# 		"id":"form_mail",
	# 		"placeholder":"Enter username"
	# 		}))

	firstName = forms.CharField(
	widget = forms.TextInput(
		attrs = {
			"class":"form-control",
			"id":"form_mail",
			"placeholder":"Enter your first name"
			}))

	lastName = forms.CharField(
	widget = forms.TextInput(
		attrs = {
			"class":"form-control",
			"id":"form_mail",
			"placeholder":"Enter your last name"
			}))

	designation = forms.CharField(
	widget = forms.TextInput(
		attrs = {
			"class":"form-control",
			"id":"form_mail",
			"placeholder":"Enter your designation"
			}))

	department = forms.CharField(
	widget = forms.TextInput(
		attrs = {
			"class":"form-control",
			"id":"form_mail",
			"placeholder":"Enter your department"
			}))

	email = forms.CharField(
	widget = forms.TextInput(
		attrs = {
			"class":"form-control",
			"id":"form_mail",
			"placeholder":"Enter your email id"
			}))

	phone = forms.CharField(
	widget = forms.TextInput(
		attrs = {
			"class":"form-control",
			"id":"form_mail",
			"placeholder":"Enter your phone number"
			}))

	pass1 = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				"class":"form-control",
				"id":"form_pass1",
				"placeholder":"Create a password"
			}))

	pass2 = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				"class":"form-control",
				"id":"form_pass2",
				"placeholder":"Confirm your password"
			}))

	##to check that created and confirmed passwords match 
	def confirm_pass(self):
		pass1 = self.cleaned_data.get('pass1')
		pass2 = self.cleaned_data.get('pass2')
		if pass1 != pass2:
			raise forms.ValidationError("Pass 1 and Pass2 do not match")
		else:
			pass
		return pass1


	##to check if the email already exists
	def confirm_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email = 'email')
		print(qs)
		if qs.exists():
			raise forms.ValidationError('email already exists')
		else:
			return email

	# ##to check if the username already exists
	# def confirm_username(self):
	# 	username = self.cleaned_data.get('username')
	# 	qs = User.objects.filter(email = 'username')
	# 	print(qs)
	# 	if qs.exists():
	# 		raise forms.ValidationError('username already exists')
	# 	else:
	# 		return username





class Emp_login(forms.Form):
	email = forms.CharField(
	widget = forms.TextInput(
		attrs = {
			"class":"form-control",
			"id":"form_mail",
			"placeholder":"Email"
			}))

	designation = forms.CharField(
	widget = forms.TextInput(
		attrs = {
			"class":"form-control",
			"id":"form_mail",
			"placeholder":"Designation"
			}))

	pass1 = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				"class":"form-control",
				"id":"form_pass1",
				"placeholder":"Enter password"
			}))

	##to check if password already exists
	def confirm_password(self):
		password = self.cleaned_data.get('pass1')
		qs = User.objects.filter(password = password)
		print(qs)
		if qs.exists():
			raise forms.ValidationError("Password already exists")
		else:
			return username

	##to check if the email already exists
	def confirm_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email = 'email')
		print(qs)
		if qs.exists():
			raise forms.ValidationError('email already exists')
		else:
			return email

