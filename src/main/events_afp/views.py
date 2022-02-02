from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# import requests
from django.shortcuts import redirect

from .forms import *

from .models import *

def afp_pname(request):
	form1 = AFP_Progname(request.POST or None)

	context = {"form1" : form1}
	print(form1.is_valid())
	print(form1.errors)
	print(request.POST)

	if request.method == "POST":
		if form1.is_valid():
			print(form1.cleaned_data)
			obj1 = AFP_ProgramName()
			print("inside form1")
			obj1.program_name = form1.cleaned_data.get('program_name')
			print(obj1.program_name)

			obj1.save()
		else:
			print("Invalid Form1")
	return render(request, 'events_afp/afp.html', context)


def afp_chname(request):
	form2 = AFP_Chann(request.POST or None)

	context = {"form2" : form2}
	print(form2.is_valid())
	print(form2.errors)
	print(request.POST)

	if request.method == "POST":
		if form2.is_valid():
			print(form2.cleaned_data)
			obj2 = AFP_Channels()
			print("inside form2")
			obj2.channels = form2.cleaned_data.get('channels')
			print(obj2.channels)

			obj2.save()
		else:
			print("Invalid Form2")
	return render(request, 'events_afp/afp2.html', context)

def afp_deal(request):
	form3 = AFP_dealform(request.POST or None)
	form5 = Events_dealform(request.POST or None)


	context = {"form3" : form3, "form5" : form5}
	print(form3.is_valid())
	print(form3.errors)
	print(request.POST)

	print(form5.is_valid())
	print(form5.errors)
	print(request.POST)

	if request.method == "POST":
		if form3.is_valid():
			print(form3.cleaned_data)
			obj3 = AFP_Deal()
			print("inside form3")
			obj3.ref_program_name = form3.cleaned_data.get('ref_program_name')
			obj3.ref_channels = form3.cleaned_data.get('ref_channels')
			obj3.promos = form3.cleaned_data.get('promos')
			obj3.slot = form3.cleaned_data.get('slot')
			obj3.eff_rate = form3.cleaned_data.get('eff_rate')
			obj3.save()
		else:
			print('Invalid Form3')
	if request.method == "POST":
		if form5.is_valid():
			print(form5.cleaned_data)
			obj5 = Events_Deal()
			print("inside form5")
			obj5.ref_category_name = form5.cleaned_data.get('ref_category_name')
			obj5.description = form5.cleaned_data.get('description')
			obj5.ref_channels = form5.cleaned_data.get('ref_channels')
			obj5.amount = form5.cleaned_data.get('amount')
			obj5.merit_money = form5.cleaned_data.get('merit_money')

			obj5.save()
		else:
			print('Invalid form5')

	return render(request, 'events_afp/afp_deal.html', context)

def cat_name(request):
	form4 = Events_catname(request.POST or None)

	context = {"form4" : form4}
	print(form4.is_valid())
	print(form4.errors)
	print(request.POST)

	if request.method == "POST":
		if form4.is_valid():
			print(form4.cleaned_data)
			obj4 = Events_Category()
			print("inside form4")
			obj4.category_name = form4.cleaned_data.get('category_name')
			print(obj4.category_name)

			obj4.save()
		else:
			print("Invalid Form4")
	return render(request, 'events_afp/Events_Category.html', context)

# def event_deal(request):
# 	form5 = Events_dealform(request.POST or None)

# 	context = {"form5" : form5}
# 	print(form5.is_valid())
# 	print(form5.errors)
# 	print(request.POST)

# 	if request.method == "POST":
# 		if form5.is_valid():
# 			print(form5.cleaned_data)
# 			obj5 = Events_Deal()
# 			print("inside form5")
# 			obj5.ref_category_name = form5.cleaned_data.get('ref_category_name')
# 			obj5.description = form5.cleaned_data.get('description')
# 			obj5.ref_channels = form5.cleaned_data.get('ref_channels')
# 			obj5.amount = form5.cleaned_data.get('amount')
# 			obj5.merit_money = form5.cleaned_data.get('merit_money')

# 			obj5.save()
# 		else:
# 			print('Invalid form5')

# 	return render(request, 'events_afp/afp_deal.html', context)
