from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.forms import (formset_factory, modelformset_factory)
from . models import *
# from nfct.forms import *
# from nfct.models import *
from deal_fct_nonfct.forms import *
from deal_fct_nonfct.models import *

CATEGORY_CHOICES = (
    ("","--------"),
    ("Conclave","Conclave"),
    ("Cookery","Cookery"),
    ("Entertainment","Entertainment"),
    ("Fashion","Fashion"),
    ("Health /Life Style","Health /Life Style"),
    ("Infotainment","Infotainment"),
    ("Manch","Manch"),
    ("Politics","Politics"),
    ("Spirituality","Spirituality"),
    ("Sports","Sports"),
    ("Technology","Technology"),
    ("Tourism","Tourism")
)

CHANNEL_CHOICE = (
    ("INN","INN"),
    ("NX","NX"),
    ("IN UP","IN UP"),
    ("MP","MP"),
    ("RAJ","RAJ"),
    ("PUN","PUN"),
    ("HAR","HAR"),
    ("GUJ","GUJ"),
    ("NE NEWS","NE NEWS")
)
class FinalEventsForm(forms.ModelForm):
    event_client_name_ref 	= forms.ModelChoiceField(queryset = CustomerName.objects.all(),widget = forms.Select(attrs = {'class':'form-select'}), empty_label='Select the Client Name')
    event_client_contact_ref = forms.ModelChoiceField(queryset = CustomerContact.objects.all(),widget = forms.Select(attrs = {'class':'form-select'}), empty_label='Client Contact')
    event_agency_name_ref = forms.ModelChoiceField(queryset = AgencyDetail.objects.all(),widget = forms.Select(attrs = {'class':'form-select'}), empty_label='Select the Agency Name')
    event_agency_contact_ref = forms.ModelChoiceField(queryset = AgencyContact.objects.all(),widget = forms.Select(attrs = {'class':'form-select'}), empty_label='Agency Contact')
    event_brand_name_ref = forms.ModelChoiceField(queryset = CustomerName.objects.all(),widget = forms.Select(attrs = {'class':'form-select'}), empty_label='Select the Brand')
    category= forms.CharField(widget= forms.Select(choices=CATEGORY_CHOICES,attrs = {'class':'form-select col-auto',}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Description'}))

    class Meta:
        model = Eventmodel
        fields = '__all__'
		# exclude = ('deal_id',)			
        widgets = {
		'deal_id'	 : forms.TextInput(attrs={'class':'form-control dealclass','readonly':'readonly'}),
		'fct_total'  : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter fct total'}),
		'nfct_total' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter nfct total'}),
		'grandtotal' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter grand total'}),
        'channel'    : forms.Select(choices=CHANNEL_CHOICE,attrs = {'class':'form-select','placeholder': 'Select Channel'}),
        
		}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['event_client_contact_ref'].queryset = Eventmodel.objects.none()
        self.fields['event_agency_contact_ref'].queryset = Eventmodel.objects.none()
        self.fields['event_agency_name_ref'].queryset = Eventmodel.objects.none()


		# print("self.data",self.data,"------------------")
        if 'event_client_name_ref' in self.data:
            print("client name exists/////")
            try:
                client_id = self.data.get('event_client_name_ref')
                self.fields['event_client_contact_ref'].queryset = CustomerContact.objects.filter(ref_creg_no=client_id).order_by('pri_fname')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['event_client_contact_ref'].queryset = self.instance.client.client_set.order_by('pri_fname')

        if 'event_agency_name_ref' in self.data:
            print("agency name exists/////")
            try:
                client_id = self.data.get('event_agency_name_ref')
                self.fields['event_agency_contact_ref'].queryset = AgencyContact.objects.filter(agency_details=client_id).order_by('pri_firstName')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['event_client_contact_ref'].queryset = self.instance.client.client_set.order_by('pri_firstName')   

        if 'event_client_name_ref' in self.data:
            print("Client name exists/////")
            try:
                agency = self.data.get('event_client_name_ref')
                self.fields['event_agency_name_ref'].queryset = AgencyDetail.objects.filter(ccreg_no=agency).order_by('agency_name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['event_agency_name_ref'].queryset = self.instance.agency.agency_set.order_by('agency_name')


        

class Form_FCT_Deal(forms.ModelForm):
    
    class Meta:
        model = EventFCTModel
        fields = '__all__'
        widgets = {
		'total_rev': forms.NumberInput(attrs = {'class': 'form-control','readonly': 'readonly'}),
		'deal_id_fct': forms.TextInput(attrs = {'class': 'form-control','readonly': 'readonly'}),
		}

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
        model = Event_NFCT_Base_Rate
        fields = '__all__'
        
        widgets = {
		'nfct_baserate' : forms.NumberInput(attrs = {'class': 'form-control'})
		}


DealModelFormset = modelformset_factory( 
    Event_Deal_Nfct,          
    # 'deal_id' we removed this from fields
    fields=('deal_id_nfct','channel', 'element','durations','duration_in', 'er', 'freq','total_seconds','base_rate','total'),
    extra=1,
    widgets={
        'deal_id_nfct': forms.TextInput(attrs={
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
        })
    }
)
