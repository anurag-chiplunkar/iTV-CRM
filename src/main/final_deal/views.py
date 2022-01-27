from django.shortcuts import render
from django.forms import formset_factory
from . forms import Deal_details
from . models import Deal_one



def deal_detail(request):
	form = Deal_details(request.POST or None) 	
	print(request.method)
	print(request.POST)
	context = {"form":form}

	if form.is_valid():

		customer_id 	= form.cleaned_data.get('customer_id')
		customer_contact = form.cleaned_data.get('customer_contact')
		agency_id 		= form.cleaned_data.get('agency_id')
		agency_contact  = form.cleaned_data.get('agency_contact')
		plan_id			= form.cleaned_data.get('plan_id')	##dispersion
		item_id			= form.cleaned_data.get('item_id')	##fct

		subitem_id1		= form.cleaned_data.get('subitem_id1')	##band1
		subitem_id2		= form.cleaned_data.get('subitem_id2')	##band1
		subitem_id3		= form.cleaned_data.get('subitem_id3')	##band1


		fct1			= form.cleaned_data.get('fct1')			##FCT = 10 for example
		eff_rate1		= form.cleaned_data.get('eff_rate1')    ##eff rate
		base_rate1		= form.cleaned_data.get('base_rate1')
		slot1			= form.cleaned_data.get('slot1')		##slot = 15  for example
		actual_fct1		= form.cleaned_data.get('actual_fct1')	##calculated field
		# total_fct1		= form.cleaned_data.get('total_fct1')


		fct2			= form.cleaned_data.get('fct2')
		eff_rate2		= form.cleaned_data.get('eff_rate2')
		base_rate2		= form.cleaned_data.get('base_rate2')
		slot2			= form.cleaned_data.get('slot2')		##slot = 15  for example
		actual_fct2		= form.cleaned_data.get('actual_fct2')	##calculated field
		# total_fct2		= form.cleaned_data.get('total_fct2')


		fct3			= form.cleaned_data.get('fct3')
		eff_rate3		= form.cleaned_data.get('eff_rate3')
		base_rate3		= form.cleaned_data.get('base_rate3')
		slot3			= form.cleaned_data.get('slot3')		##slot = 15  for example
		actual_fct3		= form.cleaned_data.get('actual_fct3')	##calculated field

		# total_fct		= form.cleaned_data.get('total_fct')

		obj = Deal_one(customer_id=customer_id,
					customer_contact=customer_contact,
					agency_id=agency_id,
					agency_contact=agency_contact,
					plan_id=plan_id,
					item_id=item_id,
					subitem_id1=subitem_id1,
					subitem_id2=subitem_id2,
					subitem_id3=subitem_id3,

					fct1=fct1,
					eff_rate1=eff_rate1,
					base_rate1=base_rate1,
					slot1=slot1,
					actual_fct1=actual_fct1,
					# total_fct1=total_fct1,


					fct2=fct2,
					eff_rate2=eff_rate2,
					base_rate2=base_rate2,
					slot2=slot2,
					actual_fct2=actual_fct2,
					# total_fct2=total_fct2,


					fct3=fct3,
					eff_rate3=eff_rate3,
					base_rate3=base_rate3,
					slot3=slot3,
					actual_fct3=actual_fct3,

					# total_fct=total_fct
					)

		obj.save()


	return render(request,'final_deal/deal_details.html',context)