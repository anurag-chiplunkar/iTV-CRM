from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.db import IntegrityError
from .forms import *
from .models import *
from agency_client.models import *
from accounts.models import Employees
from nfct.models import *
from nfct.forms import *
from deal_fct_nonfct.models import *
from deal_fct_nonfct.forms import *
import random
import json
from django.core import serializers
from django.contrib.auth.models import User

def final_deal(request):
    form = FinalFctNfctDealDetails(request.POST or None)
    form1 = form_fct_deal(request.POST or None)
    formset = DealModelFormset(request.POST or None)
    nfct_form = NFCT_Base_Rate_Form(request.POST or None)
    fct_form = base_rate_table_form(request.POST or None)
    fct_obj = fct_deal()
    user = request.user
    ag_det = AgencyDetail.objects.all()
    cli_name = CustomerName.objects.all()
    cli_det = CustomerContact.objects.all()
    agg = AgencyContact.objects.all()
    qs1 = Employees.objects.filter(emp_email__contains=user)
    tmpJson = serializers.serialize("json",cli_det)
    tmpagen = serializers.serialize("json",agg)
    formset = DealModelFormset(queryset=deal_nfct.objects.none())
    final_obj = FinalFctNfctDeal()
    context = {'form': form,'form1': form1,'ag_det':ag_det,'cli_name':cli_name,'cli_det':cli_det,'agg':agg,'tmpJson':tmpJson,'qs':qs1,'tmpagen':tmpagen, 'formset': formset, 
    'nfct_form': nfct_form, 'fct_form': fct_form}

    
    if request.method == "POST":
        print(request.POST,"all forms request.post---------------------")
        if form.is_valid() and formset.is_valid() and form1.is_valid():
            print("form errors--------------------",form.errors)
            print("form1 error===========",form1.errors)
            formset = DealModelFormset(request.POST or None)

            final_obj.fct_total   = form.cleaned_data.get('total_rev')
            final_obj.nfct_total  = form.cleaned_data.get('nfct_total')
            final_obj.grandtotal = form.cleaned_data.get('grandtotal')
            final_obj.client_name_ref     = form.cleaned_data.get('client_name_ref')
            final_obj.client_contact_ref  = form.cleaned_data.get('client_contact_ref')
            final_obj.agency_name_ref     = form.cleaned_data.get('agency_name_ref')
            final_obj.agency_contact_ref  = form.cleaned_data.get('agency_contact_ref')
            final_obj.brand_name_ref = form.cleaned_data.get('brand_name_ref')


            if request.POST.get('dis_dd') == '50%-50%':
                fct_obj.chan = request.POST.get('channel')
                fct_obj.dis = request.POST.get('dis_dd')
                fct_obj.band1 = request.POST.get('band1')
                fct_obj.band2 = request.POST.get('band2')
                fct_obj.fct1 = request.POST.get('fct1')
                fct_obj.fct2 = request.POST.get('fct2')

                fct_obj.eff_rate1 = request.POST.get('er1')
                fct_obj.eff_rate2 = request.POST.get('er2')

                fct_obj.rev1 = request.POST.get('rev1')
                fct_obj.rev2 = request.POST.get('rev2')
                rate1 = request.session['rate']
                fct_obj.base_rate1 = rate1
                rate2 = request.session['rate2']
                fct_obj.base_rate2 = rate2
                fct_obj.total_rev = form.cleaned_data.get('total_rev')
                fct_obj.deal_id = form.cleaned_data.get('deal_id')
                fct_obj.save()
                messages.success(request, 'Form is saved!')

            else:
                fct_obj.chan = request.POST.get('channel')
                fct_obj.dis = request.POST.get('dis_dd')
                fct_obj.band1 = request.POST.get('band1')
                fct_obj.band2 = request.POST.get('band2')
                fct_obj.band3 = request.POST.get('band3')
                fct_obj.fct1 = request.POST.get('fct1')
                fct_obj.fct2 = request.POST.get('fct2')
                fct_obj.fct3 = request.POST.get('fct3')
                fct_obj.eff_rate1 = request.POST.get('er1')
                fct_obj.eff_rate2 = request.POST.get('er2')
                fct_obj.eff_rate3 = request.POST.get('er3')
                fct_obj.rev1 = form.cleaned_data.get('rev1')
                fct_obj.rev2 = request.POST.get('rev2')
                fct_obj.rev3 = request.POST.get('rev3')
                fct_obj.total_rev = form.cleaned_data.get('total_rev')
                fct_obj.deal_id = form.cleaned_data.get('deal_id')
                rate1 = request.session['rate']
                fct_obj.base_rate1 = rate1
                rate2 = request.session['rate2']
                fct_obj.base_rate2 = rate2
                rate3 = request.session['rate3']
                fct_obj.base_rate3 = rate3

                fct_obj.save()
                messages.success(request, 'Form is saved!')


            formset.save()     
            final_obj.save()  
    else:
        print("Form is invalid")

    return render(request,"final_fct_nfct_deal/final_fct_nfct_deal.html",context)

def load_client_contacts(request):
    client_id = request.GET.get('client')
    client_contacts = CustomerContact.objects.filter(ref_creg_no=client_id).order_by('pri_fname')
    print(client_contacts)
    return render(request, 'final_fct_nfct_deal/client_contact_dropdown_options.html', {'client_contacts': client_contacts})

def load_agency_contacts(request):
    agency_id = request.GET.get('agency')
    agency_contacts = AgencyContact.objects.filter(agency_details=agency_id).order_by('pri_firstName')
    print(agency_contacts)
    return render(request, 'final_fct_nfct_deal/agency_contact_dropdown_options.html', {'agency_contacts': agency_contacts})

def load_br(request):
    chan_id = request.GET.get('channel')
    band1 = request.GET.get('band1')
    disp1 = request.GET.get('dis_dd')
    print("9999", chan_id, band1,disp1, request.GET)
    rates = Channel.objects.filter(c_list__contains=chan_id)
    b1 = Band.objects.filter(b_list__contains=band1)
    dis1 = Disper.objects.filter(dis_list__contains=disp1)
    if band1 is not None and chan_id is not None and disp1 != "33%-33%-33%":
        context1 = {'qs': rates}
        context2 = {'qs1': b1}
        for i in context1['qs']:
            c = i.c_list
            print("------", c)

        for j in context2['qs1']:
            b = j.b_list[:2]
            print("---****---", b)
        x = c + b
        print("*************", x)
        y = base_rate_table.objects.filter(unique_key=x)
        for k in y:
            rate = k.br
            print(rate)
            request.session['rate'] = rate
    elif disp1 == "33%-33%-33%":
        context1 = {'qs': rates}
        context2 = {'qs1': b1}
        context3 = {'qs2': dis1}
        for i in context1['qs']:
            c = i.c_list
            print("------", c)

        for j in context2['qs1']:
            b = j.b_list[:2]
            print("---****---", b)

        for m in context3['qs2']:
            d = m.dis_list[:2]
            print("---****---", d)
        x = c + d + b
        print("*************", x)
        y = base_rate_table.objects.filter(unique_key=x)
        for k in y:
            rate = k.br
            print(rate)
            request.session['rate'] = rate
    # return render(request,'deal_fct_nonfct/fct.html',{'rate': rate})
    return HttpResponse(rate)

def load_br1(request):
    chan_id = request.GET.get('channel')
    band2 = request.GET.get('band2')
    disp1 = request.GET.get('dis_dd')
    rates = Channel.objects.filter(c_list__contains=chan_id)
    b2 = Band.objects.filter(b_list__contains=band2)
    dis1 = Disper.objects.filter(dis_list__contains=disp1)
    print("REQUEST.GET!!!!!!!!!!!!!!!!!!!!!!", request.GET)
    if band2 is not None and chan_id is not None and disp1 != "33%-33%-33%":
        context1 = {'qs': rates}
        context2 = {'qs2': b2}
        for i in context1['qs']:
            c = i.c_list
            print("------", c)

        for p in context2['qs2']:
            base2 = p.b_list[:2]
            print("---****---", base2)
        x1 = c + base2
        print("*************", x1)
        y1 = base_rate_table.objects.filter(unique_key=x1)
        for k1 in y1:
            rate2 = k1.br
            print(rate2)
            request.session['rate2'] = rate2
        r = {'rate2': rate2}
        print("******************", r)
    elif disp1 == "33%-33%-33%":
        context1 = {'qs': rates}
        context2 = {'qs1': b2}
        context3 = {'qs2': dis1}
        for i in context1['qs']:
            c = i.c_list
            print("------", c)

        for j in context2['qs1']:
            base2 = j.b_list[:2]
            print("---****---", base2)

        for m in context3['qs2']:
            d = m.dis_list[:2]
            print("---****---", d)
        x = c + d + base2
        print("*************", x)
        y = base_rate_table.objects.filter(unique_key=x)
        for k in y:
            rate2 = k.br
            print(rate2)
            request.session['rate2'] = rate2
    # return render(request,'deal_fct_nonfct/fct.html',{'rate2': rate2})
    return HttpResponse(rate2)

def load_br2(request):
    chan_id = request.GET.get('channel')
    band3 = request.GET.get('band3')
    disp1 = request.GET.get('dis_dd')
    rates = Channel.objects.filter(c_list__contains=chan_id)
    b3 = Band.objects.filter(b_list__contains=band3)
    dis1 = Disper.objects.filter(dis_list__contains=disp1)
    if band3 is not None and chan_id is not None and disp1 != "33%-33%-33%":
        context1 = {'qs': rates}
        context2 = {'qs3': b3}
        for i in context1['qs']:
            c = i.c_list
            print("------", c)

        for p in context2['qs3']:
            base3 = p.b_list[:2]
            print("---****---", base3)
        x2 = c + base3
        print("*************", x2)
        y2 = base_rate_table.objects.filter(unique_key=x2)
        for k2 in y2:
            rate3 = k2.br
            print(rate3)
            request.session['rate3'] = rate3
        r = {'rate3': rate3}
        print("******************", r)
    elif disp1 == "33%-33%-33%":
        context1 = {'qs': rates}
        context2 = {'qs1': b3}
        context3 = {'qs2': dis1}
        for i in context1['qs']:
            c = i.c_list
            print("------", c)

        for j in context2['qs1']:
            b = j.b_list[:2]
            print("---****---", b)

        for m in context3['qs2']:
            d = m.dis_list[:2]
            print("---****---", d)
        x = c + d + b
        print("*************", x)
        y = base_rate_table.objects.filter(unique_key=x)
        for k in y:
            rate3 = k.br
            print(rate3)
            request.session['rate3'] = rate3
    # return render(request,'deal_fct_nonfct/fct.html',{'rate3': rate3})
    return HttpResponse(rate3)
