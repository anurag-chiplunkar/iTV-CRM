from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.forms import (formset_factory, modelformset_factory)
from . models import *
from nfct.forms import *
from nfct.models import *
from deal_fct_nonfct.forms import *
from deal_fct_nonfct.models import *

class FinalFctNfctDealDetails(forms.ModelForm):
	client_name_ref 	= forms.ModelChoiceField(queryset = CustomerName.objects.all(),widget = forms.Select(attrs = {'class':'form-select'}), empty_label='Select the Client Name')
	client_contact_ref 	= forms.ModelChoiceField(queryset = CustomerContact.objects.all(),widget = forms.Select(attrs = {'class':'form-select'}), empty_label='Client Contact')
	agency_name_ref 	= forms.ModelChoiceField(queryset = AgencyDetail.objects.all(),widget = forms.Select(attrs = {'class':'form-select'}), empty_label='Select the Agency Name')
	agency_contact_ref 	= forms.ModelChoiceField(queryset = AgencyContact.objects.all(),widget = forms.Select(attrs = {'class':'form-select'}), empty_label='Agency Contact')
	brand_name_ref		= forms.ModelChoiceField(queryset = CustomerName.objects.all(),widget = forms.Select(attrs = {'class':'form-select'}), empty_label='Select the Brand')
	
	class Meta:
		model = FinalFctNfctDeal
		fields = '__all__'
		# exclude = ('fct_total','nfct_total','grandtotal')			

		widgets = {
		'deal_id'	 : forms.TextInput(attrs={'class':'form-control','readonly':'readonly','placeholder': 'Enter deal id'}),
		'executive'  : forms.TextInput(attrs={'class':'form-control'}),
		'reporting_manager' : forms.TextInput(attrs={'class':'form-control'}),
		'RO_number' : 	forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter RO Number'}),
		'RO_value'  :	forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter RO Value'}),
		'fct_total'  : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter fct total'}),
		'nfct_total' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter nfct total'}),
		'grandtotal' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter grand total'}),
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['client_contact_ref'].queryset = FinalFctNfctDeal.objects.none()
		# print("self.data",self.data,"------------------")
		
		if 'client_name_ref' in self.data:
			print("client name exists/////")
			try:
				client_id = self.data.get('client_name_ref')
				self.fields['client_contact_ref'].queryset = CustomerContact.objects.filter(ref_creg_no=client_id).order_by('pri_fname')
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty City queryset
		elif self.instance.pk:
			self.fields['client_contact_ref'].queryset = self.instance.client.client_set.order_by('pri_fname')
			
class form_fct_deal(forms.ModelForm):

	class Meta:
		model = Fct_deal
		fields = '__all__'
		exclude = ('dealid_fct_ref',)

		widgets = {
		'total_rev': forms.TextInput(attrs = {'class': 'form-control','readonly': 'readonly'}),
		# 'deal_id': forms.TextInput(attrs = {'class': 'form-control','placeholder':'Enter Deal ID here'}),
		}

	