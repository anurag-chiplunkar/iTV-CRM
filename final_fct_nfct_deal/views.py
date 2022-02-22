from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db import IntegrityError
from .forms import *
from .models import *
from agency.models import *
from customer.models import *
from accounts.models import Employees
from nfct.models import *
import random
import json
from django.core import serializers
from django.contrib.auth.models import User

def final_deal(request):
    form = FinalFctNfctDealDetails(request.POST or None)
    user = request.user
    ag_det = AgencyDetail.objects.all()
    cli_name = CustomerName.objects.all()
    cli_det = CustomerContact.objects.all()
    agg = AgencyContact.objects.all()
    qs1 = Employees.objects.filter(emp_email__contains=user)
    tmpJson = serializers.serialize("json",cli_det)
    tmpagen = serializers.serialize("json",agg)
    
    context = {'form': form,'ag_det':ag_det,'cli_name':cli_name,'cli_det':cli_det,'agg':agg,'tmpJson':tmpJson,'qs':qs1,'tmpagen':tmpagen }
    # context = {"form" : form}

    if request.method == "POST":
        if form.is_valid():
            fct_total   = form.cleaned_data.get('fct_total')
            nfct_total  = form.cleaned_data.get('nfct_total')
            grand_total = form.cleaned_data.get('grand_total')
            client_name_ref     = form.cleaned_data.get('client_name_ref')
            client_contact_ref  = form.cleaned_data.get('client_contact_ref')
            agency_name_ref     = form.cleaned_data.get('agency_name_ref')
            agency_contact_ref  = form.cleaned_data.get('agency_contact_ref')
            brand_name_ref = form.cleaned_data.get('brand_name_ref')

            try:
                deal_id = random.randint(1,100)
                print(deal_id)
            except IntegrityError:
                deal_id = random.randint(101,200)
                print(deal_id)
        else:
            print("Form is invalid")

    return render(request,"final_fct_nfct_deal/final_fct_nfct_deal.html",context)
