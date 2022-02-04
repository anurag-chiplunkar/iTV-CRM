from django import forms
from . models import *

class ChannelForm(forms.ModelForm):
	class Meta:
		model = ChannelNFCT
		fields = '__all__'

		widgets = {
		'channel' : forms.TextInput(attrs={'class': 'form-control'}),
		}

class ElementForm(forms.ModelForm):
	class Meta:
		model = ElementNFCT
		fields = '__all__'

		widgets = {
		'element' : forms.TextInput(attrs={'class': 'form-control'}),
		}


class DealForm(forms.ModelForm):
	channel_choice = forms.ModelChoiceField(queryset = ChannelNFCT.objects.all(),widget = forms.Select(attrs = {'class':'custom-select'}), empty_label='Select Channel')
	element_choice = forms.ModelChoiceField(queryset = ElementNFCT.objects.all(),widget = forms.Select(attrs = {'class':'custom-select'}), empty_label='Select Channel')

	class Meta:
		model = DealNFCT
		fields = '__all__'
		exclude = ('channel_nfct','element_nfct','baserate_nfct')

		widgets = {
		'eff_rate' : forms.NumberInput(attrs={'class': 'form-control'}),
		'frequency' : forms.NumberInput(attrs={'class': 'form-control'}),
		'total_sec' : forms.NumberInput(attrs={'class': 'form-control'}),
		'total_cost' : forms.NumberInput(attrs={'class': 'form-control'}),		
		}
