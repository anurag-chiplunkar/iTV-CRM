from django import forms
from .models import CustomerType, CustomerName, CustomerContact


class Cust_type(forms.ModelForm):
	# cust_type_form = forms.ModelChoiceField(queryset= Modelname.objects.all())
	class Meta:
		model = CustomerType
		fields = '__all__'

		# widget = {
		# 	'cust_type' : forms. 
		# }

class Cust_name(forms.ModelForm):
	cust_type_form = forms.ModelChoiceField(queryset= CustomerType.objects.all())

	class Meta:
		model = CustomerName
		fields = ['cname']

		widget = {
			'cust_name' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Enter Client Name' }),
			'cust_type' : forms.Select(attrs = {'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Enter Client Type' })
		}


class Cust_contact(forms.ModelForm):
	class Meta:
		cname_form = forms.ModelChoiceField(queryset= CustomerName.objects.all())
		model = CustomerContact
		fields = '__all__'

		widget = {
				'fname' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Enter first Name'}),
				'lname' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Enter last Name'}),
				'desg' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Enter desig'}),
				'email' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Enter email'}),
				'phone' : forms.Textarea(attrs = {'rows': 1,'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Enter phone number'}),
				'cname' : forms.Select(attrs = {'class' : 'form-control', 'style': 'resize:none;', 'placeholder': 'Enter name'})
		}