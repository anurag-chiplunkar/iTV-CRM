from django import forms
from . models import *

class NFCT_Chann(forms.ModelForm):
	"""docstring for NFCT_Channels
	Creating form for Channel Names"""
	class Meta:
		model = NFCT_Channels
		fields = '__all__'

class NFCT_Elem(forms.ModelForm):
	"""docstring for NFCT_Elements
	Creating form for Element Names"""
	class Meta:
		model = NFCT_Elements
		fields = '__all__'

class NFCT_Base_Rate_Form(forms.ModelForm):
    nfct_channels = forms.ModelChoiceField(queryset = NFCT_Channels.objects.all(), widget = forms.Select(attrs = {'class':'form-select'}), empty_label = 'Select Channel')
    nfct_elements = forms.ModelChoiceField(queryset = NFCT_Elements.objects.all(), widget = forms.Select(attrs = {'class':'form-select'}), empty_label = 'Select Element')
    
    class Meta:
        model = NFCT_Base_Rate
        fields = '__all__'
        
        widgets = {
		'nfct_baserate' : forms.NumberInput(attrs = {'class': 'form-control'})
		}


durations_choices = (
    ('days', 'Days'),
    ('months', 'Months')

)

class NFCT_deal(forms.ModelForm):
    """docstring for NFCT Deal form
    forms for NFCT Deal"""

  
    ref_nfct_channels_id = forms.ModelChoiceField(queryset = NFCT_Channels.objects.all(), widget = forms.Select(attrs = {'class':'form-select'}), empty_label = 'Select Channel')
    ref_nfct_elements_id = forms.ModelChoiceField(queryset = NFCT_Elements.objects.all(), widget = forms.Select(attrs = {'class':'form-select'}), empty_label = 'Select Element')

    class Meta:
        model = NFCTDeal
        fields = '__all__'
        exclude = ('ref_nfct_channels', 'ref_nfct_elements',)
        # 'nfct_refrenece_no',

        widgets = {
            'durations' : forms.Select(attrs = {'class' : 'form-select'}, choices = durations_choices),
            'duration_in' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'effective_rate' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'frequency' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'total_seconds' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'base_rate' : forms.NumberInput(attrs = {'class' : 'form-control'}),
            'nfct_total' : forms.NumberInput(attrs = {'class' : 'form-control'}),
        }