from django import forms
from django.contrib.auth import get_user_model
from . models import AgencyDetail,AgencyContact


class Agency_details(forms.ModelForm):
	class Meta:
		model = AgencyDetail
		fields = '__all__'
		exclude = ('a_id',)			##exclude this because this is automatically generated in views.py

		widgets = {
		'agency_name' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Agency Name'}),
		'agency_state' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Agency State'})
		}

class Agency_contacts(forms.ModelForm):
	##empty_label is for giving a placeholder to the dropdown
	agency = forms.ModelChoiceField(queryset = AgencyDetail.objects.all(),widget = forms.Select(attrs = {'class':'custom-select'}), empty_label='Select the Agency')
	class Meta:
		model = AgencyContact
		fields = '__all__'
		exclude = ('agency_details',)

		widgets = {
		'pri_firstName' : forms.TextInput(attrs={'class': 'form-control'}),
		'pri_lastName' :  forms.TextInput(attrs={'class': 'form-control'}),
		'pri_designation' : forms.TextInput(attrs={'class': 'form-control'}),
		'pri_email' : forms.EmailInput(attrs={'class': 'form-control'}),
		'pri_phone' : forms.TextInput(attrs={'class': 'form-control'}),
		'pri_landline': forms.TextInput(attrs={'class': 'form-control'}),
		'pri_flatno': forms.TextInput(attrs={'class': 'form-control'}),
		'pri_street': forms.TextInput(attrs={'class': 'form-control'}),
		'pri_landmark': forms.TextInput(attrs={'class': 'form-control'}),
		'pri_city': forms.TextInput(attrs={'class': 'form-control'}),
		'pri_pin': forms.TextInput(attrs={'class': 'form-control'}),

		'sec_firstName' : forms.TextInput(attrs={'class': 'form-control'}),
		'sec_lastName' :  forms.TextInput(attrs={'class': 'form-control'}),
		'sec_designation' : forms.TextInput(attrs={'class': 'form-control'}),
		'sec_email' : forms.EmailInput(attrs={'class': 'form-control'}),
		'sec_phone' : forms.TextInput(attrs={'class': 'form-control'}),
		'sec_landline': forms.TextInput(attrs={'class': 'form-control'}),
		'sec_flatno': forms.TextInput(attrs={'class': 'form-control'}),
		'sec_street': forms.TextInput(attrs={'class': 'form-control'}),
		'sec_landmark': forms.TextInput(attrs={'class': 'form-control'}),
		'sec_city': forms.TextInput(attrs={'class': 'form-control'}),
		'sec_pin': forms.TextInput(attrs={'class': 'form-control'}),
		}

	# def confirm_email(self):
	# 	email = self.cleaned_data.get('email')
	# 	qs = User.objects.filter(email = email)
	# 	print(qs)
	# 	if qs.exists():
	# 		raise forms.ValidationError("Email already exists")
	# 	else:
	# 		return email



