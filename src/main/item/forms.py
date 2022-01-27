from django import forms
from django.contrib.auth import get_user_model
from . models import Item

User = get_user_model()

class Item_details(forms.Form):
	item_type = forms.CharField(
		widget = forms.TextInput(
			attrs = {
				"class":"form-control",
				"id":"form_mail",
				"placeholder":"Enter item type"
				}))



class Subitem_details(forms.Form):
	subitem_name = forms.CharField(
		widget = forms.TextInput(
			attrs = {
				"class":"form-control",
				"id":"form_mail",
				"placeholder":"Enter subitem name"
				}))

	uom_desc = forms.CharField(
		widget = forms.TextInput(
			attrs = {
				"class":"form-control",
				"id":"form_mail",
				"placeholder":"Enter subitem uom desc"
				}))

	uom_quantity = forms.IntegerField(
		widget = forms.NumberInput(
			attrs = {
				"class":"form-control",
				"id":"form_mail",
				"placeholder":"Enter subitem uom quantity"
				}))

	uom_quantity_rate = forms.IntegerField(
		widget = forms.NumberInput(
			attrs = {
				"class":"form-control",
				"id":"form_mail",
				"placeholder":"Enter subitem uom quantity rate"
				}))

	item = forms.ModelChoiceField(queryset = Item.objects.all())