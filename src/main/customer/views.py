from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# import requests
from django.shortcuts import redirect

from .forms import *

from .models import *


def cust_reg(request):
	form1 = Cust_type(request.POST or None)
	form2 = Cust_name(request.POST or None)
	form3 = Cust_contact(request.POST or None)

	context = {"form1" : form1, "form2" : form2, "form3" : form3}
	print(form1.is_valid())
	print(form1.errors)
	print(request.POST)

	if request.method == "POST":
		if form1.is_valid():
			print(form1.cleaned_data)
			obj1 = CustomerType()
			print("inside form1")
			obj1.customer_type = form1.cleaned_data.get('customer_type')		#should be same as defined in models.py
			print(obj1.customer_type)

			obj1.save()
			# return redirect(reverse('cust_reg'))
		else:
			print("invalid form1")

		if form2.is_valid():
			obj2 = CustomerName()
			print("inside form2")
			obj2.cust_name = form2.cleaned_data.get('cust_name')
			obj2.cust_type = request.POST.get('cust_type')

			obj2.save()

		else:
			print("invalid form2")


		if form3.is_valid():
			obj3 = CustomerContact()
			print("inside form3")
			obj3.fname = form3.cleaned_data.get('fname')
			obj3.lname = form3.cleaned_data.get('lname')
			obj3.desg = form3.cleaned_data.get('desg')
			obj3.email  = form3.cleaned_data.get('email')
			obj3.phone = form3.cleaned_data.get('phone')

			obj3.save()

		else:
			print("invalid form3")
	return render(request, 'customer/customer_type.html', context)





