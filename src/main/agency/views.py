from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import *
from . models import *


def agency_registration(request):
	form1 = Agency_details(request.POST or None)
	form2 = Agency_contacts(request.POST or None)
	print(form1)
	context = {"form1":form1,"form2":form2}


	if form1.is_valid():
		print(form1.cleaned_data)
		aname 	= form1.cleaned_data.get('agency_name')
		astate 	= form1.cleaned_data.get('agency_state')
		ag_id 	= aname[0] + "_agKey"
		print(ag_id)

		obj1 = AgencyDetail(agency_name = aname, agency_state = astate, a_id = ag_id)
		obj1.save()

	else:
		print("agency detail form invalid")


	if form2.is_valid():
		fname = form2.cleaned_data.get('firstName')
		lname = form2.cleaned_data.get('lastName')
		desgn = form2.cleaned_data.get('designation')
		email = form2.cleaned_data.get('email')
		phone = form2.cleaned_data.get('phone')
		ac_id = phone[-3:] + "_acKey"
		print(ac_id)

		# agency_details should be equal to a_id
		##this will give a dropdown input for the user to select from which agency he/she is.
		##after the form is submitted the fk anf pk relationship is successfully created
		agency_details = form2.cleaned_data.get('agency')
		print(agency_details)

		obj2 = AgencyContact(firstName = fname,
							lastName = lname,
							designation = desgn,
							email = email,
							phone = phone,
							ac_id = ac_id,
							agency_details = agency_details
							)
		obj2.save()



	else:
		print("agency contact form invalid")

	return render(request,'agency/register_agency_agencycontact.html',context)

# def agency_detail(request):
# 	form1 = Agency_details(request.POST or None)
# 	context1 = {"form1":form1}

# 	if form1.is_valid():
# 		aname 	= form1.cleaned_data.get('agency_name')
# 		astate 	= form1.cleaned_data.get('agency_state')
# 		ag_id 	= aname[0] + "_agKey"
# 		print(ag_id)

# 		obj = AgencyDetail(agency_name = aname, agency_state = astate, a_id = ag_id)
# 		obj.save()

# 	else:
# 		print("agency detail form invalid")
# 	return render(request,'agency/agency_registration.html',context1)    ##agency_detail_form


# def agency_contact(request):
# 	form2 = Agency_contacts(request.POST or None)
# 	context2 = {"form2":form2}

# 	if form2.is_valid():
# 		fname = form2.cleaned_data.get('firstName')
# 		lname = form2.cleaned_data.get('lastName')
# 		desgn = form2.cleaned_data.get('designation')
# 		email = form2.cleaned_data.get('email')
# 		phone = form2.cleaned_data.get('phone')
# 		ac_id = phone[-3:] + "_acKey"
# 		print(ac_id)

# 		# agency_details should be equal to a_id
# 		##this will give a dropdown input for the user to select from which agency he/she is.
# 		##after the form is submitted the fk anf pk relationship is successfully created
# 		agency_details = form2.cleaned_data.get('agency')
# 		print(agency_details)

# 		obj = AgencyContact(firstName = fname,
# 							lastName = lname,
# 							designation = desgn,
# 							email = email,
# 							phone = phone,
# 							ac_id = ac_id,
# 							agency_details = agency_details
# 							)
# 		obj.save()



# 	else:
# 		print("agency contact form invalid")

# 	return render(request,'agency/agency_registration.html',context2)


def agency_info(request):
		qs = AgencyDetail.objects.all()
		print(qs)
		qs_context = {"qs":qs}

		# for i in qs:
		# 	print(i.a_id)

		return render(request,'agency/agency_details.html',qs_context)

def agency_contact_info(request):
	qs = AgencyContact.objects.all()
	print(qs)
	qs_context = {"qs":qs}

	return render(request,'agency/agency_contacts.html',qs_context)