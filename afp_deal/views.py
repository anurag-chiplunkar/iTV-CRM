from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import *
from . models import *
from accounts.models import *
import random
import json
from django.core import serializers
from django.contrib.auth.decorators import login_required

@login_required(login_url='accounts:emp_login')
def afp_program_name(request):
	"""Docstring for saving AFP programme names in database

	:object: AFPProgramName

	:return: request, context(form) and template"""

	program_name_form = AFP_Program(request.POST or None)
	context = {"program_name_form" : program_name_form}
	print(program_name_form.is_valid())
	print(program_name_form.errors)
	print(request.POST)

	if request.method == "POST":
		if program_name_form.is_valid():
			programNameObj = AFPProgramName()
			programNameObj.program_name = program_name_form.cleaned_data.get('program_name')
			programNameObj.save()
		else:
			print("Invalid program_name_form")
	return render(request, 'afp_deal/afp_program_names.html', context)

@login_required(login_url='accounts:emp_login')
def afp_channel_name(request):
	"""Docstring for saving AFP channel names in database
	
	:object: AFPChannels

	:return: request, context(form) and template"""

	channel_name_form = AFP_Channel(request.POST or None)
	context = {"channel_name_form" : channel_name_form}
	print(channel_name_form.is_valid())
	print(channel_name_form.errors)
	print(request.POST)

	if request.method == "POST":
		if channel_name_form.is_valid():
			channelNameObj = AFPChannels()
			channelNameObj.channels = channel_name_form.cleaned_data.get('channels')
			channelNameObj.save()
		else:
			print("Invalid channel_name_form")
	return render(request, 'afp_deal/afp_channel_names.html', context)

@login_required(login_url='accounts:emp_login')
def afp_promo_name(request):
	"""Docstring for saving AFP promo names in database
	
	:object: AFPPromos

	:return: request, context(form) and template"""

	promo_name_form = AFP_Promo(request.POST or None)
	context = {"promo_name_form" : promo_name_form}
	print(promo_name_form.is_valid())
	print(promo_name_form.errors)
	print(request.POST)

	if request.method == "POST":
		if promo_name_form.is_valid():
			promoNameObj = AFPPromos()
			promoNameObj.promos = promo_name_form.cleaned_data.get('promos')
			promoNameObj.save()
		else:
			print("Invalid promo_name_form")
	return render(request, 'afp_deal/afp_promo_names.html', context)

@login_required(login_url='accounts:emp_login')
def afp_slot_name(request):
	"""Docstring for saving AFP slot names in database
	
	:object: AFPSlots

	:return: request, context(form) and template"""

	slot_name_form = AFP_Slot(request.POST or None)
	context = {"slot_name_form" : slot_name_form}
	print(slot_name_form.is_valid())
	print(slot_name_form.errors)
	print(request.POST)

	if request.method == "POST":
		if slot_name_form.is_valid():
			slotNameObj = AFPSlots()
			slotNameObj.slot = slot_name_form.cleaned_data.get('slot')
			slotNameObj.save()
		else:
			print("Invalid slot_name_form")
	return render(request, 'afp_deal/afp_slot_names.html', context)

@login_required(login_url='accounts:emp_login')
def afp_br(request):
	"""Docstring for saving AFP base rates in database
	
	:object: AFPBaseRate

	:return: request, context(form) and template"""

	br_form = AFP_Base_Rate_Form(request.POST or None)
	context = {"br_form" : br_form}
	print(br_form.is_valid())
	print(br_form.errors)
	print(request.POST)

	if request.method == "POST":
		if br_form.is_valid():
			brObj = AFPBaseRate()
			brObj.ref_program_name  = br_form.cleaned_data.get('ref_program_name')
			brObj.ref_channels     	= br_form.cleaned_data.get('ref_channels')
			brObj.baserate          = br_form.cleaned_data.get('baserate')
			brObj.br_unique_key           = str(brObj.ref_program_name) + str(brObj.ref_channels)
			brObj.save()
		else:
			print("Invalid br_form")
	return render(request, 'afp_deal/afp_baserates.html', context)

# def afp_deal(request):
# 	afp_deal_form = AFP_Deal_Form(request.POST or None)
# 	context = {"afp_deal_form" : afp_deal_form}
# 	print(afp_deal_form.is_valid())
# 	print(afp_deal_form.errors)
# 	print(request.POST)

# 	if request.method == "POST":
# 		if afp_deal_form.is_valid():
# 			dealObj = AFPDeal()
			
# 			dealObj.afp_deal_id 		= random.randint(1,100)
# 			dealObj.ref_program_name    = afp_deal_form.cleaned_data.get('ref_program_name')
# 			dealObj.ref_channels        = afp_deal_form.cleaned_data.get('ref_channels')
# 			dealObj.ref_promos          = afp_deal_form.cleaned_data.get('ref_promos')
# 			dealObj.ref_slot           	= afp_deal_form.cleaned_data.get('ref_slot')
# 			dealObj.afp_eff_rate        = afp_deal_form.cleaned_data.get('afp_eff_rate')
# 			dealObj.afp_base_rate       = request.POST.get('afp_baserate')
# 			dealObj.total               = dealObj.afp_eff_rate

# 			dealObj.save()
# 		else:
# 			print("Invalid br_form")
# 	return render(request, 'afp_deal/afp_deal.html', context)

@login_required(login_url='accounts:emp_login')
def AFPDealListView(request):
	"""Docstring for AFP deals list view

	:model name: FinalAFPDeal, AFPDealFinalTotal

	:return: request, template and context(all deal records of AFP and AFP total)
	"""

	afp_deals 	= FinalAFPDeal.objects.all()
	afp_totals = AFPDealFinalTotal.objects.all()
	print(afp_totals)
	mycontext = {'afp_deals': afp_deals, 'afp_totals': afp_totals}
	template_name = 'afp_deal/afp_final_deallist.html'
	return render(request, template_name, mycontext)

@login_required(login_url='accounts:emp_login')
def load_afp_client_contacts(request):
	"""Docstring for displaying client contact with respect to client name
	
	:model name: CustomerContact

	:return: request, template and context"""

	client_id = request.GET.get('client')
	print(client_id)
	client_contacts = CustomerContact.objects.filter(ref_creg_no=client_id).order_by('pri_fname')
	print(client_contacts)
	return render(request, 'afp_deal/afp_client_contact_dropdown_options.html', {'client_contacts': client_contacts})

@login_required(login_url='accounts:emp_login')
def load_afp_agency_contacts(request):
	"""Docstring for displaying agency contact with respect to agency name
	
	:model: AgencyContact

	:return: request, template and context"""

	agency_id = request.GET.get('agency')
	agency_contacts = AgencyContact.objects.filter(
        agency_details=agency_id).order_by('pri_firstName')
	print(agency_contacts)
	return render(request, 'afp_deal/afp_agency_contact_dropdown_options.html', {'agency_contacts': agency_contacts})

@login_required(login_url='accounts:emp_login')
def load_afp_agency_client(request):
	"""Docstring for displaying agency name wrt client name
	
	:model name: AgencyDetail

	:return: request, template and context"""

	cli_id = request.GET.get('client')
	print('CLIENT', cli_id)
	agency = AgencyDetail.objects.filter(ccreg_no=cli_id).order_by('agency_name')
	print(agency)
	return render(request, 'afp_deal/afp_agency_client_dropdown_options.html', {'agency': agency})

@login_required(login_url='accounts:emp_login')
def create_afp_deal(request):
	"""Docstring for creating a AFP deal
	
	:model name: Employees, AgencyDetail, CustomerName, CustomerContact, AgencyContact, AFPDealFinalTotal, FinalAFPDeal

	:return: request, template and context"""

	##for taking the current logged in user
	user = request.user
	emp_qs = Employees.objects.filter(emp_email__contains=user)

	##for dynamic contact details
	ag_det = AgencyDetail.objects.all()
	cli_name = CustomerName.objects.all()
	cli_det = CustomerContact.objects.all()
	agg = AgencyContact.objects.all()
	tmpJson = serializers.serialize("json", cli_det)
	tmpagen = serializers.serialize("json", agg)

	template_name = 'myafpdemo.html'
	if request.method == 'GET':
		common_form = FinalAFPDealDetails(request.POST or None)
		formset = AFPDealModelFormset(queryset = AFPDeal.objects.none())
		return render(request, template_name, {'formset': formset,'common_form':common_form,'emp_qs':emp_qs, 'ag_det': ag_det, 'cli_name': cli_name, 'cli_det': cli_det, 'agg': agg, 'tmpJson': tmpJson,'tmpagen': tmpagen})
	elif request.method == 'POST':
		print(request.POST)
		common_form = FinalAFPDealDetails(request.POST or None)
		formset = AFPDealModelFormset(request.POST or None)
		print(formset.errors)
		print(common_form.errors)
		if formset.is_valid():
			for f in formset.forms:
				obj = f.save(commit=False)
				obj.afp_deal_id = request.POST.get('afpdeal_id')
				obj.save()
				print("Saved")

			print("INSIDE TOTAL FORM")
			afpTotalObj = AFPDealFinalTotal()
			afpFinalDealObj = FinalAFPDeal()

			##for saving only total
			afpTotalObj.afp_final_total = request.POST.get('afp_deal_total')
			afpTotalObj.afp_final_deal_id = request.POST.get('afpdeal_id')
			print("OUR TOTAL:",afpTotalObj.afp_final_total)
			print("OUR DEAL ID:",afpTotalObj.afp_final_deal_id)
			afpTotalObj.save()
			
			##for saving the final deal
			if common_form.is_valid():
				print('INSIDE COMMON FORM')
				afpFinalDealObj.afpdeal_id = request.POST.get('afpdeal_id')
				afpFinalDealObj.afp_ro_number = common_form.cleaned_data.get('afp_ro_number')
				afpFinalDealObj.afp_ro_value = common_form.cleaned_data.get('afp_ro_value')
				afpFinalDealObj.afp_client_name_ref = common_form.cleaned_data.get('afp_client_name_ref')
				afpFinalDealObj.afp_client_contact_ref = common_form.cleaned_data.get('afp_client_contact_ref')
				afpFinalDealObj.afp_agency_name_ref = common_form.cleaned_data.get('afp_agency_name_ref')
				afpFinalDealObj.afp_agency_contact_ref = common_form.cleaned_data.get('afp_agency_contact_ref')
				afpFinalDealObj.afp_brand_name_ref = common_form.cleaned_data.get('afp_brand_name_ref')
				afpFinalDealObj.afp_total_ref = request.POST.get('afp_deal_total')
				
				afpFinalDealObj.save()
			else:
				print("COMMON FORM INVALID")

	
			formset.save()
			return redirect('/afp_final_deallist')
		return render(request, template_name, {'formset': formset,'common_form':common_form,'emp_qs':emp_qs, 'ag_det': ag_det, 'cli_name': cli_name, 'cli_det': cli_det, 'agg': agg, 'tmpJson': tmpJson,'tmpagen': tmpagen})

@login_required(login_url='accounts:emp_login')
def afp_deal_load_br(request):
	"""Docstring for displaying AFP base rate based on channel and programme name
	
	:model name: AFPChannels, AFPProgramName
	
	:return: base rate"""
	
	print(request.GET)
	afp_program_id 	= request.GET.get('program_name')
	print(afp_program_id)
	afp_channel_id 	= request.GET.get('channel')
	print(afp_channel_id)
	afp_chan 		= AFPChannels.objects.filter(channels__contains = afp_channel_id)
	afp_prog 		= AFPProgramName.objects.filter(program_name__contains = afp_program_id)
	context1 = {'qs1': afp_chan}
	context2 = {'qs2': afp_prog}

	##getting the filter channel from the form
	for ele1 in context1['qs1']:
		c = ele1.channels
		print("OUR CHANNEL:", c)

	##getting the filtered program name from the form
	for ele2 in context2['qs2']:
		p = ele2.program_name
		print("OUR PROGRAM:", p)
  
	##duplicating the unique key that we have saved in the master data, for that particular base rate
	our_unique_key = p+c
	print("OUR UNIQUE KEY:",our_unique_key)

	##filtering that base rate in our model
	rate = AFPBaseRate.objects.filter(br_unique_key = our_unique_key)

	for br in rate:
		our_baserate = br.baserate
		print(our_baserate)
	r = {'our_baserate': our_baserate}
	print("OUR BASE RATE", r)
	return HttpResponse(our_baserate)
