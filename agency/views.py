from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import *
from . models import *

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
				if apin.isdigit() == False:
					messages.error(request,"Enter a valid pincode")

				if aname.isalpha() and apin.isdigit() == True :
					obj1 = AgencyDetail(agency_name = aname,
									agency_officeno = aofficeno,
									agency_street = astreet,
									agency_state = astate,
									agency_landmark = alandmark,
									agency_city = acity,
									agency_pin = apin,
									a_id = ag_id)
					obj1.save()

				else:
					messages.error(request,"Agency Name Cannot be a number")

			except IntegrityError:
				messages.error(request,"Agency already exists!")



				

		else:
			print("agency detail form invalid")
	return render(request,'agency/agency_detail_form.html',context1) 



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



	else:
		print("agency contact form invalid")

	return render(request,'agency/agency_contact_form.html',context2)


def agency_info(request):
		qs = AgencyDetail.objects.all()
		print(qs)
		qs_context = {"qs":qs}

		return render(request,'agency/agency_details.html',qs_context)

def agency_contact_info(request):
	qs = AgencyContact.objects.all()
	print(qs)
	qs_context = {"qs":qs}

	return render(request,'agency/agency_contacts.html',qs_context)