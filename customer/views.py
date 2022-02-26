from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

from .forms import *
from .models import *


def ctype(request):
	form1 = Cust_type(request.POST or None)

	context = {"form1" : form1}
	print(form1.is_valid())
	print(request.POST)

	if request.method == "POST":
		if form1.is_valid():
			print(form1.cleaned_data)
			obj1 = CustomerType()
			print("inside form1")
			obj1.customer_type = form1.cleaned_data.get('customer_type')		#should be same as defined in forms.py
			print(obj1.customer_type)
			obj.save()

		else:
			print("invalid form1")

	return render(request, 'customer/customer_type.html', context)

def cname(request):
	form2 = Cust_name(request.POST or None)
	context = {"form2" : form2}
	print(form2.is_valid())
	print(form2.errors)
	print(request.POST)
	if request.method == "POST":
		if form2.is_valid():
			obj2 = CustomerName()
			print("inside form2")
			obj2.creg_no = form2.cleaned_data.get('creg_no')
			obj2.cname = form2.cleaned_data.get('cname')
			obj2.brand_name = form2.cleaned_data.get('brand_name')
			obj2.ref_customertype = form2.cleaned_data.get('ref_customertype')		#should be same as defined in forms.py
			print(obj2.ref_customertype)
			obj2.save()
			messages.success(request, 'Client name succesfully added')
	
		else:
			print("invalid form2")
	return render(request, 'customer/customer_name.html', context)

def ccontact(request):
	form3 = Cust_contact(request.POST or None)
	# print(form3)

	context = {"form3" : form3}
	print(context)
	print(form3.is_valid())
	print(form3.errors)
	print(request.POST)

	if request.method == "POST":

		if form3.is_valid():
			obj3 = CustomerContact()
			print("inside form3")
			obj3.pri_fname = form3.cleaned_data.get('pri_fname')
			obj3.pri_lname = form3.cleaned_data.get('pri_lname')
			obj3.pri_desg = form3.cleaned_data.get('pri_desg')
			obj3.pri_email  = form3.cleaned_data.get('pri_email')
			obj3.pri_phone = form3.cleaned_data.get('pri_phone')
			obj3.pri_landline = form3.cleaned_data.get('pri_landline')
			obj3.pri_flatno = form3.cleaned_data.get('pri_flatno')
			obj3.pri_streetname = form3.cleaned_data.get('pri_streetname')
			obj3.pri_landmark = form3.cleaned_data.get('pri_landmark')
			obj3.pri_city = form3.cleaned_data.get('pri_city')
			obj3.pri_pincode = form3.cleaned_data.get('pri_pincode')
			
			# print(obj3.ref_cname)

			obj3.sec_fname = form3.cleaned_data.get('sec_fname')
			print(obj3.sec_fname)
			obj3.sec_lname = form3.cleaned_data.get('sec_lname')
			obj3.sec_desg = form3.cleaned_data.get('sec_desg')
			obj3.sec_email  = form3.cleaned_data.get('sec_email')
			obj3.sec_phone = form3.cleaned_data.get('sec_phone')
			obj3.sec_landline = form3.cleaned_data.get('sec_landline')
			obj3.sec_flatno = form3.cleaned_data.get('sec_flatno')
			obj3.sec_streetname = form3.cleaned_data.get('sec_streetname')
			obj3.sec_landmark = form3.cleaned_data.get('sec_landmark')
			obj3.sec_city = form3.cleaned_data.get('sec_city')
			obj3.sec_pincode = form3.cleaned_data.get('sec_pincode')

			obj3.ref_creg_no = form3.cleaned_data.get('ref_creg_no')

			obj3.save()
			messages.success(request, 'Client Contact succesfully added')

		else:
			print("invalid form3")
	return render(request, 'customer/customer_contact.html', context)






