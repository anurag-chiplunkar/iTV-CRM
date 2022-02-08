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