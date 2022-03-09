from django import forms
from django.contrib.auth import get_user_model
from . models import AgencyDetail,AgencyContact
from . models import CustomerType, CustomerName, CustomerContact


class Agency_details(forms.ModelForm):
	ccreg_no = forms.ModelChoiceField(queryset = CustomerName.objects.all(),widget = forms.Select(attrs = {'class':'form-select'}), empty_label='Select the Client')
	
	class Meta:
		model = AgencyDetail
		fields = '__all__'
		exclude = ('a_id',)			##exclude this because this is automatically generated in views.py

		widgets = {
		'agency_name' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Name'}),
		'agency_officeno' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Office Flat Number'}),
		'agency_street' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Street'}),
		'agency_state' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter State'}),
		'agency_landmark' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Landmark'}),
		'agency_city' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter City'}),
		'agency_pin' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Pincode'}),
		# 'ccreg_no' : forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Pincode'}),
		}

class Agency_contacts(forms.ModelForm):
	##empty_label is for giving a placeholder to the dropdown
	agency = forms.ModelChoiceField(queryset = AgencyDetail.objects.all(),widget = forms.Select(attrs = {'class':'form-select'}), empty_label='Select the Agency')
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






class Cust_type(forms.ModelForm):
	class Meta:
		model = CustomerType
		fields = '__all__'

class Cust_name(forms.ModelForm):
	ref_customertype = forms.ModelChoiceField(queryset= CustomerType.objects.all(),widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Client Type')

	class Meta:
		model = CustomerName
		fields = ['cname', 'brand_name','creg_no']
		# exclude = ('ref_customertype',)


		widgets = {
			'cname' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder': 'Enter Client Name' }),
			'brand_name' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder': 'Enter Brand Name' }),
			'creg_no' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder': 'Enter Registration Number' }),
			# 'ref_customertype' : forms.Select(attrs = {'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Enter Client Type' })
		}
		


class Cust_contact(forms.ModelForm):
	ref_creg_no = forms.ModelChoiceField(queryset= CustomerName.objects.all(), widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Registration Number')
	# ref_cname = forms.ModelChoiceField(queryset= CustomerName.objects.all(), widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Registration Number')

	class Meta:
		
		model = CustomerContact
		fields = '__all__'	
		exclude = ('ref_creg_no',)	

		widgets = {
				'pri_fname' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Enter First Name'}),
				'pri_lname' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Enter Last Name'}),
				'pri_desg' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Enter Designation'}),
				'pri_email' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Enter Email'}),
				'pri_phone' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Enter Phone Number'}),
				'pri_landline' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Landline'}),
				'pri_flatno' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'House/Flat No.'}),
				'pri_streetname' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Street Name'}),
				'pri_landmark' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Landmark'}),
				'pri_city' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'City'}),
				'pri_pincode' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Pincode'}),

				'sec_fname' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Enter First Name'}),
				'sec_lname' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Enter Last Name'}),
				'sec_desg' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Enter Designation'}),
				'sec_email' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Enter Email'}),
				'sec_phone' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Enter Phone Number'}),
				'sec_landline' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Landline'}),
				'sec_flatno' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'House/Flat No.'}),
				'sec_streetname' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Street Name'}),
				'sec_landmark' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Landmark'}),
				'sec_city' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'City'}),
				'sec_pincode' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Pincode'}),

		}
		
		
           