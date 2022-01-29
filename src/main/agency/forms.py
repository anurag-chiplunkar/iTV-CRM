from django import forms
from django.contrib.auth import get_user_model
from . models import AgencyDetail,AgencyContact

class Agency_details(forms.ModelForm):
	class Meta:
		model = AgencyDetail
		fields = '__all__'
		exclude = ('a_id',)			##exclude this because this is automatically generated in views.py

		widget = {
		'agency_name' : forms.TextInput(attrs={'placeholder': 'Enter Agency Name'}),
		'agency_state' : forms.TextInput(attrs={'placeholder': 'Enter Agency State'})
		}

class Agency_contacts(forms.ModelForm):
	agency = forms.ModelChoiceField(queryset = AgencyDetail.objects.all())
	class Meta:
		model = AgencyContact
		fields = '__all__'
		exclude = ('agency_details',)

		widget = {
		'firstName' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter First Name'}),
		'lastName' :  forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Last Name'}),
		'designation' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your designation'}),
		'email' : forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Enter your email id'}),
		'phone' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your phone'}),
		'agency' : forms.Select(attrs={'class':'custom-select'})
		}




