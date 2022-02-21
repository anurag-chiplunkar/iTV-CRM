from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
import json
from django.core import serializers
from .forms import *
from .models import *
from agency.models import *
from customer.models import *
from accounts.models import Employees
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')


@login_required(login_url='accounts:emp_login')
def fct_details(request):
    form = form_fct_deal(request.POST or None)
    fct_obj = fct_deal()
    user = request.user
    ag_det = AgencyDetail.objects.all()
    cli_name = CustomerName.objects.all()
    cli_det = CustomerContact.objects.all()
    agg = AgencyContact.objects.all()
    qs1 = Employees.objects.filter(emp_email__contains=user)
    tmpJson = serializers.serialize("json",cli_det)
    tmpagen = serializers.serialize("json",agg)
    
    context = {'form': form,'ag_det':ag_det,'cli_name':cli_name,'cli_det':cli_det,'agg':agg,'tmpJson':tmpJson,'qs':qs1,'tmpagen':tmpagen }
    if request.method == "POST":
        if request.POST.get('dis_dd') == '50%-50%':
            if form.is_valid():
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
    else:
        print("outside view")

    return render(request, 'deal_fct_nonfct/fct.html', context)


@login_required(login_url='accounts:emp_login')
def br_details(request):
    form = base_form(request.POST or None)
    obj = base()
    print("---------------------", request.POST, form.is_valid(), form.errors)

    # print("***********",master)
    context = {'form': form, }
    if request.method == "POST":
        if form.is_valid():
            # obj.date = form.cleaned_data['date']
            obj.channel = request.POST.get('channel_list')
            obj.dispersion = request.POST.get('dis_list')
            obj.bands = request.POST.get('bands_list')
            obj.br = request.POST.get('base_rate')
            obj.save()
            messages.success(request, 'Base rate added!!')
            print("inside!!!!!!!!")
        else:
            print("outside view")
    return render(request, 'deal_fct_nonfct/base_rate.html', context)


@login_required(login_url='accounts:emp_login')
def enter_channels(request):
	form = channel_form(request.POST or None)
	ch_obj = Channel()
	context = {'form': form,}
	if request.method == 'POST':
		if form.is_valid():
			ch_obj.c_list = form.cleaned_data.get('c_list')
			ch_obj.save()
			messages.success(request,'Channel is saved!')
		else:
			print("outside view")
	return render(request,'deal_fct_nonfct/channel.html',context)

@login_required(login_url='accounts:emp_login')
def enter_disper(request):
    form = disper_form(request.POST or None)
    dis_obj = Disper()
    context = {'form': form, }
    print("////////////", request.POST)
    if request.method == 'POST':
        if form.is_valid():
            dis_obj.dis_list = form.cleaned_data.get('dis_list')
            dis_obj.save()
            messages.success(request, 'Dispersion is saved!')
        else:
            print("outside view")
    return render(request, 'deal_fct_nonfct/dispersion.html', context)


@login_required(login_url='accounts:emp_login')
def enter_band(request):
    form = band_form(request.POST or None)
    band_obj = Band()
    context = {'form': form, }
    print("////////////", request.POST)
    if request.method == 'POST':
        if form.is_valid():
            band_obj.b_list = form.cleaned_data.get('b_list')
            band_obj.save()
            messages.success(request, 'Band is saved!')
        else:
            print("outside view")
    return render(request, 'deal_fct_nonfct/band.html', context)


@login_required(login_url='accounts:emp_login')
def enter_base_rate(request):
    form = base_rate_table_form(request.POST or None)
    b_obj = base_rate_table()
    context = {'form': form}
    print(form.errors)
    if request.method == 'POST':
        if form.is_valid():
            chan = request.POST.get('channel')
            bd = request.POST.get('band')
            b_obj.br = form.cleaned_data.get('br')
            disp = request.POST.get('dis')
            if disp is None:
                uni = chan + bd[:2]
                b_obj.unique_key = uni

                print("----------", uni, chan, bd, b_obj.br)
                b_obj.save()
                messages.success(request, 'Base Rate is saved!')
                return redirect('deal_fct_nonfct:enter_base_rate')
            else:
                uni_33 = chan + disp[:2] + bd[:2]
                b_obj.unique_key = uni_33

                print("----------", uni_33, chan, bd, disp, b_obj.br)
                b_obj.save()
                messages.success(request, 'Base Rate is saved!')
                return redirect('deal_fct_nonfct:enter_base_rate')
    return render(request, 'deal_fct_nonfct/base.html', context)


@login_required(login_url='accounts:emp_login')
def load_br(request):
    chan_id = request.GET.get('channel')
    band1 = request.GET.get('band1')
    disp1 = request.GET.get('dis_dd')
    print("9999", chan_id, band1, request.GET)
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


@login_required(login_url='accounts:emp_login')
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


@login_required(login_url='accounts:emp_login')
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
