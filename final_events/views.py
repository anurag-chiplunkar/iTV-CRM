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
# from nfct.models import *
# from nfct.forms import *
from deal_fct_nonfct.models import *
from deal_fct_nonfct.forms import *
# import random
# import json
# import simplejson as json
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def finalDealListView(request):
    qs = Eventmodel.objects.all()
    mycontext = {'qs': qs,}
    template_name = 'final_events/event_final_deallist.html'
    return render(request, template_name, mycontext)

def final_event_deal(request):
    evt_form = FinalEventsForm(request.POST or None)
    fct_form = Form_FCT_Deal(request.POST or None)
    nfct_form = NFCT_Base_Rate_Form(request.POST or None)
    fct_br_form = Base_rate_table_form(request.POST or None)
    fct_obj = EventFCTModel()
    user = request.user
    ag_det = AgencyDetail.objects.all()
    cli_name = CustomerName.objects.all()
    cli_det = CustomerContact.objects.all()
    agg = AgencyContact.objects.all()
    qs1 = Employees.objects.filter(emp_email__contains=user)
    tmpJson = serializers.serialize("json", cli_det)
    tmpagen = serializers.serialize("json", agg)
    formset = DealModelFormset(queryset=Event_Deal_Nfct.objects.none())
    final_obj = Eventmodel()
    context = {'evt_form':evt_form,'fct_form':fct_form,'nfct_form':nfct_form,'fct_br_form':fct_br_form,'fct_obj':fct_obj,'ag_det':ag_det,
    'cli_name':cli_name,'qs1':qs1,'tmpJson':tmpJson,'tmpagen':tmpagen,'formset':formset}
    grandtotal = []
    if request.method == 'POST':
        
        print("~~~~~~~~~~~~ID HERE~~~~~~~~~~~",fct_obj.deal_id_fct)
        print("REQUEST.POST here",request.POST)
        print("form errors--------------------", evt_form.errors)
        print("form1 error===========", fct_form.errors)
        print("formset.errors here~~~~~~~", formset.errors)
        if evt_form.is_valid():
            fct_obj.deal_id_fct = evt_form.cleaned_data.get('deal_id')
            print(fct_obj.deal_id_fct,"//////fct_obj.deal_id_fct")
            print(evt_form.cleaned_data, "from form-------******------")
            # D_id = request.POST.get('deal_id')
            final_obj.deal_id = request.POST.get('deal_id')
            print("final_obj iD heRE===========",final_obj.deal_id)
            final_obj.executive = request.POST.get('salesperson')
            final_obj.reporting_manager = request.POST.get('reporting')
            final_obj.event_client_name_ref = evt_form.cleaned_data.get('event_client_name_ref')
            final_obj.event_client_contact_ref = evt_form.cleaned_data.get('event_client_contact_ref')
            final_obj.event_agency_name_ref = evt_form.cleaned_data.get('event_agency_name_ref')
            final_obj.event_agency_contact_ref = evt_form.cleaned_data.get('event_agency_contact_ref')
            final_obj.event_brand_name_ref = evt_form.cleaned_data.get('event_brand_name_ref')
            final_obj.category = evt_form.cleaned_data.get('category')
            final_obj.description = evt_form.cleaned_data.get('description')
            final_obj.channel = request.POST.get('channel')
            
            final_obj.fct_seconds = request.POST.get('fct_secs')
            final_obj.ro_number = request.POST.get('ro_number')
            final_obj.ro_value = request.POST.get('ro_value')
            evt_form.save(commit=False)
            print("save commit false above!!!")
            print(fct_form.is_valid(),"***********fct_form.is_valid()************")
            print(fct_form.cleaned_data,"*****FCT cleaned data-----")
            print(fct_form.errors, '-------------errors----------------')
            if fct_form.is_valid():
                print(request.POST, "////////////")
                if request.POST.get('dis_dd') == '50%-50%':
                    fct_obj.deal_id_fct = fct_obj.deal_id_fct
                    print("inside fct form...ID here",fct_obj.deal_id_fct)
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
                    total_revenue = fct_form.cleaned_data.get('total_rev')
                    fct_obj.total_rev = total_revenue
                    print("total rev here!!!!", fct_obj.total_rev)

                    fct_obj.save()
                    print("reached after form-1-1 saved commit false")
                    messages.success(request, 'Form is saved!')

                else:
                    fct_obj.deal_id_fct = fct_obj.deal_id_fct
                    print("inside fct form...ID here",fct_obj.deal_id_fct)
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
                    total_revenue = fct_form.cleaned_data.get('total_rev')
                    fct_obj.total_rev = total_revenue
                    request.session['fcttotal'] = fct_obj.total_rev
                    grandtotal.append(total_revenue)
                    print("total rev here!!!!", fct_obj.total_rev)
                    rate1 = request.session['rate']

                    fct_obj.base_rate1 = rate1
                    rate2 = request.session['rate2']
                    fct_obj.base_rate2 = rate2
                    rate3 = request.session['rate3']
                    fct_obj.base_rate3 = rate3

                    fct_obj.save()
                    messages.success(request, 'Form is saved!')


                print("reached after form-1 saved commit false")
                evt_form.fct_total = total_revenue

                formset = DealModelFormset(request.POST or None)
                print("//////formset.forms",formset.forms)
                print("if-----", formset.is_valid(),formset.errors)
                if formset.is_valid():
                    print("print inside formset~~~~")
                    for f in formset.forms:
                        obj = f.save(commit=False)
                        obj.deal_id_nfct = evt_form.cleaned_data.get('deal_id')
                        print("deal id nfct inside for",obj.deal_id_nfct)
                        obj.save()
                        f.save()
                        print("Saved")
                    # nfctdeal_id.deal_id_nfct = evt_form.cleaned_data.get('deal_id')
                    gt_obj = EventNFCTGrandTotal()
                    gt_obj.nfct_grandtotal = float(request.POST.get('nfct_grandtotal'))
                    print('gt_obj.nfct_grandtotal', gt_obj.nfct_grandtotal)
                    gt_obj.dealid_nfct_ref = request.POST.get('deal_id')
                    print('gt_obj.dealid_nfct_ref', gt_obj.dealid_nfct_ref)
                    gt_obj.save()
                    
                    nfct_total_amt = request.POST.get('nfct_grandtotal')
                    nfct_total_amt = float(nfct_total_amt)
                    final_obj.nfct_total_amt = nfct_total_amt
                    meritmoney = request.POST.get('merit_money')
                    final_obj.merit_money = float(meritmoney)
                    meritmoney = float(meritmoney)
                    final_obj.fct_total_amt = total_revenue
                    print("merit money printed here!!!!!!!!!!",meritmoney)
                    final_obj.grandtotal_amt = meritmoney + float(total_revenue) + nfct_total_amt
                    print("GRAND TOTAL OF ALL----------------------",final_obj.grandtotal_amt)
                    
                    print("formset saved!!!!!!!!!!!!!!!!!!!!")
                    final_obj.save()
                    formset.save(commit=True)
                    print("reached at the end---------------------")

                    return redirect('/event_final_deallist')
    return render(request,'final_events/event.html',context)

def load_client_contacts(request):
    client_id = request.GET.get('client')
    client_contacts = CustomerContact.objects.filter(
        ref_creg_no=client_id).order_by('pri_fname')
    print(client_contacts)
    return render(request, 'final_events/client_contact_dropdown_options.html', {'client_contacts': client_contacts})


def load_agency_contacts(request):
    agency_id = request.GET.get('agency')
    agency_contacts = AgencyContact.objects.filter(
        agency_details=agency_id).order_by('pri_firstName')
    print(agency_contacts)
    return render(request, 'final_events/agency_contact_dropdown_options.html', {'agency_contacts': agency_contacts})

def final_load_br(request):
    chan_id = request.GET.get('channel')
    band1 = request.GET.get('band1')
    disp1 = request.GET.get('dis_dd')
    print("9999", chan_id, band1, disp1, request.GET)
    rates = Channel.objects.filter(c_list__contains=chan_id)
    print('RATES', rates)
    b1 = Band.objects.filter(b_list__contains=band1)
    print('BAND1', b1)
    dis1 = Disper.objects.filter(dis_list__contains=disp1)
    print('DISPERSION', dis1)
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
    # return render(request,'deal_fct_nonfct/fct.html',{'rate3': rate3})
    return HttpResponse(rate3)


def nfct_enter_base_rate(request):
    nfct_form = NFCT_Base_Rate_Form(request.POST or None)
    nfct_obj = Event_NFCT_Base_Rate()
    context = {'nfct_form': nfct_form}
    print(nfct_form.errors)
    print(request.POST)
    if request.method == 'POST':
        if nfct_form.is_valid():
            nfct_obj.channel = nfct_form.cleaned_data.get('channel')
            # print(nfct_channels)

            nfct_obj.element = nfct_form.cleaned_data.get('element')
            # print(nfct_elements)
            nfct_obj.nfct_baserate = nfct_form.cleaned_data.get(
                'nfct_baserate')

            uni = str(nfct_obj.channel) + str(nfct_obj.element)
            print(uni)
            nfct_obj.nfct_unique_key = uni

            print("----------", nfct_obj.channel,
                  nfct_obj.element, nfct_obj.nfct_baserate)
            print(request.POST, '*********************************')
            nfct_obj.save()

    return render(request, 'final_events/nfct_base.html', context)


def nfct_load_br(request):
    chan_id = request.GET.get('channel')
    print(request.GET)
    print(chan_id, 'Chan id')
    element = request.GET.get('element')
    print(element, '&&&&&&&&&&&&&&&&&&')
    print("**************************************************************")

    rates = Event_NFCT_Base_Rate.objects.filter(channel__contains=chan_id)
    print(rates, '++++++++++++++')
    element_name = Event_NFCT_Base_Rate.objects.filter(element__contains=element)
    print(element_name, '++++++++++++++++++++')

    context1 = {'qs': rates}
    context2 = {'qs1': element_name}

    print("CONTEXT1", context1)
    print("CONTEXT2", context2)

    for i in context1['qs']:
        c = i.channel
        print("------", c)

    for j in context2['qs1']:
        b = j.element
        print("------", b)

    x = c + b
    print("*************", x)

    y = Event_NFCT_Base_Rate.objects.filter(nfct_unique_key__contains=x)
    print("*************", y)

    for k in y:
        # print(k)
        nfctbaserate = k.nfct_baserate
        request.session['nfct_baserate'] = nfctbaserate
        print(nfctbaserate, '0000000000000000')
        # return '200'
    mycontext = {'nfctbaserate': nfctbaserate}
    print(mycontext)
    return HttpResponse(nfctbaserate)