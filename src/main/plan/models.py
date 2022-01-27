from django.db import models
from customer.models import CustomerType
from item.models import Item,SubItem

class Plan(models.Model):
	p_id 		= models.CharField(max_length = 100,primary_key = True, unique = True,default = 'default')
	plan_desc = models.CharField(max_length = 200)
	customertype = models.ForeignKey(CustomerType,on_delete = models.CASCADE,default = 'default')
	item = models.ForeignKey(Item,on_delete = models.CASCADE,default = 'default')
	subitem = models.ForeignKey(SubItem,on_delete = models.CASCADE,default = 'default')

	def __str__(self):
		return self.plan_desc