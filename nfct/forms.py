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