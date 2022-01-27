from django.db import models

class Item(models.Model):
	item_id 		= models.CharField(max_length = 100,primary_key = True, unique = True,default = 'default')
	item_type 		= models.CharField(max_length = 200)


	def __str__(self):
		return self.item_type

class SubItem(models.Model):
	subitem_id 		= models.CharField(max_length = 100, primary_key = True, unique = True, default = 'default')
	subitem_name 	= models.CharField(max_length = 200)
	uom_desc 		= models.CharField(max_length = 100)
	uom_quantity	= models.IntegerField()
	uom_quantity_rate = models.IntegerField()
	item = models.ForeignKey(Item,on_delete = models.CASCADE,default = 'default')

	def __str__(self):
		return self.uom_desc

