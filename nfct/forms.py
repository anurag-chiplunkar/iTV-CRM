from django import forms
from . models import *
from django.forms import ModelForm
from django.forms import modelformset_factory

from django import forms

from django.forms import (formset_factory, modelformset_factory)


class NFCT_Base_Rate_Form(forms.ModelForm):
    CHANNEL_CHOICE = [
        ('INN','INN'),
        ('NX','NX'),
        ('GUJ','GUJ'),
        ('PUN','PUN'),
    ]

    ELEMENT_CHOICE = [
        ('Aston','Aston'),
        ('L Band','L Band'),
    ]
    channel = forms.Select(choices = CHANNEL_CHOICE, attrs = {'class':'form-select class_channel', 'placeholder' : 'Select Channel'})
    element = forms.Select(choices = ELEMENT_CHOICE, attrs = {'class':'form-select class_element', 'placeholder' : 'Select Element'})
    
    class Meta:
        model = NFCT_Base_Rate
        fields = '__all__'
        
        widgets = {
		'nfct_baserate' : forms.NumberInput(attrs = {'class': 'form-control'})
		}

DealModelFormset = modelformset_factory( 
    Deal_nfct,          
    # 'deal_id' we removed this from fields
    fields=('main_dealid_nfct_ref','channel', 'element','durations','duration_in', 'er', 'freq','total_seconds','base_rate','total'),
    extra=1,
    widgets={
        'main_dealid_nfct_ref': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Deal ID here'
        }),
        'channel': forms.Select(attrs={
            'class': 'class_channel form-select',
            'placeholder': 'Channel'
            }
        ),
        'element': forms.Select(attrs={
            'class': 'class_element form-select',
            'placeholder': 'Element'
            }
        ),
        'durations': forms.Select(attrs={
            'class': 'class_durations form-select',
            'placeholder': 'Duration'
            }
        ),
        'duration_in': forms.TextInput(attrs={
            'class': 'class_duration_in form-control',
            'placeholder': 'Duration In'
            }
        ),
        'er': forms.NumberInput(attrs={
            'class': 'class_er form-control',
            'placeholder': 'Enter Effective Rate here'
            }
        ),
        'freq' : forms.NumberInput(attrs={
            'class' : 'class_freq form-control',
            'placeholder': 'Enter Frequency here'
        }),
        'total_seconds' : forms.NumberInput(attrs={
            'class' : 'class_total_seconds form-control',
            'readonly' : 'readonly',
            'placeholder': 'Total Seconds'
        }),
        'base_rate' : forms.NumberInput(attrs={
            'class' : 'class_base_rate form-control',
            'readonly' : 'readonly',
            'placeholder': 'Base Rate'
        }),
        'total' : forms.NumberInput(attrs={
            'class' : 'class_total form-control',
            'readonly' : 'readonly',
            'placeholder': 'Total'
        }),
    }
)


NFCTDealModelFormset = modelformset_factory( 
    NFCTDeal,          
    # 'deal_id' we removed this from fields
    fields=('dealid_nfct','channel', 'element','durations','duration_in', 'er', 'freq','total_seconds','base_rate','nfct_total'),
    extra=1,
    widgets={
        'dealid_nfct': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Deal ID here'
        }),
        'channel': forms.Select(attrs={
            'class': 'class_channel form-select',
            'placeholder': 'Channel'
            }
        ),
        'element': forms.Select(attrs={
            'class': 'class_element form-select',
            'placeholder': 'Element'
            }
        ),
        'durations': forms.Select(attrs={
            'class': 'class_durations form-select',
            'placeholder': 'Duration'
            }
        ),
        'duration_in': forms.TextInput(attrs={
            'class': 'class_duration_in form-control',
            'placeholder': 'Duration In'
            }
        ),
        'er': forms.NumberInput(attrs={
            'class': 'class_er form-control',
            'placeholder': 'Enter Effective Rate here'
            }
        ),
        'freq' : forms.NumberInput(attrs={
            'class' : 'class_freq form-control',
            'placeholder': 'Enter Frequency here'
        }),
        'total_seconds' : forms.NumberInput(attrs={
            'class' : 'class_total_seconds form-control',
            'readonly' : 'readonly',
            'placeholder': 'Total Seconds'
        }),
        'base_rate' : forms.NumberInput(attrs={
            'class' : 'class_base_rate form-control',
            'readonly' : 'readonly',
            'placeholder': 'Base Rate'
        }),
        'nfct_total' : forms.NumberInput(attrs={
            'class' : 'class_total form-control',
            'readonly' : 'readonly',
            'placeholder': 'Total'
        }),
    }
)



class FinalNFCTForm(forms.ModelForm):
    client_name_ref 	= forms.ModelChoiceField(queryset = CustomerName.objects.all(),widget = forms.Select(attrs = {'class':'form-select'}), empty_label='Select the Client Name')
    client_contact_ref 	= forms.ModelChoiceField(queryset = CustomerContact.objects.all(),widget = forms.Select(attrs = {'class':'form-select'}), empty_label='Client Contact')
    agency_name_ref 	= forms.ModelChoiceField(queryset = AgencyDetail.objects.all(),widget = forms.Select(attrs = {'class':'form-select'}), empty_label='Select the Agency Name')
    agency_contact_ref 	= forms.ModelChoiceField(queryset = AgencyContact.objects.all(),widget = forms.Select(attrs = {'class':'form-select'}), empty_label='Agency Contact')
    brand_name_ref		= forms.ModelChoiceField(queryset = CustomerName.objects.all(),widget = forms.Select(attrs = {'class':'form-select'}), empty_label='Select the Brand')
    
    class Meta:
        model = FinalNFCT
        fields = '__all__'
        # exclude = ('deal_id',)
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



# class NFCT_Chann(forms.ModelForm):
# 	"""docstring for NFCT_Channels
# 	Creating form for Channel Names"""
# 	class Meta:
# 		model = NFCT_Channels
# 		fields = '__all__'

# class NFCT_Elem(forms.ModelForm):
# 	"""docstring for NFCT_Elements
# 	Creating form for Element Names"""
# 	class Meta:
# 		model = NFCT_Elements
# 		fields = '__all__'

# class NFCT_Base_Rate_Form(forms.ModelForm):
#     nfct_channels = forms.ModelChoiceField(queryset = NFCT_Channels.objects.all(), widget = forms.Select(attrs = {'class':'form-select'}), empty_label = 'Select Channel')
#     nfct_elements = forms.ModelChoiceField(queryset = NFCT_Elements.objects.all(), widget = forms.Select(attrs = {'class':'form-select'}), empty_label = 'Select Element')
    
#     class Meta:
#         model = NFCT_Base_Rate
#         fields = '__all__'
        
#         widgets = {
# 		'nfct_baserate' : forms.NumberInput(attrs = {'class': 'form-control'})
# 		}


# durations_choices = (
#     ('days', 'Days'),
#     ('months', 'Months')

# )

# class NFCT_deal(forms.ModelForm):
#     """docstring for NFCT Deal form
#     forms for NFCT Deal"""

  
#     ref_nfct_channels_id = forms.ModelChoiceField(queryset = NFCT_Channels.objects.all(), widget = forms.Select(attrs = {'class':'form-select'}), empty_label = 'Select Channel')
#     ref_nfct_elements_id = forms.ModelChoiceField(queryset = NFCT_Elements.objects.all(), widget = forms.Select(attrs = {'class':'form-select'}), empty_label = 'Select Element')

#     class Meta:
#         model = NFCTDeal
#         fields = '__all__'
#         exclude = ('ref_nfct_channels_id', 'ref_nfct_elements_id',)
#         # 'nfct_refrenece_no',

#         widgets = {
#             'durations' : forms.Select(attrs = {'class' : 'form-select'}, choices = durations_choices),
#             'duration_in' : forms.NumberInput(attrs = {'class' : 'form-control'}),
#             'effective_rate' : forms.NumberInput(attrs = {'class' : 'form-control'}),
#             'frequency' : forms.NumberInput(attrs = {'class' : 'form-control'}),
#             'total_seconds' : forms.NumberInput(attrs = {'class' : 'form-control'}),
#             'base_rate' : forms.NumberInput(attrs = {'class' : 'form-control'}),
#             'nfct_total' : forms.NumberInput(attrs = {'class' : 'form-control'}),
#         }

# NFCTDealFormSet = modelformset_factory(NFCTDeal, fields = '__all__', extra = 1,  widgets={
#     'ref_nfct_channels_id' : forms.Select(attrs = {'class':'form-select'}),
#     'ref_nfct_elements_id' : forms.Select(attrs = {'class':'form-select'}),
#     'durations' : forms.Select(attrs = {'class' : 'form-select'}, choices = durations_choices),
#     'duration_in' : forms.NumberInput(attrs = {'class' : 'form-control'}),
#     'effective_rate' : forms.NumberInput(attrs = {'class' : 'form-control'}),
#     'frequency' : forms.NumberInput(attrs = {'class' : 'form-control'}),
#     'total_seconds' : forms.NumberInput(attrs = {'class' : 'form-control'}),
#     'base_rate' : forms.NumberInput(attrs = {'class' : 'form-control'}),
#     'nfct_total' : forms.NumberInput(attrs = {'class' : 'form-control'}),
# })
