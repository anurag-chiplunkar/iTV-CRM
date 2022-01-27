from django import forms
from django.contrib.auth import get_user_model
from . models import AgencyDetail,AgencyContact

User = get_user_model()

class Agency_details(forms.Form):
	agency_name = forms.CharField(
		widget = forms.TextInput(
			attrs = {
				"class":"form-control",
				"id":"agncy_name",
				"placeholder":"Enter your agency name"
				}))

	agency_state = forms.CharField(
		widget = forms.TextInput(
			attrs = {
				"class":"form-control",
				"id":"agncy_loc",
				"placeholder":"Enter your agency state"
				}))

	

class Agency_contacts(forms.Form):
	firstName = forms.CharField(
	widget = forms.TextInput(
		attrs = {
			"class":"form-control",
			"id":"agncy_pri_ctc",
			"placeholder":"Name your first name"
			}))

	lastName = forms.CharField(
	widget = forms.TextInput(
		attrs = {
			"class":"form-control",
			"id":"agncy_pri_ctc2",
			"placeholder":"Enter your last name"
			}))

	designation = forms.CharField(
	widget = forms.TextInput(
		attrs = {
			"class":"form-control",
			"id":"agncy_pri_desg",
			"placeholder":"designation"
			}))

	email = forms.CharField(
	widget = forms.TextInput(
		attrs = {
			"class":"form-control",
			"id":"agncy_pri_email",
			"placeholder":"email@domain.com"
			}))

	phone = forms.CharField(
	widget = forms.TextInput(
		attrs = {
			"class":"form-control",
			"id":"agncy_pri_phone",
			"placeholder":"Phone number"
			}))

	##this will create a dropdown input field which will contain all the objects of the agencydetail model
	agency = forms.ModelChoiceField(queryset = AgencyDetail.objects.all())


