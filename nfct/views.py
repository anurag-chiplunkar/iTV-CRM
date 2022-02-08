from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import *
from .models import *

# Add Channel Names
def nfct_chname(request):
	nfct_chan_form = NFCT_Chann(request.POST or None)

	context = {"nfct_chan_form" : nfct_chan_form}
	print(nfct_chan_form.is_valid())
	print(nfct_chan_form.errors)
	print(request.POST)

	if request.method == "POST":
		if nfct_chan_form.is_valid():
			print(nfct_chan_form.cleaned_data)
			nfct_chan_obj = NFCT_Channels()
			print("inside NFCT")
			nfct_chan_obj.nfct_channels = nfct_chan_form.cleaned_data.get('nfct_channels')
			print(nfct_chan_obj.nfct_channels)
			if NFCT_Channels.objects.filter(nfct_channels = 'nfct_channels').exists():
				ValidationError("Channel Already Exists")
			else:
				nfct_chan_obj.save()
		else:
			print("Invalid NFCT")
	return render(request, 'nfct/nfct_channel.html', context)

# Add Element Names
def nfct_elename(request):
	nfct_ele_form = NFCT_Elem(request.POST or None)

	context = {"nfct_ele_form" : nfct_ele_form}
	print(nfct_ele_form.is_valid())
	print(nfct_ele_form.errors)
	print(request.POST)

	if request.method == "POST":
		if nfct_ele_form.is_valid():
			print(nfct_ele_form.cleaned_data)
			nfct_ele_obj = NFCT_Elements()
			print("inside NFCT Elements")
			nfct_ele_obj.nfct_elements = nfct_ele_form.cleaned_data.get('nfct_elements')
			print(nfct_ele_obj.nfct_elements)
			if NFCT_Elements.objects.filter(nfct_elements = 'nfct_elements').exists():
				ValidationError("Element Already Exists")
			else:
				nfct_ele_obj.save()
		else:
			print("Invalid NFCT Elements")
	return render(request, 'nfct/nfct_element.html', context)


# Add Base rates
def nfct_enter_base_rate(request):
	nfct_form = NFCT_Base_Rate_Form(request.POST or None)
	nfct_obj = NFCT_Base_Rate()
	context = {'nfct_form':nfct_form}
	print(nfct_form.errors)
	print(request.POST)
	if request.method == 'POST':
		if nfct_form.is_valid():
			nfct_channels = nfct_form.cleaned_data.get('nfct_channels')
			# print(nfct_channels)

			nfct_elements = nfct_form.cleaned_data.get('nfct_elements')
			# print(nfct_elements)
			nfct_obj.nfct_baserate = nfct_form.cleaned_data.get('nfct_baserate')

			uni = str(nfct_channels) + str(nfct_elements)
			print(uni)
			nfct_obj.nfct_unique_key = uni

			print("----------",nfct_channels,nfct_elements,nfct_obj.nfct_baserate)
			print(request.POST, '*********************************')
			nfct_obj.save()

	return render(request,'nfct/nfct_base.html',context)

# NFCT Deal form
def nfct_deal_form(request):
	nfct_deal = NFCT_deal(request.POST or None)
	context = {'nfct_deal' : nfct_deal}
	print(nfct_deal.is_valid())
	print(nfct_deal.errors)
	print(request.POST)

	if request.method == 'POST':
		if nfct_deal.is_valid():
			# def incrementor():
			# 	info = {"count": 0000000000}
			# 	def number():
			# 		info["count"] += 1
			# 		return info["count"]
			# 	return number

			# nfct_refrenece_no = incrementor()
			
			durations = nfct_deal.cleaned_data.get('durations')
			duration_in = nfct_deal.cleaned_data.get('duration_in')
			effective_rate = nfct_deal.cleaned_data.get('effective_rate')
			frequency =nfct_deal.cleaned_data.get('frequency')
			total_seconds =nfct_deal.cleaned_data.get('total_seconds')
			base_rate = nfct_deal.cleaned_data.get('base_rate')
			nfct_total = nfct_deal.cleaned_data.get('nfct_total')

			nfct_deal.save()

	return render(request, 'nfct/nfct_deal.html', context)
