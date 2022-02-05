from django.shortcuts import render
import json
# Create your views here.

from django.http import HttpResponse
import requests
from django.shortcuts import redirect
from django.contrib import messages
from .forms import *
from .models import *

def home(request):
	return render(request,'home.html')

def fct_details(request):
	# master = base.objects.all()
	# context = {'master':master}
	return render(request,'deal_fct_nonfct/fct.html')

def br_details(request):
	form = base_form(request.POST or None)
	obj = base()
	print("---------------------",request.POST,form.is_valid(),form.errors)
	
	# print("***********",master)
	context = {'form':form,}
	if request.method == "POST":
		if form.is_valid():
			# obj.date = form.cleaned_data['date']
			obj.channel = request.POST.get('channel_list')
			obj.dispersion = request.POST.get('dis_list')
			obj.bands = request.POST.get('bands_list')
			obj.br = request.POST.get('base_rate')
			obj.save()
			messages.success(request, 'Base rate added!!')
			print("inside!!!!!!!!")

	return render(request,'deal_fct_nonfct/base_rate.html',context)

def enter_channels(request):
	form = channel_form(request.POST or None)
	ch_obj = Channel()
	context = {'form': form,}
	print("////////////",request.POST)
	if request.method == 'POST':
		if form.is_valid():
			ch_obj.c_list = form.cleaned_data.get('c_list')
			ch_obj.save()
			print("inside channel views-----")
		else:
			print("outside view")
	return render(request,'deal_fct_nonfct/channel.html',context)

def enter_disper(request):
	form = disper_form(request.POST or None)
	dis_obj = Disper()
	context = {'form': form,}
	print("////////////",request.POST)
	if request.method == 'POST':
		if form.is_valid():
			dis_obj.dis_list = form.cleaned_data.get('dis_list')
			dis_obj.save()
			print("inside dispersion views-----")
		else:
			print("outside view")
	return render(request,'deal_fct_nonfct/dispersion.html',context)

def enter_band(request):
	form = band_form(request.POST or None)
	band_obj = Band()
	context = {'form': form,}
	print("////////////",request.POST)
	if request.method == 'POST':
		if form.is_valid():
			band_obj.b_list = form.cleaned_data.get('b_list')
			band_obj.save()
			print("inside band views-----")
		else:
			print("outside view")
	return render(request,'deal_fct_nonfct/band.html',context)

def enter_base_rate(request):
	form = base_rate_table_form(request.POST or None)
	b_obj = base_rate_table()
	context = {'form':form}
	print(form.errors)
	if request.method == 'POST':
		if form.is_valid():
			chan = request.POST.get('channel')
			bd = request.POST.get('band')
			b_obj.br = form.cleaned_data.get('br')

			uni = chan + bd[:2]
			b_obj.unique_key = uni

			print("----------",uni,chan,bd,b_obj.br)
			b_obj.save()

	return render(request,'deal_fct_nonfct/base.html',context)


def load_br(request):
	chan_id = request.GET.get('channel')
	band1 = request.GET.get('band1')
	print("9999",chan_id,band1)
	rates = Channel.objects.filter(c_list__contains=chan_id)
	b1 = Band.objects.filter(b_list__contains=band1)
	context1 = {'qs':rates}
	context2 = {'qs1':b1}
	for i in context1['qs']:
		c = i.c_list
		print("------",c)

	for j in context2['qs1']:
		b = j.b_list[:2]
		print("---****---",b)
	x = c + b 
	print("*************",x)
	y = base_rate_table.objects.filter(unique_key=x)
	for k in y:
		rate = k.br
		print(rate)
	# r = {'rate': rate}
	# print("******************",r)
	return render(request,'deal_fct_nonfct/fct.html',{'rate': rate})