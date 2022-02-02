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
	master = base.objects.all()
	context = {'master':master}
	return render(request,'deal_fct_nonfct/fct.html',context)

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
