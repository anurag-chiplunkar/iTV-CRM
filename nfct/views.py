from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import *
from .models import *
from django.forms import modelformset_factory



# Add Channel Names
def nfct_chname(request):
	nfct_chan_form = NFCT_Chann(request.POST or None)

	context = {"nfct_chan_form" : nfct_chan_form}
	print(nfct_chan_form.is_valid())
	print(nfct_chan_form.errors)
	print(request.POST)

	if request.method == "POST":
		if nfct_chan_form.is_valid():
			print(nfct_chan_form.cleaned_data)
			nfct_chan_obj = NFCT_Channels()
			print("inside NFCT")
			nfct_chan_obj.nfct_channels = nfct_chan_form.cleaned_data.get('nfct_channels')
			print(nfct_chan_obj.nfct_channels)
			if NFCT_Channels.objects.filter(nfct_channels = 'nfct_channels').exists():
				ValidationError("Channel Already Exists")
			else:
				nfct_chan_obj.save()
		else:
			print("Invalid NFCT")
	return render(request, 'nfct/nfct_channel.html', context)

# Add Element Names
def nfct_elename(request):
	nfct_ele_form = NFCT_Elem(request.POST or None)

	context = {"nfct_ele_form" : nfct_ele_form}
	print(nfct_ele_form.is_valid())
	print(nfct_ele_form.errors)
	print(request.POST)

	if request.method == "POST":
		if nfct_ele_form.is_valid():
			print(nfct_ele_form.cleaned_data)
			nfct_ele_obj = NFCT_Elements()
			print("inside NFCT Elements")
			nfct_ele_obj.nfct_elements = nfct_ele_form.cleaned_data.get('nfct_elements')
			print(nfct_ele_obj.nfct_elements)
			if NFCT_Elements.objects.filter(nfct_elements = 'nfct_elements').exists():
				ValidationError("Element Already Exists")
			else:
				nfct_ele_obj.save()
		else:
			print("Invalid NFCT Elements")
	return render(request, 'nfct/nfct_element.html', context)


# Add Base rates
def nfct_enter_base_rate(request):
	nfct_form = NFCT_Base_Rate_Form(request.POST or None)
	nfct_obj = NFCT_Base_Rate()
	context = {'nfct_form':nfct_form}
	print(nfct_form.errors)
	print(request.POST)
	if request.method == 'POST':
		if nfct_form.is_valid():
			nfct_channels = nfct_form.cleaned_data.get('nfct_channels')
			# print(nfct_channels)

			nfct_elements = nfct_form.cleaned_data.get('nfct_elements')
			# print(nfct_elements)
			nfct_obj.nfct_baserate = nfct_form.cleaned_data.get('nfct_baserate')

			uni = str(nfct_channels) + str(nfct_elements)
			print(uni)
			nfct_obj.nfct_unique_key = uni

			print("----------",nfct_channels,nfct_elements,nfct_obj.nfct_baserate)
			print(request.POST, '*********************************')
			nfct_obj.save()

	return render(request,'nfct/nfct_base.html',context)

# NFCT Deal form
def nfct_deal_form(request):
	# nfct_deal = NFCT_deal(request.POST or None)
	nfct_obj1 = NFCTDeal()
	# context = {'nfct_deal' : nfct_deal}
	NFCT_dealformset = modelformset_factory(NFCTDeal, form = NFCT_deal, extra= 0)
	# print(nfct_deal.is_valid())
	# print(nfct_deal.errors)
	# print(request.POST)
	formset = NFCT_dealformset(queryset=NFCTDeal.objects.none())

	if request.method == 'POST':
		# if ((request.POST.get('ref_nfct_elements_id') == 'Aston') or (request.POST.get('ref_nfct_elements_id') == 'L Band')):
		formset = NFCT_dealformset(request.POST or None)
		print(request.POST, '&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
		if formset.is_valid():
			print(request.POST, '&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
			# for form in formset:
			# print(form.ref_nfct_channels_id, '**************************')

			# nfct_reference_no = ('nfct_reference_no')
			nfct_obj1.ref_nfct_channels_id = formset.cleaned_data.get('ref_nfct_channels_id')
			print(nfct_obj1.ref_nfct_channels_id, '*****************')
			nfct_obj1.ref_nfct_elements_id = formset.cleaned_data.get('ref_nfct_elements_id')

			nfct_obj1.effective_rate = request.POST.get('effective_rate')
			nfct_obj1.frequency = request.POST.get('frequency')
			nfct_obj1.total_seconds =formset.cleaned_data.get('total_seconds')
			nfct_obj1.base_rate = request.POST.get('base_rate')
			nfct_obj1.nfct_total = formset.cleaned_data.get('nfct_total')

			form.save()
		# else:
		# 		# nfct_reference_no = ('nfct_reference_no')
		# 	# ref_nfct_channels_id = nfct_deal.cleaned_data.get('ref_nfct_channels_id')
		# 	# ref_nfct_elements_id = nfct_deal.cleaned_data.get('ref_nfct_elements_id')
		# 	# durations = nfct_deal.cleaned_data.get('durations')
		# 	# duration_in = nfct_deal.cleaned_data.get('duration_in')

		# 	# frequency = request.POST.get('frequency')
		# 	# base_rate = request.POST.get('base_rate')
		# 	# nfct_total = nfct_deal.cleaned_data.get('nfct_total')

		# 	formset.save()
	return render(request, 'nfct/nfct_deal.html', {'formset': formset})

def nfct_load_br(request):

	chan_id = request.GET.get('channel')
	print(request.GET)
	print(chan_id, '*******************')
	element = request.GET.get('element')
	print(element, '&&&&&&&&&&&&&&&&&&')
	print("9999",chan_id,element)
	rates = NFCT_Channels.objects.filter(nfct_channels__contains=chan_id)
	print(rates, '++++++++++++++')
	element_name = NFCT_Elements.objects.filter(nfct_elements__contains=element)
	print(element_name, '++++++++++++++++++++')
	context1 = {'qs':rates}
	context2 = {'qs1':element_name}
	for i in context1['qs']:
		print(i, 'iiiiiiiiiiiiiiiiiiiiiii')
		c = i.nfct_channels
		print("------",c)

	for j in context2['qs1']:
		b = j.nfct_elements
		print("---****---",b)
	x = c + b 
	print("*************",x)
	y = NFCT_Base_Rate.objects.filter(nfct_unique_key__contains=x)
	# print(y, '++++++++++++++++++++++++')
	for k in y:
		# print(k)
		nfctbaserate = k.nfct_baserate
		print(nfctbaserate, '0000000000000000')
	return render(request,'nfct/nfct_deal.html',{'nfctbaserate': nfctbaserate})


def nfctformset(request):
	NFCT_dealformset = modelformset_factory(NFCTDeal, form = NFCT_deal, extra= 0)
	
	# formset = NFCT_dealformset(request.POST or None)
	# obj = NFCTDeal()
	#formset = NFCT_dealformset(request.POST or None)
    #formset1 = NFCT_dealformset()
	# formset = NFCT_dealformset(queryset=NFCTDeal.objects.filter(ref_nfct_channels_id='-1'))
	# NFCT_dealFormSet = inlineformset_factory()
	formset = NFCT_dealformset(queryset=NFCTDeal.objects.none())
	if request.method == 'POST':
		if ((request.POST.get('ref_nfct_elements_id') == 'Aston') or (request.POST.get('ref_nfct_elements_id') == 'L Band')):
			if formset.is_valid():
				
				obj.ref_nfct_channels_id = nfct_deal.cleaned_data.get('ref_nfct_channels_id')
				obj.ref_nfct_elements_id = nfct_deal.cleaned_data.get('ref_nfct_elements_id')

				obj.effective_rate = request.POST.get('effective_rate')
				obj.frequency = request.POST.get('frequency')
				obj.total_seconds =nfct_deal.cleaned_data.get('total_seconds')
				obj.base_rate = request.POST.get('base_rate')
				obj.nfct_total = nfct_deal.cleaned_data.get('nfct_total')

				obj.save()
		else:
				# nfct_reference_no = ('nfct_reference_no')
			obj.ref_nfct_channels_id = nfct_deal.cleaned_data.get('ref_nfct_channels_id')
			obj.ref_nfct_elements_id = nfct_deal.cleaned_data.get('ref_nfct_elements_id')
			obj.durations = nfct_deal.cleaned_data.get('durations')
			obj.duration_in = nfct_deal.cleaned_data.get('duration_in')

			obj.frequency = request.POST.get('frequency')
			obj.base_rate = request.POST.get('base_rate')
			obj.nfct_total = nfct_deal.cleaned_data.get('nfct_total')

			obj.save()
	return render(request, 'nfct/formset.html', {'formset':formset})


class NFCT_Deal(ListView):
	model = NFCTDeal
	template_name = 'nfct_list.html'


class Add_NFCT_Deal(TemplateView):
	nfct_obj1 = NFCTDeal()
	model = NFCTDeal
	template_name = 'nfct_deal.html'
	def get(self, *args, **kwargs):
		formset = NFCTDealFormSet(queryset = NFCTDeal.objects.none())
		return self.render_to_response({'nfct_deal_formset':formset})

	def post(self, *args, **kwargs):
		formset = NFCTDealFormSet(data = self.request.POST)
		if formset.is_valid():
			# if ((request.POST.get('ref_nfct_elements_id') == 'Aston') or (request.POST.get('ref_nfct_elements_id') == 'L Band')):
			# 	nfct_obj1.ref_nfct_channels_id = formset.cleaned_data.get('ref_nfct_channels_id')
			# 	print(nfct_obj1.ref_nfct_channels_id, '*****************')
			# 	nfct_obj1.ref_nfct_elements_id = formset.cleaned_data.get('ref_nfct_elements_id')

			# 	nfct_obj1.effective_rate = request.POST.get('effective_rate')
			# 	nfct_obj1.frequency = request.POST.get('frequency')
			# 	nfct_obj1.total_seconds =formset.cleaned_data.get('total_seconds')
			# 	nfct_obj1.base_rate = request.POST.get('base_rate')
			# 	nfct_obj1.nfct_total = formset.cleaned_data.get('nfct_total')

			# 	formset.save()
			# else:
			# 	# nfct_reference_no = ('nfct_reference_no')
			# 	ref_nfct_channels_id = nfct_deal.cleaned_data.get('ref_nfct_channels_id')
			# 	ref_nfct_elements_id = nfct_deal.cleaned_data.get('ref_nfct_elements_id')
			# 	durations = nfct_deal.cleaned_data.get('durations')
			# 	duration_in = nfct_deal.cleaned_data.get('duration_in')

			# 	frequency = request.POST.get('frequency')
			# 	base_rate = request.POST.get('base_rate')
			# 	nfct_total = nfct_deal.cleaned_data.get('nfct_total')

			formset.save()
			return redirect('/nfct/')
		return self.render_to_response({'nfct_deal_formset':formset})
