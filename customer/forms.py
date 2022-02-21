from django import forms
from .models import CustomerType, CustomerName, CustomerContact


class Cust_type(forms.ModelForm):
	class Meta:
		model = CustomerType
		fields = '__all__'

class Cust_name(forms.ModelForm):
	ref_customertype = forms.ModelChoiceField(queryset= CustomerType.objects.all(),widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Client Type')

	class Meta:
		model = CustomerName
		fields = ['cname', 'brand_name',]


		widgets = {
			'cname' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder': 'Enter Client Name' }),
			'brand_name' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder': 'Enter Brand Name' }),
		}


class Cust_contact(forms.ModelForm):
	ref_cname = forms.ModelChoiceField(queryset= CustomerName.objects.all(), widget=forms.Select(attrs={'class':'form-select'}), empty_label = 'Select Client Name')
	class Meta:
		
		model = CustomerContact
		fields = '__all__'		

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
		
		
           