from django import forms
from django.contrib.auth import get_user_model
from . models import Deal_one
from customer.models import CustomerName,CustomerContact
from agency.models import AgencyDetail,AgencyContact
from plan.models import Plan
from item.models import Item,SubItem
import calculation




User = get_user_model()
base_rate_choices = [(700,700),(500,500),(400,400)]

class Deal_details(forms.Form):

	
	customer_id 	= forms.ModelChoiceField(queryset = CustomerName.objects.all(),widget = forms.Select(attrs = {"class":"form-select"}))
	customer_contact= forms.ModelChoiceField(queryset = CustomerContact.objects.all(),widget = forms.Select(attrs = {"class":"form-select"}))

	agency_id 		= forms.ModelChoiceField(queryset = AgencyDetail.objects.all(),widget = forms.Select(attrs = {"class":"form-select"}))
	agency_contact  = forms.ModelChoiceField(queryset = AgencyContact.objects.all(),widget = forms.Select(attrs = {"class":"form-select"}))

	plan_id 		= forms.ModelChoiceField(queryset = Plan.objects.all(),widget = forms.Select(attrs = {"class":"form-select"}) )

	item_id			= forms.ModelChoiceField(queryset = Item.objects.all(),widget = forms.Select(attrs = {"class":"form-select"}))
	
	#below is for "bands"
	subitem_id1		= forms.ModelChoiceField(queryset = SubItem.objects.all(),widget = forms.Select(attrs = {"class":"form-select"}))
	subitem_id2		= forms.ModelChoiceField(queryset = SubItem.objects.all(),widget = forms.Select(attrs = {"class":"form-select"}))
	subitem_id3		= forms.ModelChoiceField(queryset = SubItem.objects.all(),widget = forms.Select(attrs = {"class":"form-select"}))

	base_rate1      = forms.ChoiceField(choices = base_rate_choices,widget = forms.Select(attrs = {"class":"form-select"}))
	base_rate2       = forms.ChoiceField(choices = base_rate_choices,widget = forms.Select(attrs = {"class":"form-select"}))
	base_rate3       = forms.ChoiceField(choices = base_rate_choices,widget = forms.Select(attrs = {"class":"form-select"}))

	fct1 			= forms.IntegerField(
					widget = forms.NumberInput(
					attrs = {
						"class":"form-control",
						"id":"form",
						"placeholder":"Enter FCT"
						}))

	fct2 			= forms.IntegerField(
					widget = forms.NumberInput(
					attrs = {
						"class":"form-control",
						"id":"form",
						"placeholder":"Enter FCT"
						}))


	fct3 			= forms.IntegerField(
						widget = forms.NumberInput(
						attrs = {
							"class":"form-control",
							"id":"form",
							"placeholder":"Enter FCT"
						}))


	eff_rate1		= forms.IntegerField(
					widget = forms.NumberInput(
					attrs = {
						"class":"form-control",
						"id":"form",
						"placeholder":"Enter eff rate"
						}))

	eff_rate2		= forms.IntegerField(
					widget = forms.NumberInput(
					attrs = {
						"class":"form-control",
						"id":"form",
						"placeholder":"Enter eff rate"
						}))
	eff_rate3		= forms.IntegerField(
					widget = forms.NumberInput(
					attrs = {
						"class":"form-control",
						"id":"form",
						"placeholder":"Enter eff rate"
						}))



	slot1		= forms.IntegerField(
					widget = forms.NumberInput(
					attrs = {
						"class":"form-control",
						"id":"form",
						"placeholder":"Enter slot"
						}))
	slot2		= forms.IntegerField(
					widget = forms.NumberInput(
					attrs = {
						"class":"form-control",
						"id":"form",
						"placeholder":"Enter slot"
						}))
	slot3		= forms.IntegerField(
					widget = forms.NumberInput(
					attrs = {
						"class":"form-control",
						"id":"form",
						"placeholder":"Enter slot"
						}))

	actual_fct1 			= forms.IntegerField(widget = calculation.FormulaInput(('(fct1*eff_rate1)/slot1')))
	actual_fct2 			= forms.IntegerField(widget = calculation.FormulaInput(('(fct2*eff_rate2)/slot2')))
	actual_fct3 			= forms.IntegerField(widget = calculation.FormulaInput(('(fct3*eff_rate3)/slot3')))


	total_fct	= forms.IntegerField(
					widget = calculation.FormulaInput('actual_fct1+actual_fct2+actual_fct3'))

