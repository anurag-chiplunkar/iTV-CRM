from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.forms import (formset_factory, modelformset_factory)
from . models import *

class FinalFctNfctDealDetails(forms.ModelForm):
	client_name_ref 	= forms.ModelChoiceField(queryset = CustomerName.objects.all(),widget = forms.Select(attrs = {'class':'custom-select'}), empty_label='Select the Client Name')
	client_contact_ref 	= forms.ModelChoiceField(queryset = CustomerContact.objects.all(),widget = forms.Select(attrs = {'class':'custom-select'}), empty_label='Select the Client Contact')
	agency_name_ref 	= forms.ModelChoiceField(queryset = AgencyDetail.objects.all(),widget = forms.Select(attrs = {'class':'custom-select'}), empty_label='Select the Agency Name')
	agency_contact_ref 	= forms.ModelChoiceField(queryset = AgencyContact.objects.all(),widget = forms.Select(attrs = {'class':'custom-select'}), empty_label='Select the Agency Contact')
	brand_name_ref		= forms.ModelChoiceField(queryset = CustomerName.objects.all(),widget = forms.Select(attrs = {'class':'custom-select'}), empty_label='Select the Brand')
	
	class Meta:
		model = FinalFctNfctDeal
		fields = '__all__'
		# exclude = ('deal_id',)			

		widgets = {
		'deal_id'	 : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter deal id'}),
		'fct_total'  : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter fct total'}),
		'nfct_total' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter nfct total'}),
		'grandtotal' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter grand total'}),
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['client_contact_ref'].queryset = FinalFctNfctDeal.objects.none()

	