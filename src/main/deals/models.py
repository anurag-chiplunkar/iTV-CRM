from django.db import models

class ChannelNFCT(models.Model):
	channel = models.CharField(max_length = 100, primary_key = True, unique = True)

	def __str__(self):
		return self.channel

class ElementNFCT(models.Model):
	element = models.CharField(max_length = 100, primary_key = True, unique = True)

	def __str__(self):
		return self.element

class BaseRateNFCT(models.Model):
	unique_key	= models.CharField(max_length = 100, primary_key = True,unique = True,default = 'default')
	base_rate	= models.IntegerField()

	def __str__(self):
		return self.base_rate

class DealNFCT(models.Model):
	seconds		= models.IntegerField(null = True, blank = True)
	days		= models.IntegerField(null = True, blank = True)
	months		= models.IntegerField(null = True, blank = True)
	eff_rate 	= models.IntegerField()
	frequency 	= models.IntegerField()
	total_sec 	= models.IntegerField()
	total_cost 	= models.IntegerField()

	channel_nfct 	= models.ForeignKey(ChannelNFCT,on_delete = models.CASCADE,default = 'default')
	element_nfct 	= models.ForeignKey(ElementNFCT,on_delete = models.CASCADE,default = 'default')
	baserate_nfct 	= models.ForeignKey(BaseRateNFCT,on_delete = models.CASCADE,default = 'default')


	def __str__(self):
		return self.eff_rate