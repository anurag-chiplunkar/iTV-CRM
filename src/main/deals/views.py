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

def register_base_rate(request):
	form = BaseRateForm(request.POST or None)
	context = {"form":form}

	if request.method == "POST":
		print(request.POST)

		if form.is_valid():
			channel_choice = form.cleaned_data.get('channel_choice')
			element_choice = form.cleaned_data.get('element_choice')
			print(element_choice,type(element_choice))
			key = str(channel_choice)+str(element_choice)
			print(key)
			br 	= form.cleaned_data.get('base_rate')

			obj = BaseRateNFCT(base_rate = br,unique_key = key)
			obj.save()

		else:
			print("base rate form invalid")
	return render(request,'deals/baserates.html',context)


def register_deal(request):
	form = DealForm(request.POST or None)
	context = {"form":form}

	if request.method == "POST":
		print(request.POST)

		if form.is_valid():
			eff_rate 	= form.cleaned_data.get('eff_rate')
			frequency 	= form.cleaned_data.get('frequency')
			# total_sec 	= form.cleaned_data.get('total_sec')
			total_cost 	= form.cleaned_data.get('total_cost')

			channel_choice = form.cleaned_data.get('channel_choice')
			element_choice = form.cleaned_data.get('element_choice')

			obj = DealNFCT(eff_rate = eff_rate, frequency = frequency, total_sec = total_sec, total_cost = total_cost, base_rate = base_rate)
			obj.save()

		else:
			print("deal form invalid")
	return render(request,'deals/nfct_deal.html',context)

def load_br(request):
	print("Our resquest",request.GET)
	ch = request.GET.get('channel_choice')
	print(ch)

	selected_channel = ChannelNFCT.objects.filter(channel__contains = ch)
	print(selected_channel)

	sc = {"qs":selected_channel}
	for i in sc["qs"]:
		c1 = i.channel
		print(c1)

	ele = request.GET.get('checkbox1')
	elem = ele.title()
	print(elem)
	
	# selected_ele = ElementNFCT.objects.filter(element__contains = elem)
	# print(selected_ele)

	# se = {"qs":selected_ele}
	# for j in se["qs"]:
	# 	e1 = i.element
	# 	print(e1)

	x = ch+'Aston Band'
	print(x)

	selected_baserate = BaseRateNFCT.objects.filter(unique_key__contains = x)
	for k in selected_baserate:
		rate = k.base_rate
		print(rate)
	return render(request,'deals/nfct_deal.html',{'rate': rate})
