from django.db import models
from agency_client.models import *
import datetime

class AFPProgramName(models.Model):
	"""	Registration of Program Names

	:program_name: Saving AFP programme names

	:CharField: program_name"""

	program_name = models.CharField(max_length = 100, primary_key = True, unique = True)

	def __str__(self):
		return self.program_name

class AFPChannels(models.Model):
	"""Registration of Channel Names
	
	:channels: Saving AFP channels
	
	:CharField: channels"""

	channels = models.CharField(max_length = 200, primary_key = True, unique = True)

	def __str__(self):
		return self.channels

class AFPPromos(models.Model):
	"""Registration of Promos names
	
	:promos: Saving AFP promos
	
	:CharField: promos"""

	promos = models.CharField(max_length = 100, primary_key = True, unique = True)
	
	def __str__(self):
		return self.promos

class AFPSlots(models.Model):
	"""Registration of slot names
	
	:slot: Saving AFP slots
	
	:CharField: slot"""

	slot = models.CharField(max_length = 100, primary_key = True, unique = True)
	
	def __str__(self):
		return self.slot

class AFPBaseRate(models.Model):
	"""Filling base rates for AFP
	
	:br_unique_key: Stores the unique key for base rates
	
	:CharField: br_unique_key
	:IntegerField: saves base rates for respective unique key"""

	br_unique_key = models.CharField(max_length=100, primary_key = True, unique = True)
	baserate = models.IntegerField()
	def __str__(self):
		return self.baserate


class AFPDeal(models.Model):
	"""Registration of AFP Deals
	
	:afp_deal_id: saving afp deal id
	:ref_program_name: saving programme name from AFPProgramName model
	:description: adding description of programme name
	ref_channels: saving channel name from AFPChannels model
	ref_promos: saving promos in database
	ref_slot: saving slot from AFPSlots model
	afp_eff_rate: saving effective rate in database
	afp_base_rate: saving base rate in database
	afp_created: saving date and time of deal creation
	
	:CharField: afp_deal_id, description, ref_promos
	:Foreign Key: ref_program_name, ref_channels, ref_slot
	:DecimalField: afp_eff_rate
	:DateTimeField: afp_created
	:IntegerField: afp_base_rate"""

	afp_deal_id         = models.CharField(max_length = 20)
	ref_program_name    = models.ForeignKey(AFPProgramName, on_delete = models.CASCADE,verbose_name = 'program Name')
	description 		= models.CharField(max_length=255,null=True,blank=True)
	# ref_program_name	= models.CharField(max_length = 200,verbose_name = 'program Name')
	ref_channels        = models.ForeignKey(AFPChannels, on_delete = models.CASCADE,verbose_name = 'channel')
	# ref_promos          = models.ForeignKey(AFPPromos, on_delete = models.CASCADE,verbose_name = 'promo')
	ref_promos			= models.CharField(max_length = 200,verbose_name = 'promos')
	ref_slot            = models.ForeignKey(AFPSlots, on_delete = models.CASCADE,verbose_name = 'slot')
	afp_eff_rate        = models.DecimalField(verbose_name = 'effective Rate', max_digits = 12, decimal_places = 2)
	afp_base_rate       = models.IntegerField(verbose_name = 'base Rate')
	afp_created			= models.DateTimeField(auto_now_add = True)

class AFPDealFinalTotal(models.Model):
	"""Saving AFP final total
	
	:afp_final_total: storing final total of AFP
	:afp_final_deal_id: storing AFP deal id
	
	:DecimalField: afp_final_total
	:CharField: afp_final_deal_id"""

	afp_final_total = models.DecimalField(primary_key = True, max_digits = 12, decimal_places = 2)
	afp_final_deal_id = models.CharField(max_length = 100,default = 'default')


class FinalAFPDeal(models.Model):
	"""Saving common form of AFP
	
	:afpdeal_id: storing AFP deal id
	:afp_ro_number: saving AFP RO number
	:afp_ro_value: saving AFP RO value
	:afp_client_name_ref: saving AFP client name from CustomerName model
	:afp_client_contact_ref: saving AFP client contact name from CustomerContact model
	:afp_agency_name_ref: saving AFP agency name from AgencyDetail model
	:afp_agency_contact_ref: saving AFP agency contact from AgencyContact model
	:afp_brand_name_ref: saving AFP brand name from CustomerName
	:afp_total_ref: saving AFP total
	:afp_deal_created: saving date and time of AFP deal creation

	:CharField: afpdeal_id,afp_ro_number
	:DecimalField: afp_ro_value, afp_total_ref
	:DateTimeField: afp_deal_created
	:Foreign Key: afp_client_name_ref, afp_client_contact_ref, afp_agency_name_ref, afp_agency_contact_ref, afp_brand_name_ref
	"""
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
