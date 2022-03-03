from django.shortcuts import render, reverse
from django.http import HttpResponse
import requests
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.models import Employees



from .forms import (

    DealModelFormset,
    NFCT_Base_Rate_Form,
    NFCTGrandTotal,
    FinalNFCTForm,
)
from .models import *

# Create your views here.


class DealListView(generic.ListView):

    model = Deal_nfct
    context_object_name = 'nfct'
    template_name = 'list.html'


# @login_required(login_url='accounts:emp_login')
# def create_deal_model_form(request):
#     template_name = 'test.html'
#     if request.method == 'GET':
#         nfct_form = NFCTGrandTotal(request.POST or None)
#         formset = DealModelFormset(queryset=Deal_nfct.objects.none())
#         return render(request, template_name, {'formset': formset, 'nfct_form' : nfct_form})
#     elif request.method == 'POST':
#         nfct_form = NFCTGrandTotal(request.POST or None)
#         formset = DealModelFormset(request.POST or None)
#         if formset.is_valid():
#             # gt_obj = NFCTGrandTotal()
#             # gt_obj.nfct_grandtotal = request.POST.get('nfct_grandtotal')
#             # gt_obj.dealid_nfct_ref = request.POST.get('deal_id')
#             # formset.save(commit=False)
#             if nfct_form.is_valid():
#                 nfct_gt = Deal_nfct()
#                 print(request.POST, 'request*****************')
#                 nfct_gt.nfct_grandtotal = nfct_form.cleaned_data.get('nfct_grandtotal')
#                 print(nfct_gt.nfct_grandtotal, 'nfct_grandtotal')
#                 nfct_gt.save()
#             formset.save()
#             return redirect('nfct:deallist')
#         return render(request, template_name, {'formset': formset, 'nfct_form' : nfct_form})


@login_required(login_url='accounts:emp_login')
def eff_sec(request):
    print('inside eff_sec function')
    print(request.session['eff_seconds'])
    if 'eff_seconds' in request.session:
        eff_seconds = request.session['eff_seconds']
        print('eff_seconds', eff_seconds)
        return HttpResponse(eff_seconds)


@login_required(login_url='accounts:emp_login')
def nfct_enter_base_rate(request):
    nfct_form = NFCT_Base_Rate_Form(request.POST or None)
    nfct_obj = NFCT_Base_Rate()
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

    return render(request, 'nfct/nfct_base.html', context)


@login_required(login_url='accounts:emp_login')
def nfct_load_br(request):
    chan_id = request.GET.get('channel')
    print(request.GET)
    print(chan_id, 'Chan id')
    element = request.GET.get('element')
    print(element, '&&&&&&&&&&&&&&&&&&')
    print("**************************************************************")

    rates = NFCT_Base_Rate.objects.filter(channel__contains=chan_id)
    print(rates, '++++++++++++++')
    element_name = NFCT_Base_Rate.objects.filter(element__contains=element)
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

    y = NFCT_Base_Rate.objects.filter(nfct_unique_key__contains=x)
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


def nfct_finaldeal(request):
    form = FinalNFCTForm(request.POST or None)
    nfct_form = NFCT_Base_Rate_Form(request.POST or None)
    user = request.user
    ag_det = AgencyDetail.objects.all()
    cli_name = CustomerName.objects.all()
    cli_det = CustomerContact.objects.all()
    agg = AgencyContact.objects.all()
    qs1 = Employees.objects.filter(emp_email__contains=user)

    formset = DealModelFormset(queryset=Deal_nfct.objects.none())
    final_obj = FinalNFCT()
    context = {'form': form, 'ag_det': ag_det, 'cli_name': cli_name, 'cli_det': cli_det, 'agg': agg,'qs1': qs1,'formset': formset, 'nfct_form': nfct_form}
    grandtotal = []
    if request.method == 'POST':
        print("form errors--------------------", form.errors)
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
            formset = DealModelFormset(request.POST or None)
            
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
                nfct_total = int(nfct_total)
                final_obj.nfct_total = nfct_total
                final_obj.save()
                # form1.save(commit=True)
                # form.save(commit=True)
                formset.save()
                print("reached at the end---------------------")

                # return redirect('/final_deallist')
            

    return render(request, "test.html", context)


def load_client_contacts(request):
    client_id = request.GET.get('client')
    client_contacts = CustomerContact.objects.filter(
        ref_creg_no=client_id).order_by('pri_fname')
    print(client_contacts)
    return render(request, 'final_fct_nfct_deal/client_contact_dropdown_options.html', {'client_contacts': client_contacts})


def load_agency_contacts(request):
    agency_id = request.GET.get('agency')
    agency_contacts = AgencyContact.objects.filter(
        agency_details=agency_id).order_by('pri_firstName')
    print(agency_contacts)
    return render(request, 'final_fct_nfct_deal/agency_contact_dropdown_options.html', {'agency_contacts': agency_contacts})


# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse
# from django.views.generic import ListView, TemplateView
# from django.urls import reverse_lazy
# from django.shortcuts import redirect
# from .forms import *
# from .models import *
# from .models import NFCT_Base_Rate
# from django.forms import modelformset_factory


# Add Channel Names
# def nfct_chname(request):
# 	nfct_chan_form = NFCT_Chann(request.POST or None)

# 	context = {"nfct_chan_form" : nfct_chan_form}
# 	print(nfct_chan_form.is_valid())
# 	print(nfct_chan_form.errors)
# 	print(request.POST)

# 	if request.method == "POST":
# 		if nfct_chan_form.is_valid():
# 			print(nfct_chan_form.cleaned_data)
# 			nfct_chan_obj = NFCT_Channels()
# 			print("inside NFCT")
# 			nfct_chan_obj.nfct_channels = nfct_chan_form.cleaned_data.get('nfct_channels')
# 			print(nfct_chan_obj.nfct_channels)
# 			if NFCT_Channels.objects.filter(nfct_channels = 'nfct_channels').exists():
# 				ValidationError("Channel Already Exists")
# 			else:
# 				nfct_chan_obj.save()
# 		else:
# 			print("Invalid NFCT")
# 	return render(request, 'nfct/nfct_channel.html', context)

# # Add Element Names
# def nfct_elename(request):
# 	nfct_ele_form = NFCT_Elem(request.POST or None)

# 	context = {"nfct_ele_form" : nfct_ele_form}
# 	print(nfct_ele_form.is_valid())
# 	print(nfct_ele_form.errors)
# 	print(request.POST)

# 	if request.method == "POST":
# 		if nfct_ele_form.is_valid():
# 			print(nfct_ele_form.cleaned_data)
# 			nfct_ele_obj = NFCT_Elements()
# 			print("inside NFCT Elements")
# 			nfct_ele_obj.nfct_elements = nfct_ele_form.cleaned_data.get('nfct_elements')
# 			print(nfct_ele_obj.nfct_elements)
# 			if NFCT_Elements.objects.filter(nfct_elements = 'nfct_elements').exists():
# 				ValidationError("Element Already Exists")
# 			else:
# 				nfct_ele_obj.save()
# 		else:
# 			print("Invalid NFCT Elements")
# 	return render(request, 'nfct/nfct_element.html', context)


# # Add Base rates
# def nfct_enter_base_rate(request):
# 	nfct_form = NFCT_Base_Rate_Form(request.POST or None)
# 	nfct_obj = NFCT_Base_Rate()
# 	context = {'nfct_form':nfct_form}
# 	print(nfct_form.errors)
# 	print(request.POST)
# 	if request.method == 'POST':
# 		if nfct_form.is_valid():
# 			nfct_channels = nfct_form.cleaned_data.get('nfct_channels')
# 			# print(nfct_channels)

# 			nfct_elements = nfct_form.cleaned_data.get('nfct_elements')
# 			# print(nfct_elements)
# 			nfct_obj.nfct_baserate = nfct_form.cleaned_data.get('nfct_baserate')

# 			uni = str(nfct_channels) + str(nfct_elements)
# 			print(uni)
# 			nfct_obj.nfct_unique_key = uni

# 			print("----------",nfct_channels,nfct_elements,nfct_obj.nfct_baserate)
# 			print(request.POST, '*********************************')
# 			nfct_obj.save()

# 	return render(request,'nfct/nfct_base.html',context)

# # NFCT Deal form
# def nfct_deal_form(request):
# 	# nfct_deal = NFCT_deal(request.POST or None)
# 	nfct_obj1 = NFCTDeal()
# 	# context = {'nfct_deal' : nfct_deal}
# 	NFCT_dealformset = modelformset_factory(NFCTDeal, form = NFCT_deal, extra= 0)
# 	# print(nfct_deal.is_valid())
# 	# print(nfct_deal.errors)
# 	# print(request.POST)
# 	formset = NFCT_dealformset(queryset=NFCTDeal.objects.none())

# 	if request.method == 'POST':
# 		# if ((request.POST.get('ref_nfct_elements_id') == 'Aston') or (request.POST.get('ref_nfct_elements_id') == 'L Band')):
# 		formset = NFCT_dealformset(request.POST or None)
# 		print(request.POST, '&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
# 		if formset.is_valid():
# 			print(request.POST, '&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
# 			# for form in formset:
# 			# print(form.ref_nfct_channels_id, '**************************')

# 			# nfct_reference_no = ('nfct_reference_no')
# 			nfct_obj1.ref_nfct_channels_id = formset.cleaned_data.get('ref_nfct_channels_id')
# 			print(nfct_obj1.ref_nfct_channels_id, '*****************')
# 			nfct_obj1.ref_nfct_elements_id = formset.cleaned_data.get('ref_nfct_elements_id')

# 			nfct_obj1.effective_rate = request.POST.get('effective_rate')
# 			nfct_obj1.frequency = request.POST.get('frequency')
# 			nfct_obj1.total_seconds =formset.cleaned_data.get('total_seconds')
# 			nfct_obj1.base_rate = request.POST.get('base_rate')
# 			nfct_obj1.nfct_total = formset.cleaned_data.get('nfct_total')

# 			form.save()
# 		# else:
# 		# 		# nfct_reference_no = ('nfct_reference_no')
# 		# 	# ref_nfct_channels_id = nfct_deal.cleaned_data.get('ref_nfct_channels_id')
# 		# 	# ref_nfct_elements_id = nfct_deal.cleaned_data.get('ref_nfct_elements_id')
# 		# 	# durations = nfct_deal.cleaned_data.get('durations')
# 		# 	# duration_in = nfct_deal.cleaned_data.get('duration_in')

# 		# 	# frequency = request.POST.get('frequency')
# 		# 	# base_rate = request.POST.get('base_rate')
# 		# 	# nfct_total = nfct_deal.cleaned_data.get('nfct_total')

# 		# 	formset.save()
# 	return render(request, 'nfct/nfct_deal.html', {'formset': formset})

# def nfct_load_br(request):
# 	chan_id = request.GET.get('channel')
# 	print(chan_id, 'Chan id')
# 	element = request.GET.get('element')
# 	print(element, '&&&&&&&&&&&&&&&&&&')
# 	print("**************************************************************")

# 	rates = NFCT_Channels.objects.filter(nfct_channels__contains=chan_id)
# 	print(rates, '++++++++++++++')

# 	element_name = NFCT_Elements.objects.filter(nfct_elements__contains=element)
# 	print(element_name, '++++++++++++++++++++')

# 	context1 = {'qs':rates}
# 	context2 = {'qs1':element_name}

# 	print("CONTEXT1", context1)
# 	print("CONTEXT2", context2)

# 	for i in context1['qs']:
# 		c = i.nfct_channels
# 		print("------",c)

# 	for j in context2['qs1']:
# 		b = j.nfct_elements
# 		print("------",b)


# 	x = c + b
# 	print("*************",x)

# 	y = NFCT_Base_Rate.objects.filter(nfct_unique_key__contains=x)
# 	print("*************",y)

# 	for k in y:
# 		# print(k)
# 		nfctbaserate = k.nfct_baserate
# 		print(nfctbaserate, '0000000000000000')
# 	# return '200'
# 	mycontext = {'nfctbaserate': nfctbaserate}
# 	return render(request,'nfct_deal.html',mycontext)


# class NFCT_Deal(ListView):
# 	model = NFCTDeal
# 	template_name = 'nfct_list.html'


# class Add_NFCT_Deal(TemplateView):
# 	nfct_obj1 = NFCTDeal()
# 	model = NFCTDeal
# 	template_name = 'nfct_deal.html'
# 	def get(self, *args, **kwargs):
# 		formset = NFCTDealFormSet(queryset = NFCTDeal.objects.none())
# 		return self.render_to_response({'nfct_deal_formset':formset})

# 	def post(self, *args, **kwargs):
# 		formset = NFCTDealFormSet(data = self.request.POST)
# 		if formset.is_valid():
# 			print(request.POST, 'request.POST')
# 			# if ((request.POST.get('ref_nfct_elements_id') == 'Aston') or (request.POST.get('ref_nfct_elements_id') == 'L Band')):
# 			# 	nfct_obj1.ref_nfct_channels_id = formset.cleaned_data.get('ref_nfct_channels_id')
# 			# 	print(nfct_obj1.ref_nfct_channels_id, '*****************')
# 			# 	nfct_obj1.ref_nfct_elements_id = formset.cleaned_data.get('ref_nfct_elements_id')

# 			# 	nfct_obj1.effective_rate = request.POST.get('effective_rate')
# 			# 	nfct_obj1.frequency = request.POST.get('frequency')
# 			# 	nfct_obj1.total_seconds =formset.cleaned_data.get('total_seconds')
# 			# 	nfct_obj1.base_rate = request.POST.get('base_rate')
# 			# 	nfct_obj1.nfct_total = formset.cleaned_data.get('nfct_total')

# 			# 	formset.save()
# 			# else:
# 			# 	# nfct_reference_no = ('nfct_reference_no')
# 			# 	ref_nfct_channels_id = nfct_deal.cleaned_data.get('ref_nfct_channels_id')
# 			# 	ref_nfct_elements_id = nfct_deal.cleaned_data.get('ref_nfct_elements_id')
# 			# 	durations = nfct_deal.cleaned_data.get('durations')
# 			# 	duration_in = nfct_deal.cleaned_data.get('duration_in')

# 			# 	frequency = request.POST.get('frequency')
# 			# 	base_rate = request.POST.get('base_rate')
# 			# 	nfct_total = nfct_deal.cleaned_data.get('nfct_total')

# 			formset.save()
# 			return redirect('/nfct/')
# 		return self.render_to_response({'nfct_deal_formset':formset})
