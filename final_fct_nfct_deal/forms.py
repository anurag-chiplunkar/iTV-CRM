from django import forms
from django.contrib.auth import get_user_model
from . models import *


class FinalFctNfctDealDetails(forms.ModelForm):
    client_name_ref = forms.ModelChoiceField(queryset = CustomerName.objects.all(),widget = forms.Select(attrs = {'class':'custom-select'}), empty_label='Select the Client')
    client_contact_ref = forms.ModelChoiceField(queryset = CustomerName.objects.all(),widget = forms.Select(attrs = {'class':'custom-select'}), empty_label='Select the Client')
    agency_name_ref = forms.ModelChoiceField(queryset = CustomerName.objects.all(),widget = forms.Select(attrs = {'class':'custom-select'}), empty_label='Select the Client')
    agency_contact_ref = forms.ModelChoiceField(queryset = CustomerName.objects.all(),widget = forms.Select(attrs = {'class':'custom-select'}), empty_label='Select the Client')

	class Meta:
		model = FinalFctNfctDeal
		fields = '__all__'
		exclude = ('deal_id',)			

		widgets = {
		'fct_total' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter fct total'}),
		'nfct_total' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter nfct total'}),
		'grandtotal' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter grand total'}),
		}

	