from django.db import models
from customer.models import CustomerName,CustomerContact
from agency.models import AgencyDetail,AgencyContact
from plan.models import Plan
from item.models import Item,SubItem

# base_rate_choices = [(700,700),(500,500),(400,400)]

class Deal_one(models.Model):
	fct1				= models.IntegerField(blank = True, null = True)
	fct2				= models.IntegerField(blank = True, null = True)
	fct3				= models.IntegerField(blank = True, null = True)

	eff_rate1		= models.IntegerField(blank = True, null = True)
	eff_rate2		= models.IntegerField(blank = True, null = True)
	eff_rate3		= models.IntegerField(blank = True, null = True)

	base_rate1		= models.IntegerField(blank = True, null = True)
	base_rate2		= models.IntegerField(blank = True, null = True)
	base_rate3		= models.IntegerField(blank = True, null = True)

	slot1			= models.IntegerField(blank = True, null = True)
	slot2			= models.IntegerField(blank = True, null = True)
	slot3			= models.IntegerField(blank = True, null = True)

	subitem_id		= models.ForeignKey(SubItem,on_delete = models.CASCADE,default = 'default')
	# subitem_id2		= models.ForeignKey(SubItem,on_delete = models.CASCADE,default = 'default')
	# subitem_id3		= models.ForeignKey(SubItem,on_delete = models.CASCADE,default = 'default')

	actual_fct1		= models.IntegerField(blank = True, null = True)
	actual_fct2		= models.IntegerField(blank = True, null = True)
	actual_fct3		= models.IntegerField(blank = True, null = True)

	# total_fct		= models.IntegerField(blank = True, null = True)
	# total_members		= models.IntegerField(blank = True, null = True) #*****************************************


	##getting customer dropdown
	customer_id		= models.ForeignKey(CustomerName,on_delete = models.CASCADE,default = 'default')
	customer_contact = models.ForeignKey(CustomerContact,on_delete = models.CASCADE,default = 'default')

	##getting agency dropdown
	agency_id	 	= models.ForeignKey(AgencyDetail,on_delete = models.CASCADE,default = 'default')
	agency_contact  = models.ForeignKey(AgencyContact,on_delete = models.CASCADE,default = 'default')

	##getting plan dropdown
	plan_id 		= models.ForeignKey(Plan,on_delete = models.CASCADE,default = 'default')

	##getting item and subitem dropdown
	item_id			= models.ForeignKey(Item,on_delete = models.CASCADE,default = 'default')
	

	# def __str__(self):
	# 	return int(self.base_rate)

