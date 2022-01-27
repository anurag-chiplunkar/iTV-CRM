from django import forms
from django.contrib.auth import get_user_model
from . models import Plan
from customer.models import CustomerType
from item.models import Item,SubItem

User = get_user_model()

class Plan_details(forms.Form):
	plan_desc = forms.CharField(
		widget = forms.TextInput(
			attrs = {
				"class":"form-control",
				"id":"form_mail",
				"placeholder":"Enter your plan_desc"
				}))

	customertype = forms.ModelChoiceField(queryset = CustomerType.objects.all() )

	item = forms.ModelChoiceField(queryset = Item.objects.all() )

	subitem = forms.ModelChoiceField(queryset = SubItem.objects.all() )