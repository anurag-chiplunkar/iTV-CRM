from django import forms
from . models import *
# from django.forms import ModelForm
# from django.forms import modelformset_factory
# from .models import Book


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
		
# AFPModelFormSet = modelformset_factory(
# 	AFP_Deal, fields = '__all__', extra = 2)
# formset = AFPModelFormSet()
# print(formset)

class Events_catname(forms.ModelForm):
	"""docstring for Events_catname
	Creating form for Category Names"""
	class Meta:
		model = Events_Category
		fields = '__all__'

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

class AFP_Base_Rate_Form(forms.ModelForm):

	class Meta:
		model = AFP_Base_Rate
		fields = '__all__'

		widgets = {
		'baserate' : forms.TextInput(attrs = {'class': 'form-control'})
		}


# class ElementForm(forms.ModelForm):
# 	class Meta:
# 		model = ElementNFCT
# 		fields = '__all__'

# 		widgets = {
# 		'element' : forms.TextInput(attrs={'class': 'form-control'}),
# 		}

class AFP_dealform(forms.ModelForm):
	"""docstring for AFP_dealform
	Creating form for AFP Deal Detail"""
	promos_choices = (
    ("10", "10"),
    ("20", "20"),
    ("30", "30"),
	)

	slot_choices = (
		("10", "10"),
	    ("22", "22"),
	)
	ref_program_name = forms.ModelChoiceField(queryset= AFP_ProgramName.objects.all(),widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Program')
	ref_channels = forms.ModelChoiceField(queryset= AFP_Channels.objects.all(),widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Channel')
	
	class Meta:
		model = AFP_Deal
		fields = '__all__'

		widgets = {
			'promos' : forms.Select(attrs = {'class' : 'form-select', 'placeholder':'Select Promo'}, choices = promos_choices),
			'slot' : forms.Select(attrs = {'class' : 'form-select'}, choices = slot_choices),
			'eff_rate' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Effective Rate'}),
			# 'total' : forms.TextInput(attrs = {'class' : 'form-select', 'placeholder' : 'Total'})
		}

class Events_dealform(forms.ModelForm):
	"""docstring for Events_dealform
	Creating form for Events Deal Detail"""
	ref_category_name = forms.ModelChoiceField(queryset = Events_Category.objects.all(), widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Category')
	ref_channels = forms.ModelChoiceField(queryset= AFP_Channels.objects.all(),widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Channel')

	class Meta:
		model = Events_Deal
		fields = ['description', 'merit_money',]


		widgets = {
			'description' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter Description'}),
			'merit_money' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter Merit Money'}),
				}
				
class form_fct_deal(forms.ModelForm):

	class Meta:
		model = fct_deal
		fields = '__all__'

		widgets = {
		'total_rev': forms.TextInput(attrs = {'class': 'form-control'})
		}

# class NonFCTDealForm(forms.ModelForm):
# 	channel_choice = forms.ModelChoiceField(queryset = ChannelNFCT.objects.all(),widget = forms.Select(attrs = {'class':'custom-select'}), empty_label='Select Channel')
# 	element_choice = forms.ModelChoiceField(queryset = ElementNFCT.objects.all(),widget = forms.Select(attrs = {'class':'custom-select'}), empty_label='Select Element')

# 	class Meta:
# 		model = DealNFCT
# 		fields = '__all__'
# 		exclude = ('channel_nfct','element_nfct','baserate_nfct')

# 		widgets = {
# 		'eff_rate' : forms.NumberInput(attrs={'class': 'form-control'}),
# 		'frequency' : forms.NumberInput(attrs={'class': 'form-control'}),
# 		# 'total_sec' : forms.NumberInput(attrs={'class': 'form-control'}),
# 		'total_cost' : forms.NumberInput(attrs={'class': 'form-control'}),
# 		}

# class Final_Deal(forms.ModelForm):
# 	class Meta:
# 		model = FinalDeal
# 		fields = '__all__'



# final deal form
# class Final_Deal(forms.ModelForm):
# 	promos_choices = (
# 	    ("10", "10"),
# 	    ("20", "20"),
# 	    ("30", "30"),
# 	)

# 	slot_choices = (
# 		("10", "10"),
# 	    ("22", "22"),
# 	)
# 	# event deal form
# 	ref_category_name = forms.ModelChoiceField(queryset = Events_Category.objects.all(), widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Category')
# 	ref_channels = forms.ModelChoiceField(queryset= AFP_Channels.objects.all(),widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Channel')
# 	ref_program_name = forms.ModelChoiceField(queryset= AFP_ProgramName.objects.all(),widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Program')
# 	channel_choice = forms.ModelChoiceField(queryset = AFP_Channels.objects.all(),widget = forms.Select(attrs = {'class':'custom-select'}), empty_label='Select Channel')
# 	element_choice = forms.ModelChoiceField(queryset = ElementNFCT.objects.all(),widget = forms.Select(attrs = {'class':'custom-select'}), empty_label='Select Element')

# 	class Meta:
# 		model = FinalDeal
# 		fields = '__all__'
# 		exclude = ('ref_category_name', 'ref_channels','channel_nfct','element_nfct','baserate_nfct',)


# 		widgets = {
# 			'description' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter Description'}),
# 			'merit_money' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter Merit Money'}),
# 			'promos' : forms.Select(attrs = {'class' : 'form-select', 'placeholder':'Select Promo'}, choices = promos_choices),
# 			'slot' : forms.Select(attrs = {'class' : 'form-select'}, choices = slot_choices),
# 			'eff_rate' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Effective Rate'}),
# 			'eff_rate' : forms.NumberInput(attrs={'class': 'form-control'}),
# 			'frequency' : forms.NumberInput(attrs={'class': 'form-control'}),
# 			# 'total_sec' : forms.NumberInput(attrs={'class': 'form-control'}),
# 			'total_cost' : forms.NumberInput(attrs={'class': 'form-control'}),
# 				}


# fct



# class form_fct_deal(forms.ModelForm):

# 	class Meta:
# 		model = fct_deal
# 		fields = '__all__'

# 		# widgets = {
# 		# 'total_rev': forms.TextInput(attrs = {'class': 'form-control'})
# 		# }


# AFP


# class BaseRateForm(forms.ModelForm):
# 	channel_choice = forms.ModelChoiceField(queryset = AFP_Channels.objects.all(),widget = forms.Select(attrs = {'class':'custom-select'}), empty_label='Select Channel')
# 	element_choice = forms.ModelChoiceField(queryset = ElementNFCT.objects.all(),widget = forms.Select(attrs = {'class':'custom-select'}), empty_label='Select Element')
# 	class Meta:
# 		model = BaseRateNFCT
# 		fields = '__all__'
# 		exclude = ('channel_nfct','element_nfct','unique_key')

# 		widgets = {
# 		'base_rate' : forms.TextInput(attrs={'class': 'form-control'}),
# 		}
