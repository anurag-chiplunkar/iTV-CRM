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

		widgets = {
		'total_rev': forms.TextInput(attrs = {'class': 'form-control','readonly': 'readonly'}),
		
		}

