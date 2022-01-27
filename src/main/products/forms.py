from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

dispersion = [
	('25%,50%,50%, 25%,50%,50%'),
	('50%, 50%, 50%, 50%'),
	('33%, 33%, 33%,33%, 33%, 33%')
	]

bands = [
	('0600 - 1200, 0600 - 1200'),
	('1200 - 1800", "1200 - 1800'),
	('1800 - 2400", "1800 - 2400')
]



class Products(forms.Form):

	# disp = forms.ChoiceField(choices = dispersion)

	# band = forms.ChoiceField(choices = bands)

	disp = forms.CharField(
		widget = forms.TextInput(
			attrs = {
				"class" : "form-control",
				"id" : "form_base",
				"placeholder" : "Dispersion"
			}))

	band = forms.CharField(
		widget = forms.TextInput(
			attrs = {
				"class" : "form-control",
				"id" : "form_base",
				"placeholder" : "Bands"
			}))

	base_rate = forms.CharField(
		widget = forms.TextInput(
			attrs = {
				"class" : "form-control",
				"id" : "form_base",
				"placeholder" : "Base Rate"
			}))

	eff_rate = forms.CharField(
		widget = forms.TextInput(
			attrs = {
				"class" : "form-control",
				"id" : "form_base",
				"placeholder" : "Effective Rate"
			}))

	other_dispersion = forms.CharField(
		widget = forms.TextInput(
			attrs = {
				"class" : "form-control",
				"id" : "form_base",
				"placeholder" : "Other Dispersion"
			}))