from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . models import Prod
from . forms import Products

# Create your views here.

def products(request):
	form = Products(request.POST or None)
	context = {"form" : form}

	if form.is_valid():
		print(form.cleaned_data)

		disps = form.cleaned_data.get('disp')
		b = form.cleaned_data.get('band')
		base = form.cleaned_data.get('base_rate')
		eff = form.cleaned_data.get('eff_rate')
		other_disp = form.cleaned_data.get('other_dispersion')

		obj = Prod(dispersion = disps, bands = b, base_rate = base, effective_rate = eff, other_dispersion = other_disp)
		obj.save()

	else:
		print('INVALID FORM!')

	return render(request, 'products/product.html', context)
