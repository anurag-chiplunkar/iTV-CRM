from django.shortcuts import render,redirect
from accounts.models import Employees
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib import messages
from accounts.views import emp_registration

def profile(request):
	user = request.user.email
	print(user,"*********")

	qs1 = Employees.objects.filter(emp_email__contains=user)

	print(qs1)

	context = {"qs":qs1}

	return render(request,'profiles/profile.html',context)

def logout_view(request):
	logout(request)
	messages.success(request,'You are logged out!!')
	print('LOGGED OUT!!!!!!!!!!!!!')
	return redirect('/')
