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
	agency = forms.ModelChoiceField(queryset = AgencyDetail.objects.all(),widget = forms.Select(attrs = {'class':'custom-select'}))
	class Meta:
		model = AgencyContact
		fields = '__all__'
		exclude = ('agency_details',)

		widgets = {
		'pri_firstName' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter First Name'}),
		'pri_lastName' :  forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Last Name'}),
		'pri_designation' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your designation'}),
		'pri_email' : forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Enter your email id'}),
		'pri_phone' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your phone'}),
		'pri_landline': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your landline'}),
		'pri_flatno': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter flat number'}),
		'pri_street': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter street address'}),
		'pri_landmark': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter landmark if any'}),
		'pri_city': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your city'}),
		'pri_pin': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter pincode'}),

		'sec_firstName' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter First Name'}),
		'sec_lastName' :  forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Last Name'}),
		'sec_designation' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your designation'}),
		'sec_email' : forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Enter your email id'}),
		'sec_phone' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your phone'}),
		'sec_landline': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your landline'}),
		'sec_flatno': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter flat number'}),
		'sec_street': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter street address'}),
		'sec_landmark': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter landmark if any'}),
		'sec_city': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your city'}),
		'sec_pin': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter pincode'}),
		}




