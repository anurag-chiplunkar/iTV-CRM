from django import forms
from . models import *

class AFP_Progname(forms.ModelForm):
	"""docstring for AFP_Progname
	Creating form for Program Names"""
	class Meta:
		model = AFP_ProgramName
		fields = '__all__'


class AFP_Chann(forms.ModelForm):
	"""docstring for AFP_Progname
	Creating form for Channel Names"""
	class Meta:
		model = AFP_Channels
		fields = '__all__'
		


class AFP_dealform(forms.ModelForm):
	"""docstring for AFP_dealform
	Creating form for AFP Deal Detail"""
	# promos = forms.ChoiceField(queryset= AFP_Deal.objects.all(), widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Program Name')
	# slot = forms.ModelChoiceField(queryset= AFP_Deal.objects.all(), widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Slot Name')
	ref_program_name = forms.ModelChoiceField(queryset= AFP_ProgramName.objects.all(),widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Program')
	ref_channels = forms.ModelChoiceField(queryset= AFP_Channels.objects.all(),widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Channel')
	class Meta:
		model = AFP_Deal
		fields = '__all__'

		widgets = {
			# 'promos' : forms.Select(attrs = {'class' : 'form-select', 'placeholder' : 'Select Promos'}),
			# 'slot' : forms.Select(attrs = {'class' : 'form-select', 'placeholder' : 'Select Slots'}),
			'eff_rate' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Effective Rate'}),
			# 'total' : forms.TextInput(attrs = {'class' : 'form-select', 'placeholder' : 'Total'})
		}

		
class Events_catname(forms.ModelForm):
	"""docstring for Events_catname
	Creating form for Category Names"""
	class Meta:
		model = Events_Category
		fields = '__all__'


class Events_dealform(forms.ModelForm):
	"""docstring for Events_dealform
	Creating form for Events Deal Detail"""
	ref_category_name = forms.ModelChoiceField(queryset = Events_Category.objects.all(), widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Category')
	ref_channels = forms.ModelChoiceField(queryset= AFP_Channels.objects.all(),widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Channel Name')

	class Meta:
		model = Events_Deal
		fields = ['description', 'amount', 'merit_money',]


	widgets = {
		'description' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter Description'}),
		'amount' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter Amount'}),
		'merit_money' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter Merit Money'}),
			}
