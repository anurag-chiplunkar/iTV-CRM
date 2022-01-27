from django import forms
from .models import bill
from django.db.models import Q


class generatebill(forms.ModelForm):
	# cust_name = forms.CharField(widget=forms.Textarea(attrs={'rows':1,'class': 'form-control','style':'resize:none;', 'placeholder': 'Type here'}))
	class Meta:
		model = bill
		fields = ['cust_name','phone']
		# field = '__all__'
		# exclude = ('items','price_unit','quantity','total','amt')
		widget = {
		'cust_name' : forms.Textarea(attrs={'rows':1,'class': 'form-control','style':'resize:none;', 'placeholder': 'Type here'}),
		'phone' : forms.Textarea(attrs={'rows':1,'class': 'form-control','style':'resize:none;', 'placeholder': 'Type here'})
		}