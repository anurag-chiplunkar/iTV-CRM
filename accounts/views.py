from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,get_user_model
from .forms import *
from . models import *

def emp_registration(request):
	form = Employee_registration(request.POST or None)
	context = {"form":form}
	print(request.POST)
 
	if form.is_valid():
		emp_fname 			= form.cleaned_data.get('emp_fname')
		emp_lname 			= form.cleaned_data.get('emp_lname')
		emp_email 			= form.cleaned_data.get('emp_email')
		emp_phone 			= form.cleaned_data.get('emp_phone')
		emp_desgn 			= form.cleaned_data.get('jobtitle')
		emp_reporting_mgr 	= form.cleaned_data.get('emp_reporting_mgr')

		emp_pass1			= form.cleaned_data.get('emp_pass1')

		obj = Employees(emp_fname = emp_fname,
							emp_lname = emp_lname,
							emp_email = emp_email,
							emp_phone = emp_phone,
							emp_desgn = emp_desgn,
							emp_reporting_mgr = emp_reporting_mgr
							)

		obj.save()
		myuser = User.objects.create_user(emp_email[:emp_email.find('@')],emp_email,emp_pass1) 	##email before the '@' is saved as username in django backend
		return redirect('/emp_login')



	else:
		print("employee registration form invalid")

	return render(request,'accounts/emp_registration.html',context)


def emp_login(request):
	form = Employee_login(request.POST or None)
	context = {"form":form}

	if form.is_valid():
		print('login form is valid')
		print(form.cleaned_data)
		email = form.cleaned_data.get('emp_email')
		username = email[:email.find('@')]
		password = form.cleaned_data.get('emp_pass1')
		# print(username,'********')

		user = authenticate(request,username = username, password = password)
		print(user)

		if user is not None:
			login(request,user)
			print(request.user)
			print('You are logged in')

			qs1 = Employees.objects.filter(emp_email=email)
			qs_context = {"qs":qs1}

			for i in qs_context['qs']:
				designation = i.emp_desgn

			if designation == "Admin":
				return render(request,'profiles/admin_profile.html',qs_context)
			
			else:
				return render(request,'accounts/error_page.html')

	return render(request,'accounts/emp_login.html',context)