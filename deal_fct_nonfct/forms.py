from django import forms
from .models import *
# from . models import (Base, Channel, Disper, Band, Base_rate_table, Fct_deal)
from .models import Base

class Base_form(forms.ModelForm):
	class Meta:
		model = Base
		fields = '__all__'
		# fields = ['date',]
		# widgets = {
		# 'date' : forms.DateInput(attrs = {'class': 'form-control',})
		# }


class Channel_form(forms.ModelForm):
	"""docstring for Channel"""
	class Meta:
		model = Channel
		fields = '__all__'

		widgets = {
		'c_list' : forms.TextInput(attrs = {'class': 'form-control'})
		}

class Disper_form(forms.ModelForm):

	class Meta:
		model = Disper 
		fields = '__all__'

		widgets = {
		'dis_list' : forms.TextInput(attrs = {'class': 'form-control'})
		}

class Band_form(forms.ModelForm):

	class Meta:
		model = Band 
		fields = '__all__'

		widgets = {
		'b_list' : forms.TextInput(attrs = {'class': 'form-control'})
		}


class Base_rate_table_form(forms.ModelForm):

	class Meta:
		model = Base_rate_table
		fields = '__all__'

		widgets = {
		'br' : forms.TextInput(attrs = {'class': 'form-control'})
		}

class Form_fct_deal(forms.ModelForm):

	class Meta:
		model = Fct_deal
		fields = '__all__'
		# exclude = ('dealid_fct_ref',)

		widgets = {
		'total_rev': forms.TextInput(attrs = {'class': 'form-control','readonly': 'readonly'}),
		
		}

# single Fct_deal
class Form_fctdeal(forms.ModelForm):

	class Meta:
		model = DealFct
		fields = '__all__'
		exclude = ('dealid_fct',)

		widgets = {
		'total_rev': forms.TextInput(attrs = {'class': 'form-control','readonly': 'readonly'}),
		# 'deal_id': forms.TextInput(attrs = {'class': 'form-control','placeholder':'Enter Deal ID here'}),
		}


class FinalFCTForm(forms.ModelForm):
    client_name_ref 	= forms.ModelChoiceField(queryset = CustomerName.objects.all(),widget = forms.Select(attrs = {'class':'form-select'}), empty_label='Select the Client')
    client_contact_ref 	= forms.ModelChoiceField(queryset = CustomerContact.objects.all(),widget = forms.Select(attrs = {'class':'form-select'}), empty_label='Client Contact')
    agency_name_ref 	= forms.ModelChoiceField(queryset = AgencyDetail.objects.all(),widget = forms.Select(attrs = {'class':'form-select'}), empty_label='Select the Agency')
    agency_contact_ref 	= forms.ModelChoiceField(queryset = AgencyContact.objects.all(),widget = forms.Select(attrs = {'class':'form-select'}), empty_label='Agency Contact')
    brand_name_ref		= forms.ModelChoiceField(queryset = CustomerName.objects.all(),widget = forms.Select(attrs = {'class':'form-select'}), empty_label='Select the Brand')
    
    class Meta:
        model = FinalFCT
        fields = '__all__'
        # exclude = ('deal_id',)
        widgets = {
            'deal_id'	 : forms.TextInput(attrs={'class':'form-control','readonly':'readonly','placeholder': 'Enter deal id'}),
            'executive'  : forms.TextInput(attrs={'class':'form-control'}),
            'reporting_manager' : forms.TextInput(attrs={'class':'form-control'}),
            'RO_number' : 	forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter RO Number'}),
            'RO_value'  :	forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter RO Value'}),
            'fct_total_rev'  : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter fct total'}),
            }
   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client_contact_ref'].queryset = FinalNFCT.objects.none()
        self.fields['agency_contact_ref'].queryset = FinalNFCT.objects.none()
        if 'client_name_ref' in self.data:
            print("client name exists/////")
            try:
                client_id = self.data.get('client_name_ref')
                self.fields['client_contact_ref'].queryset = CustomerContact.objects.filter(ref_creg_no=client_id).order_by('pri_fname')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['client_contact_ref'].queryset = self.instance.client.client_set.order_by('pri_fname')
			
        if 'agency_name_ref' in self.data:
            print("agency name exists/////")
            try:
                agency_id = self.data.get('agency_name_ref')
                self.fields['agency_contact_ref'].queryset = AgencyContact.objects.filter(agency_details=agency_id).order_by('pri_firstName')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['agency_contact_ref'].queryset = self.instance.agency.agency_set.order_by('pri_firstName')

