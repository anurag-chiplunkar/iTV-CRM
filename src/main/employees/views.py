from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import Emp_signup, Emp_login
from . models import Employees

def emp_signup(request):
	form = Emp_signup(request.POST or None)
	context = {"form":form}

	if form.is_valid():
		print(form.cleaned_data)

		# username = form.cleaned_data.get('username')
		fname = form.cleaned_data.get('firstName')
		lname = form.cleaned_data.get('lastName')
		desgn = form.cleaned_data.get('designation')
		dept  = form.cleaned_data.get('department')
		email = form.cleaned_data.get('email')
		phone = form.cleaned_data.get('phone')
		password = form.cleaned_data.get('pass1')

		username = email[:email.find('@')]
		# print(username)

		obj = Employees(username = username,
						firstName = fname,
						lastName = lname,
						designation = desgn,
						department = dept,
						email = email,
						phone = phone,
						)
		obj.save()
		myuser = User.objects.create_user(username,email,password)
		# print(myuser.password)

		return redirect('/emp_login')

	else:
		print('INVALID FORM!')

	return render(request,'employees/emp_signup.html', context)


def emp_login(request):
	form = Emp_login(request.POST or None)
	context = {"form":form}
	print(request.user.is_authenticated)

	if form.is_valid():
		print(form.cleaned_data)

		email = form.cleaned_data.get('email')
		desgn = form.cleaned_data.get('designation')
		password = form.cleaned_data.get('pass1')

		user = authenticate(request, email = email, password = password)
		print(user)

		if user is not None:
			if "sales" or "Sales" in desgn:
				login(request,user)
				print(request.user)
				return redirect('/agency_details_form')
			else:
				print("This is not a salesperson")

		else:
			print('invalid login')

	return render(request,'employees/emp_login.html',context)

