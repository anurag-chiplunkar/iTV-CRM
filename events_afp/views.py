from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# import requests
from django.shortcuts import redirect

from .forms import *

import random
from .models import *
# from .forms import AFPModelFormSet
# from django.forms import modelformset_factory
# from django.views.generic import TemplateView
# from django.forms import formset_factory
global ref

def afp_pname(request):
	form1 = AFP_Progname(request.POST or None)

	context = {"form1" : form1}
	print(form1.is_valid())
	print(form1.errors)
	print(request.POST)

	if request.method == "POST":
		if form1.is_valid():
			print(form1.cleaned_data)
			obj1 = AFP_ProgramName()
			print("inside form1")
			obj1.program_name = form1.cleaned_data.get('program_name')
			print(obj1.program_name)

			obj1.save()
		else:
			print("Invalid Form1")
	return render(request, 'events_afp/afp.html', context)


def afp_chname(request):
	form2 = AFP_Chann(request.POST or None)

	context = {"form2" : form2}
	print(form2.is_valid())
	print(form2.errors)
	print(request.POST)

	if request.method == "POST":
		if form2.is_valid():
			print(form2.cleaned_data)
			obj2 = AFP_Channels()
			print("inside form2")
			obj2.channels = form2.cleaned_data.get('channels')
			print(obj2.channels)

			obj2.save()
		else:
			print("Invalid Form2")
	return render(request, 'events_afp/afp2.html', context)
def enter_channels(request):
	form = channel_form(request.POST or None)
	ch_obj = Channel()
	context = {'form': form,}
	print("////////////",request.POST)
	if request.method == 'POST':
		if form.is_valid():
			ch_obj.c_list = form.cleaned_data.get('c_list')
			ch_obj.save()
			print("inside channel views-----")
		else:
			print("outside view")
	return render(request,'deal_fct_nonfct/channel.html',context)
def enter_disper(request):
	form = disper_form(request.POST or None)
	dis_obj = Disper()
	context = {'form': form,}
	print("////////////",request.POST)
	if request.method == 'POST':
		if form.is_valid():
			dis_obj.dis_list = form.cleaned_data.get('dis_list')
			dis_obj.save()
			print("inside dispersion views-----")
		else:
			print("outside view")
	return render(request,'events_afp/dispersion.html',context)

def enter_band(request):
	form = band_form(request.POST or None)
	band_obj = Band()
	context = {'form': form,}
	print("////////////",request.POST)
	if request.method == 'POST':
		if form.is_valid():
			band_obj.b_list = form.cleaned_data.get('b_list')
			band_obj.save()
			print("inside band views-----")
		else:
			print("outside view")
	return render(request,'events_afp/band.html',context)

def enter_base_rate(request):
	form = base_rate_table_form(request.POST or None)
	b_obj = base_rate_table()
	context = {'form':form}
	print(form.errors)
	print(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			chan = request.POST.get('channels')
			bd = request.POST.get('band')
			b_obj.br = form.cleaned_data.get('br')

			uni = chan + bd[:2]
			b_obj.unique_key = uni

			print("----------",uni,chan,bd,b_obj.br)
			b_obj.save()

	return render(request,'events_afp/base.html',context)

def cat_name(request):
	form4 = Events_catname(request.POST or None)

	context = {"form4" : form4}
	print(form4.is_valid())
	print(form4.errors)
	print(request.POST)

	if request.method == "POST":
		if form4.is_valid():
			print(form4.cleaned_data)
			obj4 = Events_Category()
			print("inside form4")
			obj4.category_name = form4.cleaned_data.get('category_name')
			print(obj4.category_name)

			obj4.save()
		else:
			print("Invalid Form4")
	return render(request, 'events_afp/Events_Category.html', context)
# def register_element(request):
# 	form = ElementForm(request.POST or None)
# 	context = {"form":form}

# 	if request.method == "POST":
# 		print(request.POST)

# 		if form.is_valid():
# 			e 	= form.cleaned_data.get('element')
# 			obj = ElementNFCT(element = e)
# 			obj.save()

# 		else:
# 			print("element form invalid")
# 	return render(request,'deals/elements.html',context)
	





# def final_deal_info(request):
# 	qs = FinalDeal.objects.all()
# 	print(qs)
# 	qs_context = {"qs":qs}
# 	return render(request, 'events_afp/deal_info.html', qs_context)




def load_br(request):
	print("inside load br")
	chan_id = request.GET.get('channel')
	band1 = request.GET.get('band1')
	print("9999",chan_id,band1)
	rates = AFP_Channels.objects.filter(channels__contains=chan_id)
	b1 = Band.objects.filter(b_list__contains=band1)
	context1 = {'qs':rates}
	context2 = {'qs1':b1}
	for i in context1['qs']:
		c = i.channels
		print("------",c)

	for j in context2['qs1']:
		b = j.b_list[:2]
		print("---****---",b)
	x = c + b 
	print("*************",x)
	y = base_rate_table.objects.filter(unique_key__contains = x)
	print(y, '++++++++++++++++++++++')
	for k in y:
		rate = k.br
		print(rate)
	return render(request,'events_afp/final_deal.html',{'rate': rate})

def load_br1(request):
	chan_id = request.GET.get('channels')
	band2 = request.GET.get('band2')
	rates = AFP_Channels.objects.filter(channels__contains=chan_id)
	b2 = Band.objects.filter(b_list__contains=band2)
	context1 = {'qs':rates}
	context2 = {'qs2':b2}
	for i in context1['qs']:
		c = i.channels
		print("------",c)

	for p in context2['qs2']:
		base2 = p.b_list[:2]
		print("---****---",base2)
	x1 = c + base2
	print("*************",x1)
	y1 = base_rate_table.objects.filter(unique_key=x1)
	for k1 in y1:
		rate2 = k1.br
		print(rate2)
	r = {'rate2': rate2}
	print("******************",r)
	return render(request,'events_afp/final_deal.html',{'rate2': rate2})

def load_br2(request):
	chan_id = request.GET.get('channels')
	band3 = request.GET.get('band3')
	rates = AFP_Channels.objects.filter(channels__contains=chan_id)
	b3 = Band.objects.filter(b_list__contains=band3)
	context1 = {'qs':rates}
	context2 = {'qs3':b3}
	for i in context1['qs']:
		c = i.channels
		print("------",c)

	for p in context2['qs3']:
		base3 = p.b_list[:2]
		print("---****---",base3)
	x2 = c + base3
	print("*************",x2)
	y2 = base_rate_table.objects.filter(unique_key=x2)
	for k2 in y2:
		rate3 = k2.br
		print(rate3)
	r = {'rate3': rate3}
	print("******************",r)
	return render(request,'events_afp/final_deal.html',{'rate3': rate3})


# afp
def afp_base_rate(request):
	form = AFP_Base_Rate_Form(request.POST or None)
	b_obj = AFP_Base_Rate()
	context = {'form':form}
	print(form.errors)
	print(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			program_name = request.POST.get('program_name')
			channels = request.POST.get('channels')
			b_obj.baserate = form.cleaned_data.get('baserate')

			uni = channels + bd[:2]
			b_obj.unique_key = uni

			print("----------",uni,program_name,channels,b_obj.baserate)
			b_obj.save()

	return render(request,'events_afp/base.html',context)

def afp_load_br(request):
	chan_id = request.GET.get('channel')
	program = request.GET.get('program_name')
	print("9999",chan_id,program)
	rates = AFP_Channels.objects.filter(channels__contains=chan_id)
	program_name = AFP_ProgramName.objects.filter(program_name__contains=program)
	context1 = {'qs':rates}
	context2 = {'qs1':program_name}
	for i in context1['qs']:
		c = i.channels
		print("------",c)

	for j in context2['qs1']:
		b = j.program_name
		print("---****---",b)
	x = c + b 
	print("*************",x)
	y = AFP_Base_Rate.objects.filter(afp_unique_key__contains=x)
	# print(y, '++++++++++++++++++++++++')
	for k in y:
		# print(k)
		afprate = k.baserate
		print(afprate)
	return render(request,'events_afp/final_deal.html',{'afprate': afprate})

def afp_enter_base_rate(request):
	afp_form = AFP_Base_Rate_Form(request.POST or None)
	b_obj = AFP_Base_Rate()
	context = {'afp_form':afp_form}
	print(afp_form.errors)
	print(request.POST)
	if request.method == 'POST':
		if afp_form.is_valid():
			channels = request.POST.get('channel')
			print(channels)

			program_name = request.POST.get('band')
			print(program_name)
			b_obj.baserate = afp_form.cleaned_data.get('baserate')

			uni = channels + program_name
			print(uni)
			b_obj.afp_unique_key = uni

			print("----------",channels,program_name,b_obj.baserate)
			b_obj.save()

	return render(request,'events_afp/afp_base.html',context)

# Non-FCT deal

# def register_element(request):
# 	form = ElementForm(request.POST or None)
# 	context = {"form":form}

# 	if request.method == "POST":
# 		print(request.POST)

# 		if form.is_valid():
# 			e 	= form.cleaned_data.get('element')
# 			obj = ElementNFCT(element = e)
# 			obj.save()

# 		else:
# 			print("element form invalid")
# 	return render(request,'events_afp/elements.html',context)
# def register_base_rate(request):
# 	form = BaseRateForm(request.POST or None)
# 	context = {"form":form}

# 	if request.method == "POST":
# 		print(request.POST)

# 		if form.is_valid():
# 			channel_choice = form.cleaned_data.get('channel_choice')
# 			element_choice = form.cleaned_data.get('element_choice')
# 			print(element_choice,type(element_choice))
# 			key = str(channel_choice)+str(element_choice)
# 			print(key)
# 			br 	= form.cleaned_data.get('base_rate')

# 			obj = BaseRateNFCT(base_rate = br,unique_key = key)
# 			obj.save()

# 		else:
# 			print("base rate form invalid")
# 	return render(request,'events_afp/baserates.html',context)

# def register_deal(request):
# 	form = DealForm(request.POST or None)
# 	context = {"form":form}

# 	if request.method == "POST":
# 		print(request.POST)

# 		if form.is_valid():
# 			eff_rate 	= form.cleaned_data.get('eff_rate')
# 			frequency 	= form.cleaned_data.get('frequency')
# 			# total_sec 	= form.cleaned_data.get('total_sec')
# 			total_cost 	= form.cleaned_data.get('total_cost')

# 			channel_choice = form.cleaned_data.get('channel_choice')
# 			element_choice = form.cleaned_data.get('element_choice')

# 			obj = DealNFCT(eff_rate = eff_rate, frequency = frequency, total_sec = total_sec, total_cost = total_cost, base_rate = base_rate)
# 			obj.save()

# 		else:
# 			print("deal form invalid")
# 	return render(request,'events_afp/nfct_deal.html',context)



# def events_afp_final_deal(request):
# 	form1 = Events_dealform(request.POST or None)
# 	form2 = form_fct_deal(request.POST or None)
# 	form3 = NonFCTDealForm(request.POST or None)
# 	form4 = AFP_dealform(request.POST or None)

# 	context = {'form1':form1, 'form2':form2, 'form3':form3, 'form4':form4}
# 	# Events
# 	if request.method == "POST":
# 		if form1.is_valid():
# 			print(form1.cleaned_data)
# 			obj1 = Events_Deal()
# 			print("inside events")
# 			# for i in range(1,10):
# 			# 	event = ref + "_events" + str(i)
# 			# 	print(event)
# 				# obj.ref_event_pri_key = event
# 			# r = random.randint(1, 10)
# 			# ref_event_pri_key = "EventsAFP" + str(r)
# 			# e = Events_Deal.objects.filter(ref_event_pri_key__contains = ref_event_pri_key)
# 			# if e.exists():

# 			# obj.ref_event_pri_key = ref_event_pri_key

# 			obj1.ref_category_name = form1.cleaned_data.get('ref_category_name')
# 			obj1.description = form1.cleaned_data.get('description')
# 			obj1.ref_channels = form1.cleaned_data.get('ref_channels')
# 			obj1.merit_money = form1.cleaned_data.get('merit_money')

# 			obj1.save()
# 		else:
# 			print('Invalid form1')

# 	# fct
# 	if request.method == "POST":
# 		if form2.is_valid():
# 			fct_obj = fct_deal()
# 			print("inside fct")
# 			fct_obj.chan = request.POST.get('channel')
# 			fct_obj.dis = request.POST.get('dis_dd')
# 			fct_obj.band1 = request.POST.get('band1')
# 			fct_obj.band2 = request.POST.get('band2')
# 			fct_obj.band3 = request.POST.get('band3')
# 			fct_obj.fct1 = request.POST.get('fct1')
# 			fct_obj.fct2 = request.POST.get('fct2')
# 			fct_obj.fct3 = request.POST.get('fct3')
# 			fct_obj.eff_rate1 = request.POST.get('er1')
# 			fct_obj.eff_rate2 = request.POST.get('er2')
# 			fct_obj.eff_rate3 = request.POST.get('er3')
# 			fct_obj.rev1 = request.POST.get('rev1')
# 			fct_obj.rev2 = request.POST.get('rev2')
# 			fct_obj.rev3 = request.POST.get('rev3')
# 			fct_obj.total_rev = form2.cleaned_data.get('total_rev')
# 			fct_obj.save()
# 			print("inside!!!!!!!!")
# 		else:
# 			print("outside view")

# 	# nonfct
# 	if request.method == "POST":
# 		print(request.POST)

# 		if form3.is_valid():
# 			non_fct_obj = DealNFCT()
# 			non_fct_obj.seconds = request.POST.get('seconds')
# 			non_fct_obj.days = request.POST.get('days')
# 			non_fct_obj.months = request.POST.get('months')
# 			non_fct_obj.eff_rate 	= form3.cleaned_data.get('eff_rate')
# 			non_fct_obj.frequency 	= form3.cleaned_data.get('frequency')
# 			total_sec 	= request.POST.get('Totalsec')
# 			non_fct_obj.total_cost 	= request.POST.get('Total')

# 			non_fct_obj.channel_choice = form3.cleaned_data.get('channel_choice')
# 			non_fct_obj.element_choice = form3.cleaned_data.get('element_choice')

# 			obj.save()

# 		else:
# 			print("deal form invalid")

# 	# afp
# 	if request.method == "POST":
# 		if form4.is_valid():
# 			print(form4.cleaned_data)
# 			obj4 = AFP_Deal()
# 			print("inside form3")
# 			obj4.ref_program_name = form4.cleaned_data.get('ref_program_name')
# 			obj4.ref_channels = form4.cleaned_data.get('ref_channels')
# 			obj4.promos = form4.cleaned_data.get('promos')
# 			obj4.slot = form4.cleaned_data.get('slot')
# 			obj4.eff_rate = form4.cleaned_data.get('eff_rate')
# 			obj4.save()
# 		else:
# 			print('Invalid Form4')

# 	return render(request, 'events_afp/afp_deal.html', context)



def events(request):
	form1 = Events_dealform(request.POST or None)
	context = {'form1':form1}
	if request.method == "POST":
		if form1.is_valid():
			print(form1.cleaned_data)
			obj1 = Events_Deal()
			print("inside events")
			obj1.ref_category_name = form1.cleaned_data.get('ref_category_name')
			obj1.description = form1.cleaned_data.get('description')
			obj1.ref_channels = form1.cleaned_data.get('ref_channels')
			obj1.merit_money = form1.cleaned_data.get('merit_money')

			obj1.save()
		else:
			print('Invalid form1')
	return render(request,'events_afp/events.html',context )

def afp(request):
	form4 = AFP_dealform(request.POST or None)
	context = {'form4':form4}
	if request.method == "POST":
		if form4.is_valid():
			print(form4.cleaned_data)
			obj4 = AFP_Deal()
			print("inside form3")
			obj4.ref_program_name = form4.cleaned_data.get('ref_program_name')
			obj4.ref_channels = form4.cleaned_data.get('ref_channels')
			obj4.promos = form4.cleaned_data.get('promos')
			obj4.slot = form4.cleaned_data.get('slot')
			obj4.eff_rate = form4.cleaned_data.get('eff_rate')
			obj4.save()
		else:
			print('Invalid Form4')

	return render(request, 'events_afp/afp1.html', context)

def fct(request):
	form2 = form_fct_deal(request.POST or None)
	context = {'form2':form2}
	if request.method == "POST":
		if form2.is_valid():
			fct_obj = fct_deal()
			print("inside fct")
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
			fct_obj.total_rev = form2.cleaned_data.get('total_rev')
			fct_obj.save()
			print("inside!!!!!!!!")
		else:
			print("outside view")

	return render(request,'events_afp/fct1.html',context)




