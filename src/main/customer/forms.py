from django import forms
from django.contrib.auth import get_user_model
from . models import CustomerType,CustomerName,CustomerContact
	##cust type and cust name dropdown

User = get_user_model()

class Cust_type(forms.Form):
	customer_type = forms.CharField(
		widget = forms.TextInput(
			attrs = {
				"class":"form-control",
				"id":"client_type",
				"placeholder":"Enter customer type"
				}))

class Cust_name(forms.Form):
	name = forms.CharField(
		widget = forms.TextInput(
			attrs = {
				"class":"form-control",
				"id":"client_name",
				"placeholder":"Name of the customer"
				}))

	##to get a dropdown in the cust_name form. Dropdown for selecting cust type
	custType = forms.ModelChoiceField(queryset = CustomerType.objects.all() )

class Cust_contacts(forms.Form):
	firstName = forms.CharField(
	widget = forms.TextInput(
		attrs = {
			"class":"form-control",
			"id":"client_pri_ctc",
			"placeholder":"Enter your first name"
			}))

	lastName = forms.CharField(
	widget = forms.TextInput(
		attrs = {
			"class":"form-control",
			"id":"client_pri_ctc2",
			"placeholder":"Enter your last name"
			}))

	designation = forms.CharField(
	widget = forms.TextInput(
		attrs = {
			"class":"form-control",
			"id":"client_pri_desg",
			"placeholder":"Enter your designation"
			}))

	email = forms.CharField(
	widget = forms.TextInput(
		attrs = {
			"class":"form-control",
			"id":"client_pri_email",
			"placeholder":"Enter your email id"
			}))

	phone = forms.CharField(
	widget = forms.TextInput(
		attrs = {
			"class":"form-control",
			"id":"client_pri_phone",
			"placeholder":"Enter your phone number"
			}))

	cust_name = forms.ModelChoiceField(queryset = CustomerName.objects.all())
