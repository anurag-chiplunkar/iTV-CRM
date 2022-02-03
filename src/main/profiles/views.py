from django.shortcuts import render
from accounts.models import Employees

def profile(request):
	user = request.user
	qs1 = Employees.objects.filter(emp_fname=user)
	print(qs1)

	context = {"qs":qs1}

	return render(request,'profiles/emp_profile.html',context)