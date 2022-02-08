from django import forms
from . models import *

class NFCT_Chann(forms.ModelForm):
	"""docstring for AFP_Progname
	Creating form for Channel Names"""
	class Meta:
		model = NFCT_Channels
		fields = '__all__'