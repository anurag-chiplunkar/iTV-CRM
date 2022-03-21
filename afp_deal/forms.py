from django import forms
from . models import *
from django.forms import (formset_factory, modelformset_factory)

class AFP_Program(forms.ModelForm):
	"""Creating form for Program Names"""
	class Meta:
		model = AFPProgramName
		fields = '__all__'
		
		widgets = {
		'program_name' : forms.TextInput(attrs = {'class': 'form-control'})
		}

class AFP_Channel(forms.ModelForm):
	"""Creating form for Channel Names"""
	class Meta:
		model = AFPChannels
		fields = '__all__'
		
		widgets = {
		'channels' : forms.TextInput(attrs = {'class': 'form-control'})
		}

class AFP_Promo(forms.ModelForm):
	"""Creating form for promos Names"""
	class Meta:
		model = AFPPromos
		fields = '__all__'
		
		widgets = {
		'promos' : forms.TextInput(attrs = {'class': 'form-control'})
		}


class AFP_Slot(forms.ModelForm):
	"""Creating form for slot Names"""
	class Meta:
		model = AFPSlots
		fields = '__all__'
		
		widgets = {
		'slot' : forms.TextInput(attrs = {'class': 'form-control'})
		}

class AFP_Base_Rate_Form(forms.ModelForm):
	"""ModelForm for saving base rates"""
	ref_program_name = forms.ModelChoiceField(queryset= AFPProgramName.objects.all(),widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Program')
	ref_channels = forms.ModelChoiceField(queryset= AFPChannels.objects.all(),widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Channel')
	class Meta:
		model = AFPBaseRate
		fields = '__all__'
		exclude = ('br_unique_key','ref_program_name','ref_channels',)

		widgets = {
		'baserate' : forms.TextInput(attrs = {'class': 'form-control'})
		}

# class AFP_Deal_Form(forms.ModelForm):
# 	ref_program_name = forms.ModelChoiceField(queryset= AFPProgramName.objects.all(),widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Program')
# 	ref_channels = forms.ModelChoiceField(queryset= AFPChannels.objects.all(),widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Channel')
# 	# ref_promos = forms.ModelChoiceField(queryset= AFPPromos.objects.all(),widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Promo')
# 	ref_slot = forms.ModelChoiceField(queryset= AFPSlots.objects.all(),widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Slot')
# 	class Meta:
# 		model = AFPDeal
# 		fields = '__all__'
# 		exclude = ('afp_base_rate',)
# 		widgets = {'afp_eff_rate' :forms.TextInput(attrs = {'class': 'form-control'}),
				
# 				'ref_promos' :forms.TextInput(attrs = {'class': 'form-control'}),
# 		}

# Model Formset for AFP multiple forms (Add new form)
AFPDealModelFormset = modelformset_factory(
	AFPDeal,
	fields = ('ref_program_name','description','ref_channels','ref_promos','ref_slot','afp_eff_rate','afp_base_rate',),
	extra = 1,
	widgets = {
		# 'afp_deal_id': forms.TextInput(attrs={
        #     'class': 'class_afp_deal_id form-control',
        #     'placeholder': 'Deal id'
        #     }
        # ),

		'ref_program_name': forms.Select(attrs={
            'class': 'class_ref_program_name form-select',
            'placeholder': 'Program Name'
            }
        ),

		'description': forms.TextInput(attrs={
            'class': 'class_desc form-control',
            'placeholder': 'Enter Description'
            }
        ),

		'ref_channels': forms.Select(attrs={
            'class': 'class_ref_channels form-select',
            'placeholder': 'Channel'
            }
        ),

		'ref_promos': forms.TextInput(attrs={
            'class': 'class_ref_promos form-control',
            'placeholder': 'Promo'
            }
        ),

		'ref_slot': forms.Select(attrs={
            'class': 'class_ref_slot form-select',
            'placeholder': 'Slot'
            }
        ),

		'afp_eff_rate': forms.NumberInput(attrs={
            'class': 'class_afp_eff_rate form-control',
            'placeholder': 'Enter Effective Rate'
            }
        ),

		'afp_base_rate' : forms.NumberInput(attrs={
            'class' : 'class_afp_base_rate form-control',
            'readonly' : 'readonly',
            'placeholder': 'Base Rate'
        }),

	}
)

class FinalAFPDealDetails(forms.ModelForm):
	"""ModelForm for AFP common form"""
	afp_client_name_ref 	= forms.ModelChoiceField(queryset = CustomerName.objects.all(),widget = forms.Select(attrs = {'class':'form-control'}), empty_label='Select the Client Name')
	afp_client_contact_ref 	= forms.ModelChoiceField(queryset = CustomerContact.objects.all(),widget = forms.Select(attrs = {'class':'form-control'}), empty_label='Client Contact')
	afp_agency_name_ref 	= forms.ModelChoiceField(queryset = AgencyDetail.objects.all(),widget = forms.Select(attrs = {'class':'form-control'}), empty_label='Select the Agency Name')
	afp_agency_contact_ref 	= forms.ModelChoiceField(queryset = AgencyContact.objects.all(),widget = forms.Select(attrs = {'class':'form-control'}), empty_label='Agency Contact')
	afp_brand_name_ref		= forms.ModelChoiceField(queryset = CustomerName.objects.all(),widget = forms.Select(attrs = {'class':'form-control'}), empty_label='Select the Brand')
	
	class Meta:
		model = FinalAFPDeal
		fields = '__all__'

		widgets = {
		'afpdeal_id'	 : forms.TextInput(attrs={'class':'form-control','readonly':'readonly','placeholder': 'Enter deal id'}),
		'afp_ro_number'	 : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter RO Number'}),
		'afp_ro_value'	 : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter RO Value'}),
		}

	def __init__(self, *args, **kwargs):
			"""Function for dependent dropdown for client name, agency name, client contact and agency contact
			
			:afp_client_name: afp_agency_name and afp_client_contact changes according to the afp_client_name selection
			:afp_agency_name: afp_agency_contact changes according to afp_agency_name selection"""
			
			super().__init__(*args, **kwargs)
			self.fields['afp_client_contact_ref'].queryset = FinalAFPDeal.objects.none()
			self.fields['afp_agency_contact_ref'].queryset = FinalAFPDeal.objects.none()
			self.fields['afp_agency_name_ref'].queryset = FinalAFPDeal.objects.none()

			# print("self.data",self.data,"------------------")
			
			if 'afp_client_name_ref' in self.data:
				print("client name exists/////")
				try:
					client_id = self.data.get('afp_client_name_ref')
					self.fields['afp_client_contact_ref'].queryset = CustomerContact.objects.filter(ref_creg_no=client_id).order_by('pri_fname')
				except (ValueError, TypeError):
					pass  
			elif self.instance.pk:
				self.fields['afp_client_contact_ref'].queryset = self.instance.client.client_set.order_by('pri_fname')
			
			if 'afp_agency_name_ref' in self.data:
				print("agency name exists/////")
				try:
					agency_id = self.data.get('afp_agency_name_ref')
					self.fields['afp_agency_contact_ref'].queryset = AgencyContact.objects.filter(agency_details=agency_id).order_by('pri_firstName')
				except (ValueError, TypeError):
					pass  
			elif self.instance.pk:
				self.fields['afp_agency_contact_ref'].queryset = self.instance.agency.agency_set.order_by('pri_firstName')

			if 'afp_client_name_ref' in self.data:
				print("Client name exists/////")
				try:
					agency = self.data.get('afp_client_name_ref')
					self.fields['afp_agency_name_ref'].queryset = AgencyDetail.objects.filter(ccreg_no=agency).order_by('agency_name')
				except (ValueError, TypeError):
					pass
			elif self.instance.pk:
				self.fields['afp_agency_name_ref'].queryset = self.instance.agency.agency_set.order_by('agency_name')
