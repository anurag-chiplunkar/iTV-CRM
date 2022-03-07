from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import *
from . models import *
from django.http import HttpResponse


def agency_detail(request):
	form1 = Agency_details(request.POST or None)
	context1 = {"form1":form1}

	if request.method == "POST":
		print(request.POST)

		if form1.is_valid():
			aname 		= form1.cleaned_data.get('agency_name')
			aofficeno 	= form1.cleaned_data.get('agency_officeno')
			astreet 	= form1.cleaned_data.get('agency_street')
			astate 		= form1.cleaned_data.get('agency_state')
			alandmark 	= form1.cleaned_data.get('agency_landmark')
			acity 		= form1.cleaned_data.get('agency_city')
			apin 		= form1.cleaned_data.get('agency_pin')
			
			##generating primary key
			if ' ' in aname:
				ag_name = aname.split(' ')
				ag_id 	= ''.join([str(i[0]) for i in ag_name]) + '_' + astate
				print(ag_id)

			else:
				ag_id 	= aname + '_' + astate
				print(ag_id)

			##checking if the agency already exists and agency is not a number
			try:
				a = int(aname)
				messages.error(request,"Enter a valid Agency Name")
			except ValueError:
				obj1 = AgencyDetail(agency_name = aname,
									agency_officeno = aofficeno,
									agency_street = astreet,
									agency_state = astate,
									agency_landmark = alandmark,
									agency_city = acity,
									agency_pin = apin,
									a_id = ag_id)
				obj1.save()

				# obj1.customernames.add()
				messages.success(request,"Agency added successfully")
		
			except IntegrityError:
				messages.error(request,"This Agency Already Exists")

		else:
			print("agency detail form invalid")
	return render(request,'agency_client/agency_detail_form.html',context1) 



def agency_contact(request):
	form2 = Agency_contacts(request.POST or None)
	context2 = {"form2":form2}

	if form2.is_valid():
			pri_fname 		= form2.cleaned_data.get('pri_firstName')
			pri_lname 		= form2.cleaned_data.get('pri_lastName')
			pri_desgn 		= form2.cleaned_data.get('pri_designation')
			pri_email 		= form2.cleaned_data.get('pri_email')
			pri_phone 		= form2.cleaned_data.get('pri_phone')
			pri_landline  	= form2.cleaned_data.get('pri_landline')
			pri_flatno  	= form2.cleaned_data.get('pri_flatno')
			pri_street 		= form2.cleaned_data.get('pri_street')
			pri_landmark 	= form2.cleaned_data.get('pri_landmark')
			pri_city 		= form2.cleaned_data.get('pri_city')
			pri_pin 		= form2.cleaned_data.get('pri_pin')

			sec_fname 		= form2.cleaned_data.get('sec_firstName')
			sec_lname 		= form2.cleaned_data.get('sec_lastName')
			sec_desgn 		= form2.cleaned_data.get('sec_designation')
			sec_email 		= form2.cleaned_data.get('sec_email')
			sec_phone 		= form2.cleaned_data.get('sec_phone')
			sec_landline  	= form2.cleaned_data.get('sec_landline')
			sec_flatno  	= form2.cleaned_data.get('sec_flatno')
			sec_street 		= form2.cleaned_data.get('sec_street')
			sec_landmark 	= form2.cleaned_data.get('sec_landmark')
			sec_city 		= form2.cleaned_data.get('sec_city')
			sec_pin 		= form2.cleaned_data.get('sec_pin')
	

			##this will give a dropdown input for the user to select from which agency he/she is.
			##after the form is submitted the fk anf pk relationship is successfully created
			agency_details = form2.cleaned_data.get('agency')
			print(agency_details)

			obj2 = AgencyContact(pri_firstName = pri_fname,
								pri_lastName = pri_lname,
								pri_designation = pri_desgn,
								pri_email = pri_email,
								pri_phone = pri_phone,
								pri_landline = pri_landline,
								pri_flatno = pri_flatno,
								pri_street = pri_street,
								pri_landmark = pri_landmark,
								pri_city = pri_city,
								pri_pin = pri_pin,

								sec_firstName = sec_fname,
								sec_lastName = sec_lname,
								sec_designation = sec_desgn,
								sec_email = sec_email,
								sec_phone = sec_phone,
								sec_landline = sec_landline,
								sec_flatno = sec_flatno,
								sec_street = sec_street,
								sec_landmark = sec_landmark,
								sec_city = sec_city,
								sec_pin = sec_pin,

								agency_details = agency_details
								)
			obj2.save()
			messages.success(request,"Agency Contact successfully added")



	else:
		print("agency contact form invalid")

	return render(request,'agency_client/agency_contact_form.html',context2)


# def agency_info(request):
# 		qs = AgencyDetail.objects.all()
# 		print(qs)
# 		qs_context = {"qs":qs}

# 		return render(request,'agency_client/agency_details.html',qs_context)

# def agency_contact_info(request):
# 	qs = AgencyContact.objects.all()
# 	print(qs)
# 	qs_context = {"qs":qs}

# 	return render(request,'agency_client/agency_contacts.html',qs_context)






def ctype(request):
	form3 = Cust_type(request.POST or None)

	context = {"form3" : form3}
	print(form3.is_valid())
	print(request.POST)

	if request.method == "POST":
		if form3.is_valid():
			print(form3.cleaned_data)
			obj1 = CustomerType()
			print("inside form3")
			obj1.customer_type = form3.cleaned_data.get('customer_type')		#should be same as defined in forms.py
			print(obj1.customer_type)
			obj1.save()

		else:
			print("invalid form3")

	return render(request, 'agency_client/customer_type.html', context)

def cname(request):
	form4 = Cust_name(request.POST or None)
	context = {"form4" : form4}
	print(form4.is_valid())
	print(form4.errors)
	print(request.POST)
	if request.method == "POST":
		if form4.is_valid():
			obj2 = CustomerName()
			print("inside form4")
			obj2.creg_no = form4.cleaned_data.get('creg_no')
			obj2.cname = form4.cleaned_data.get('cname')
			obj2.brand_name = form4.cleaned_data.get('brand_name')
			obj2.ref_customertype = form4.cleaned_data.get('ref_customertype')		#should be same as defined in forms.py
			print(obj2.ref_customertype)
			obj2.save()
			messages.success(request, 'Client name succesfully added')
	
		else:
			print("invalid form4")
	return render(request, 'agency_client/customer_name.html', context)

def ccontact(request):
	form5 = Cust_contact(request.POST or None)
	# print(form3)

	context = {"form5" : form5}
	print(context)
	print(form5.is_valid())
	print(form5.errors)
	print(request.POST)

	if request.method == "POST":

		if form5.is_valid():
			obj3 = CustomerContact()
			print("inside form5")
			obj3.pri_fname = form5.cleaned_data.get('pri_fname')
			obj3.pri_lname = form5.cleaned_data.get('pri_lname')
			obj3.pri_desg = form5.cleaned_data.get('pri_desg')
			obj3.pri_email  = form5.cleaned_data.get('pri_email')
			obj3.pri_phone = form5.cleaned_data.get('pri_phone')
			obj3.pri_landline = form5.cleaned_data.get('pri_landline')
			obj3.pri_flatno = form5.cleaned_data.get('pri_flatno')
			obj3.pri_streetname = form5.cleaned_data.get('pri_streetname')
			obj3.pri_landmark = form5.cleaned_data.get('pri_landmark')
			obj3.pri_city = form5.cleaned_data.get('pri_city')
			obj3.pri_pincode = form5.cleaned_data.get('pri_pincode')
			
			# print(obj3.ref_cname)

			obj3.sec_fname = form5.cleaned_data.get('sec_fname')
			print(obj3.sec_fname)
			obj3.sec_lname = form5.cleaned_data.get('sec_lname')
			obj3.sec_desg = form5.cleaned_data.get('sec_desg')
			obj3.sec_email  = form5.cleaned_data.get('sec_email')
			obj3.sec_phone = form5.cleaned_data.get('sec_phone')
			obj3.sec_landline = form5.cleaned_data.get('sec_landline')
			obj3.sec_flatno = form5.cleaned_data.get('sec_flatno')
			obj3.sec_streetname = form5.cleaned_data.get('sec_streetname')
			obj3.sec_landmark = form5.cleaned_data.get('sec_landmark')
			obj3.sec_city = form5.cleaned_data.get('sec_city')
			obj3.sec_pincode = form5.cleaned_data.get('sec_pincode')

			obj3.ref_creg_no = form5.cleaned_data.get('ref_creg_no')

			obj3.save()
			messages.success(request, 'Client Contact succesfully added')

		else:
			print("invalid form5")
	return render(request, 'agency_client/customer_contact.html', context)






