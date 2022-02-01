from django import forms
from .models import base

class base_form(forms.ModelForm):
	class Meta:
		model = base
		fields = '__all__'
		# fields = ['date',]
		# widgets = {
		# 'date' : forms.DateInput(attrs = {'class': 'form-control',})
		# }


