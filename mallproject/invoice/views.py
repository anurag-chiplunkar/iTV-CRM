from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
import requests
from django.shortcuts import redirect
from django.contrib import messages

from .forms import *
from .models import *

# Create your views here.

def home(request):
	form = generatebill(request.POST or None)
	
	print(request.POST)
	print(form.is_valid())
	print(form.errors)
	if request.method == "POST":
		if form.is_valid():
			obj = bill()
			print("inside")
			obj.cust_name = form.cleaned_data.get('cust_name')
			obj.phone = form.cleaned_data.get('phone')
			obj.items = request.POST.get('item')
			obj.price_unit = request.POST.get('price')
			obj.quantity = request.POST.get('quan')
			obj.total = request.POST.get('total')
			obj.amt = request.POST.get('amt')
			obj.save()
			messages.success(request,"Bill is saved!!!!")
		return redirect(reverse('home'))
		# return http.HttpResponseRedirect('home')
			
		
	else:
			# form = generatebill()
		context = {'form':form}
		print("invalid")
		return render(request, 'home.html',context)

		
