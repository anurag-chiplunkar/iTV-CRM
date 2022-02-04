from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import *
from . models import *

def register_channel(request):
	form = ChannelForm(request.POST or None)
	context = {"form":form}

	if request.method == "POST":
		print(request.POST)

		if form.is_valid():
			c 	= form.cleaned_data.get('channel')
			obj = ChannelNFCT(channel = c)
			obj.save()

		else:
			print("channel form invalid")
	return render(request,'deals/channels.html',context)

def register_element(request):
	form = ElementForm(request.POST or None)
	context = {"form":form}

	if request.method == "POST":
		print(request.POST)

		if form.is_valid():
			e 	= form.cleaned_data.get('element')
			obj = ElementNFCT(element = e)
			obj.save()

		else:
			print("element form invalid")
	return render(request,'deals/elements.html',context)


def register_deal(request):
	form = DealForm(request.POST or None)
	context = {"form":form}

	if request.method == "POST":
		print(request.POST)

		if form.is_valid():
			eff_rate 	= form.cleaned_data.get('eff_rate')
			frequency 	= form.cleaned_data.get('frequency')
			total_sec 	= form.cleaned_data.get('total_sec')
			total_cost 	= form.cleaned_data.get('total_cost')

			channel_choice = form.cleaned_data.get('channel_choice')
			element_choice = form.cleaned_data.get('element_choice')

			obj = DealNFCT(eff_rate = eff_rate, frequency = frequency, total_sec = total_sec, total_cost = total_cost)
			obj.save()

		else:
			print("deal form invalid")
	return render(request,'deals/nfct_deal.html',context)
