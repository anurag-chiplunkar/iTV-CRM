from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import *
from .models import *

def nfct_chname(request):
	nfct_form = NFCT_Chann(request.POST or None)

	context = {"nfct_form" : nfct_form}
	print(nfct_form.is_valid())
	print(nfct_form.errors)
	print(request.POST)

	if request.method == "POST":
		if nfct_form.is_valid():
			print(nfct_form.cleaned_data)
			nfct_obj = NFCT_Channels()
			print("inside NFCT")
			nfct_obj.channels = nfct_form.cleaned_data.get('channels')
			print(nfct_obj.channels)

			nfct_obj.save()
		else:
			print("Invalid NFCT")
	return render(request, 'nfct/nfct_channel.html', context)