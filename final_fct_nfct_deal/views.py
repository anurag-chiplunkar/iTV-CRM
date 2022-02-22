from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db import IntegrityError
from .forms import *
from .models import *
import random

def final_deal(request):
    form = FinalFctNfctDealDetails(request.POST or None)
    context = {"form" : form}

    if request.method == "POST":
		if form.is_valid():
            fct_total   = form.cleaned_data.get('fct_total')
            nfct_total  = form.cleaned_data.get('nfct_total')
            grand_total = form.cleaned_data.get('grand_total')

            client_name_ref     = form.cleaned_data.get('client_name_ref')
            client_contact_ref  = form.cleaned_data.get('client_contact_ref')
            agency_name_ref     = form.cleaned_data.get('agency_name_ref')
            agency_contact_ref  = form.cleaned_data.get('agency_contact_ref')

            try:
                deal_id = random.randint(1,100)
                print(deal_id)
            except IntegrityError:
                deal_id = random.randint(101,200)
                print(deal_id)

