from django.shortcuts import render,redirect
from .forms import Cust_name,Cust_type,Cust_contacts
from django.contrib.auth.models import User
from .models import CustomerType,CustomerName,CustomerContact


def customer_registration(request):
	form1 = Cust_type(request.POST or None)
	form2 = Cust_name(request.POST or None)
	form3 = Cust_contacts(request.POST or None)
	context = {"form1":form1,"form2":form2,"form3":form3}

	if form1.is_valid():
		# print(form1.cleaned_data)

		ctype = form1.cleaned_data.get('customer_type')
		ct_id = ctype[:4] + '_ctKey'

		obj = CustomerType(customer_type = ctype, ctype_id = ct_id)
		obj.save()
		# myuser = User.objects.create_user(ctype)

	else:
		print("Invalid customer type")


	if form2.is_valid():
		# print(form2.cleaned_data)

		cname = form2.cleaned_data.get('name')
		c_id = cname[:3]+'_cKey'
		customertype = form2.cleaned_data.get('custType')

		obj = CustomerName(name = cname,cust_id = c_id,customertype = customertype)
		obj.save()
		# myuser = User.objects.create_user(cname)

	else:
		print("Invalid customer")



	if form3.is_valid():
		fname = form3.cleaned_data.get('firstName')
		lname = form3.cleaned_data.get('lastName')
		desgn = form3.cleaned_data.get('designation')
		email = form3.cleaned_data.get('email')
		phone = form3.cleaned_data.get('phone')
		cc_id = email[:email.find('@')] + "_ccKey"
		customername = form3.cleaned_data.get('cust_name')

		obj = CustomerContact(firstName = fname,
							lastName = lname,
							designation = desgn,
							email = email,
							phone = phone,
							cc_id = cc_id,
							customername = customername)
		obj.save()

	else:
		print("customer contact form invalid")

	return render(request,'customer/register_cust_custcontact.html',context)










# def customer_name(request):
# 	form = Cust_name(request.POST or None)
# 	context = {"form1":form1}

# 	if form.is_valid():
# 		print(form.cleaned_data)

# 		cname = form.cleaned_data.get('name')
# 		c_id = cname[:3]+'_cKey'
# 		customertype = form.cleaned_data.get('custType')

# 		obj = CustomerName(name = cname,cust_id = c_id,customertype = customertype)
# 		obj.save()
# 		# myuser = User.objects.create_user(cname)

# 	else:
# 		print("Invalid customer")

# 	return render(request,'customer/customer_registration.html',context)		##cust_name


# def customer_contact(request):
# 	form = Cust_contacts(request.POST or None)
# 	context = {"form":form}

# 	if form.is_valid():
# 		fname = form.cleaned_data.get('firstName')
# 		lname = form.cleaned_data.get('lastName')
# 		desgn = form.cleaned_data.get('designation')
# 		email = form.cleaned_data.get('email')
# 		phone = form.cleaned_data.get('phone')
# 		cc_id = email[:email.find('@')] + "_ccKey"
# 		customername = form.cleaned_data.get('cust_name')

# 		obj = CustomerContact(firstName = fname,
# 							lastName = lname,
# 							designation = desgn,
# 							email = email,
# 							phone = phone,
# 							cc_id = cc_id,
# 							customername = customername)
# 		obj.save()

# 	else:
# 		print("customer contact form invalid")

# 	return render(request,'customer/cust_contact_form.html',context)

def cust_info(request):
	qs = CustomerName.objects.all()
	print(qs)
	qs_context = {"qs":qs}

	return render(request,'customer/cust_details_info.html',qs_context)

def cust_contact_info(request):
	qs = CustomerContact.objects.all()
	print(qs)
	qs_context = {"qs":qs}

	return render(request,'customer/cust_contacts_info.html',qs_context)

def cust_type_info(request):
	qs = CustomerType.objects.all()
	print(qs)
	qs_context = {"qs":qs}

	return render(request,'customer/cust_types_info.html',qs_context)