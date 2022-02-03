from django import forms
from .models import base, Channel, Disper, Band, base_rate_table

class base_form(forms.ModelForm):
	class Meta:
		model = base
		fields = '__all__'
		# fields = ['date',]
		# widgets = {
		# 'date' : forms.DateInput(attrs = {'class': 'form-control',})
		# }


class channel_form(forms.ModelForm):
	"""docstring for """
	class Meta:
		model = Channel
		fields = '__all__'

		widgets = {
		'c_list' : forms.TextInput(attrs = {'class': 'form-control'})
		}

class disper_form(forms.ModelForm):

	class Meta:
		model = Disper 
		fields = '__all__'

		widgets = {
		'dis_list' : forms.TextInput(attrs = {'class': 'form-control'})
		}

class band_form(forms.ModelForm):

	class Meta:
		model = Band 
		fields = '__all__'

		widgets = {
		'b_list' : forms.TextInput(attrs = {'class': 'form-control'})
		}


class base_rate_table_form(forms.ModelForm):

	class Meta:
		model = base_rate_table
		fields = '__all__'

		widgets = {
		'br' : forms.TextInput(attrs = {'class': 'form-control'})
		}


