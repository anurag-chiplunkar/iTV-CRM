# from typing import final
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
from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts:emp_login')
def finalDealListView(request):
    qs = FinalFctNfctDeal.objects.all()
    qs1 = Fct_deal.objects.all()
    qs2 = Deal_nfct.objects.all()
    mycontext = {'qs': qs, 'qs1': qs1, 'qs2': qs2}
    template_name = 'final_fct_nfct_deal/final_deallist.html'
    return render(request, template_name, mycontext)

@login_required(login_url='accounts:emp_login')
def final_deal(request):
    form = FinalFctNfctDealDetails(request.POST or None)
    form1 = form_fct_deal(request.POST or None)
    nfct_form = NFCT_Base_Rate_Form(request.POST or None)
    fct_form = Base_rate_table_form(request.POST or None)
    fct_obj = Fct_deal()
    nfct_obj = Deal_nfct()
    user = request.user
    ag_det = AgencyDetail.objects.all()
    cli_name = CustomerName.objects.all()
    cli_det = CustomerContact.objects.all()
    agg = AgencyContact.objects.all()
    qs1 = Employees.objects.filter(emp_email__contains=user)
    tmpJson = serializers.serialize("json", cli_det)
    tmpagen = serializers.serialize("json", agg)
    formset = DealModelFormset(queryset=Deal_nfct.objects.none())
    final_obj = FinalFctNfctDeal()
    context = {'form': form, 'form1': form1, 'ag_det': ag_det, 'cli_name': cli_name, 'cli_det': cli_det, 'agg': agg, 'tmpJson': tmpJson, 'qs': qs1, 'tmpagen': tmpagen, 'formset': formset,
               'nfct_form': nfct_form, 'fct_form': fct_form}
    
    if request.method == 'POST':
        fct_obj.dealid_fct_ref = request.POST.get('deal_id')
        print('fct_obj.dealid_fct_ref', fct_obj.dealid_fct_ref)
        print("form errors--------------------", form.errors)
        print("form1 error===========", form1.errors)
        print("formset.errors here~~~~~~~", formset.errors)
        if form.is_valid():
            print('inside form')
            print(form.cleaned_data, "from form-------******------")
            final_obj.deal_id = request.POST.get('deal_id')
            final_obj.executive = request.POST.get('executive')
            final_obj.reporting_manager = request.POST.get('reporting_manager')
            final_obj.RO_number = form.cleaned_data.get('RO_number')
            final_obj.RO_value = form.cleaned_data.get('RO_value')
            final_obj.client_name_ref = form.cleaned_data.get(
                'client_name_ref')
            final_obj.client_contact_ref = form.cleaned_data.get(
                'client_contact_ref')
            final_obj.agency_name_ref = form.cleaned_data.get(
                'agency_name_ref')
            final_obj.agency_contact_ref = form.cleaned_data.get(
                'agency_contact_ref')
            final_obj.brand_name_ref = form.cleaned_data.get('brand_name_ref')
            
            form.save(commit=False)
            print("save commit false!!!")
            
            print(form1.is_valid)
            if form1.is_valid():
                
                print('indise form1')
                print(request.POST, "////////////")
                if request.POST.get('dis_dd') == '50%-50%':
                    fct_obj.dealid_fct_ref = fct_obj.dealid_fct_ref
                    print('fct_obj.dealid_fct_ref',fct_obj.dealid_fct_ref)
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
                    total_revenue = form1.cleaned_data.get('total_rev')
                    if total_revenue is None:
                        total_revenue = 0
                    else:
                        fct_obj.total_rev = float(total_revenue)
                    
                    print("total rev here!!!!", fct_obj.total_rev)

                    fct_obj.save()
                    print("reached after form-1-1 saved commit false")
                    messages.success(request, 'Form is saved!')

                else:
                    fct_obj.dealid_fct_ref = fct_obj.dealid_fct_ref
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
                    fct_obj.rev1 = request.POST.get('rev1')
                    fct_obj.rev2 = request.POST.get('rev2')
                    fct_obj.rev3 = request.POST.get('rev3')
                    total_revenue = form1.cleaned_data.get('total_rev')
                    if total_revenue is None:
                        total_revenue = 0.0
                    else:
                        fct_obj.total_rev = float(total_revenue)
                    request.session['fcttotal'] = fct_obj.total_rev
                    # grandtotal.append(total_revenue)
                    print("total rev here!!!!", fct_obj.total_rev)
                    # rate1 = request.session['rate']
                    # fct_obj.base_rate1 = rate1
                    # rate2 = request.session['rate2']
                    # fct_obj.base_rate2 = rate2
                    # rate3 = request.session['rate3']
                    # fct_obj.base_rate3 = rate3
                    print("Session values before",request.session.items())
                    rate1 = request.session.get('rate',0)
                    print(rate1,"RATE1 Printed!!!!") 
                    fct_obj.base_rate1 = rate1
                    rate2 = request.session.get('rate2',0)
                    print(rate2,"RATE2 Printed!!!!") 
                    fct_obj.base_rate2 = rate2
                    rate3 = request.session.get('rate3',0)
                    print(type(rate3),"RATE3 Printed!!!!")
                    fct_obj.base_rate3 = rate3
                    print("Session values after",request.session.items())

                    fct_obj.save()
                    messages.success(request, 'Form is saved!')


                print("reached after form-1 saved commit false")
                form.fct_total = total_revenue

                formset = DealModelFormset(request.POST or None)
                print("if-----", formset.is_valid())
                print(formset.forms, '++++++++++++++++++++++++++')
                print(formset.errors, '==============================')
                
                if formset.is_valid():
                    for f in formset.forms:
                        obj = f.save(commit=False)
                        obj.main_dealid_nfct_ref = request.POST.get('deal_id')
                        obj.save()
                        print("Saved")
                    gt_obj = NFCTGrandTotal()
                    gt_obj.nfct_grandtotal = request.POST.get('nfct_grandtotal')
                    print('gt_obj.nfct_grandtotal', gt_obj.nfct_grandtotal)
                    gt_obj.dealid_nfct_ref = request.POST.get('deal_id')
                    print('gt_obj.dealid_nfct_ref', gt_obj.dealid_nfct_ref)
                    gt_obj.save()
                    nfct_total = request.POST.get('nfct_grandtotal')
                    nfct_total = float(nfct_total)
                    final_obj.nfct_total = nfct_total
                    final_obj.fct_total = total_revenue
                    # fct_total = request.session['fcttotal']
                    print("-----nfct total here -***---", nfct_total,total_revenue)
                    
                    final_obj.grandtotal = float(total_revenue) + float(nfct_total)
                    # final_obj.grandtotal = gtotal
                    print("grandtotal here!!!!!!~~~~~", final_obj.grandtotal)
                    final_obj.save()
                    # form1.save(commit=True)
                    # form.save(commit=True)
                    formset.save()
                    print("Form is saved and rates are removed from session dictionary~~~Happpy~~~",request.session.items())
                    if request.session.get('rate',None):
                        del request.session['rate']
                    else:
                        print("None")
                    if request.session.get('rate2',None):
                        del request.session['rate2']
                    else:
                        print("None")
                    if request.session.get('rate3',None):
                        del request.session['rate3']
                    else:
                        print("None")
                    print("Form is saved and rates are removed from session dictionary (down)~~~Happpy~~~",request.session.items())
                   
                    print("reached at the end---------------------")

                    return redirect('/final_deallist')
               

    return render(request, "final_fct_nfct_deal/final_fct_nfct_deal.html", context)


def load_client_contacts(request):
    client_id = request.GET.get('client')
    client_contacts = CustomerContact.objects.filter(ref_creg_no=client_id).order_by('pri_fname')
    print(client_contacts)
    return render(request, 'final_fct_nfct_deal/client_contact_dropdown_options.html', {'client_contacts': client_contacts})


def load_agency_contacts(request):
    agency_id = request.GET.get('agency')
    agency_contacts = AgencyContact.objects.filter(
        agency_details=agency_id).order_by('pri_firstName')
    print(agency_contacts)
    return render(request, 'final_fct_nfct_deal/agency_contact_dropdown_options.html', {'agency_contacts': agency_contacts})

def load_agency_client(request):
    cli_id = request.GET.get('client')
    print('CLIENT', cli_id)
    agency = AgencyDetail.objects.filter(ccreg_no=cli_id).order_by('agency_name')
    print(agency)
    return render(request, 'final_fct_nfct_deal/agency_client_dropdown_options.html', {'agency': agency})




def final_load_br(request):
    chan_id = request.GET.get('channel')
    band1 = request.GET.get('band1')
    disp1 = request.GET.get('dis_dd')
    print("9999", chan_id, band1, disp1, request.GET)
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
        y = Base_rate_table.objects.filter(unique_key=x)
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
        y = Base_rate_table.objects.filter(unique_key=x)
        for k in y:
            rate = k.br
            print(rate)
            request.session['rate'] = rate
    # return render(request,'deal_fct_nonfct/fct.html',{'rate': rate})
    return HttpResponse(rate)


def final_load_br1(request):
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
        y1 = Base_rate_table.objects.filter(unique_key=x1)
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
        y = Base_rate_table.objects.filter(unique_key=x)
        for k in y:
            rate2 = k.br
            print(rate2)
            request.session['rate2'] = rate2
    else:
        request.session['rate2'] = 0
        print("rate2 PRINTED~~~",request.session['rate2'])
    # return render(request,'deal_fct_nonfct/fct.html',{'rate2': rate2})
    return HttpResponse(rate2)


def final_load_br2(request):
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
        y2 = Base_rate_table.objects.filter(unique_key=x2)
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
        y = Base_rate_table.objects.filter(unique_key=x)
        for k in y:
            rate3 = k.br
            print(rate3)
            request.session['rate3'] = rate3

    else:
        request.session['rate3'] = 0
        print("rate3 PRINTED~~~",request.session['rate3'])
    # return render(request,'deal_fct_nonfct/fct.html',{'rate3': rate3})
    return HttpResponse(rate3)
