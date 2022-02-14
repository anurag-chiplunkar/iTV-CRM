from django.shortcuts import render,redirect
from accounts.models import Employees
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout

def profile(request):
	user = request.user
	# print(user,"*********")
	qs1 = Employees.objects.filter(emp_email__contains=user)
	print(qs1)

	context = {"qs":qs1}

	return render(request,'profiles/profile.html',context)

def logout_view(request):
	logout(request)
	print('LOGGED OUT!!!!!!!!!!!!!')
	return redirect('/emp_login')
