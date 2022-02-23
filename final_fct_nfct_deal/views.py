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

    # if request.method == 'GET':
    #     formset = DealModelFormset(queryset=deal_nfct.objects.none())
    #     return render(request, 'final_fct_nfct_deal/final_fct_nfct_deal.html', {'formset': formset})
    # elif request.method == 'POST':

        # formset = DealModelFormset(request.POST or None)
        # if formset.is_valid():
        #     formset.save()
            # return redirect('nfct:deallist')

    user = request.user
    ag_det = AgencyDetail.objects.all()
    cli_name = CustomerName.objects.all()
    cli_det = CustomerContact.objects.all()
    agg = AgencyContact.objects.all()
    qs1 = Employees.objects.filter(emp_email__contains=user)
    tmpJson = serializers.serialize("json",cli_det)
    tmpagen = serializers.serialize("json",agg)
    formset = DealModelFormset(queryset=deal_nfct.objects.none())
    context = {'form': form,'ag_det':ag_det,'cli_name':cli_name,'cli_det':cli_det,'agg':agg,'tmpJson':tmpJson,'qs':qs1,'tmpagen':tmpagen, 'formset': formset, 'nfct_form': nfct_form, 'fct_form': fct_form}

    ##generating deal id
    try:
        deal_id = random.randint(1,100)
        print(deal_id)
    except IntegrityError:
        deal_id = random.randint(101,200)
        print(deal_id)

    if request.method == 'GET':
        # formset = DealModelFormset(queryset=deal_nfct.objects.none())
        return render(request, 'final_fct_nfct_deal/final_fct_nfct_deal.html', context)
    
    elif request.method == "POST":
        if form.is_valid() and formset.is_valid() and form1.is_valid():
            formset = DealModelFormset(request.POST or None)

            fct_total   = form.cleaned_data.get('total_rev')
            nfct_total  = form.cleaned_data.get('nfct_total')
            grand_total = form.cleaned_data.get('grand_total')
            client_name_ref     = form.cleaned_data.get('client_name_ref')
            client_contact_ref  = form.cleaned_data.get('client_contact_ref')
            agency_name_ref     = form.cleaned_data.get('agency_name_ref')
            agency_contact_ref  = form.cleaned_data.get('agency_contact_ref')
            brand_name_ref = form.cleaned_data.get('brand_name_ref')

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



            
        else:
            print("Form is invalid")

    return render(request,"final_fct_nfct_deal/final_fct_nfct_deal.html",context)



def load_br(request):
    chan_id = request.GET.get('channel')
    band1 = request.GET.get('band1')
    disp1 = request.GET.get('dis_dd')
    print("9999", chan_id, band1, request.GET)
    rates = Channel.objects.filter(c_list__contains=chan_id)
    b1 = Band.objects.filter(b_list__contains=band1)
    dis1 = Disper.objects.filter(dis_list__contains=disp1)
    # if band1 is not None and chan_id is not None and disp1 != "33%-33%-33%":
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
    # elif disp1 == "33%-33%-33%":
    #     context1 = {'qs': rates}
    #     context2 = {'qs1': b1}
    #     context3 = {'qs2': dis1}
    #     for i in context1['qs']:
    #         c = i.c_list
    #         print("------", c)

    #     for j in context2['qs1']:
    #         b = j.b_list[:2]
    #         print("---****---", b)

    #     for m in context3['qs2']:
    #         d = m.dis_list[:2]
    #         print("---****---", d)
    #     x = c + d + b
    #     print("*************", x)
    #     y = base_rate_table.objects.filter(unique_key=x)
    #     for k in y:
    #         rate = k.br
    #         print(rate)
    #         request.session['rate'] = rate
    # return render(request,'deal_fct_nonfct/fct.html',{'rate': rate})
    return HttpResponse(rate)
