from django.db import models
from agency_client.models import *
import datetime

class AFPProgramName(models.Model):
	"""	Registration of Program Names"""
	program_name = models.CharField(max_length = 100, primary_key = True, unique = True)

	def __str__(self):
		return self.program_name

class AFPChannels(models.Model):
	"""Registration of Channel Names"""
	channels = models.CharField(max_length = 200, primary_key = True, unique = True)

	def __str__(self):
		return self.channels

class AFPPromos(models.Model):
	"""Registration of Promos names"""
	promos = models.CharField(max_length = 100, primary_key = True, unique = True)
	
	def __str__(self):
		return self.promos

class AFPSlots(models.Model):
	"""Registration of slot names"""
	slot = models.CharField(max_length = 100, primary_key = True, unique = True)
	
	def __str__(self):
		return self.slot

class AFPBaseRate(models.Model):
	br_unique_key = models.CharField(max_length=100, primary_key = True, unique = True)
	baserate = models.IntegerField()
	def __str__(self):
		return self.baserate


class AFPDeal(models.Model):
	"""Registration of AFP Deals"""
	afp_deal_id         = models.CharField(max_length = 20)
	# ref_program_name    = models.ForeignKey(AFPProgramName, on_delete = models.CASCADE,verbose_name = 'program Name')
	ref_program_name	= models.CharField(max_length = 200,verbose_name = 'program Name')
	ref_channels        = models.ForeignKey(AFPChannels, on_delete = models.CASCADE,verbose_name = 'channel')
	# ref_promos          = models.ForeignKey(AFPPromos, on_delete = models.CASCADE,verbose_name = 'promo')
	ref_promos			= models.CharField(max_length = 200,verbose_name = 'promos')
	ref_slot            = models.ForeignKey(AFPSlots, on_delete = models.CASCADE,verbose_name = 'slot')
	afp_eff_rate        = models.DecimalField(verbose_name = 'effective Rate', max_digits = 12, decimal_places = 2)
	afp_base_rate       = models.IntegerField(verbose_name = 'base Rate')
	afp_created			= models.DateTimeField(auto_now_add = True)

class AFPDealFinalTotal(models.Model):
	afp_final_total = models.DecimalField(primary_key = True, max_digits = 12, decimal_places = 2)
	afp_final_deal_id = models.CharField(max_length = 100,default = 'default')


class FinalAFPDeal(models.Model):
	afpdeal_id          	= models.CharField(max_length = 100, primary_key = True, unique = True)
	afp_ro_number			= models.CharField(max_length = 100)
	afp_ro_value			= models.DecimalField(max_digits = 12, decimal_places = 2)
	afp_client_name_ref     = models.ForeignKey(CustomerName,on_delete = models.CASCADE,default = 'default',related_name = 'client2')
	afp_client_contact_ref  = models.ForeignKey(CustomerContact,on_delete = models.CASCADE,default = 'default')
	afp_agency_name_ref     = models.ForeignKey(AgencyDetail,on_delete = models.CASCADE,default = 'default')
	afp_agency_contact_ref  = models.ForeignKey(AgencyContact,on_delete = models.CASCADE,default = 'default')
	afp_brand_name_ref      = models.ForeignKey(CustomerName,on_delete = models.CASCADE, default = 'default', related_name = 'brand2')
	afp_total_ref           = models.DecimalField(max_digits = 12, decimal_places = 2, null=True, blank=True)
	afp_deal_created		= models.DateTimeField(auto_now_add = True)
	
	def __str__(self):
		return self.afp_deal_id
