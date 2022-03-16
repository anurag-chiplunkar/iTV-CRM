from django.db import models
from datetime import date, datetime
from django.utils import timezone
from final_fct_nfct_deal.models import *
from agency_client.models import *
from nfct.models import *
from final_fct_nfct_deal.models import (

  FinalFctNfctDeal,
)
# from final_fct_nfct_deal.models import FinalFctNfctDeal
# Create your models here.

class Fct_deal(models.Model):
	"""Model of FCT for Final_fct_nfct_deal
	
	:dealid_fct_ref: Deal id of form
	:chan: Channel
	:dis: Dispersion
	:band1, band2, band3: Bands(0600-1200, 1200-1800, 1800-2400)
	:fct1, fct2, fct3: FCT values
	:eff_rate1, eff_rate2, eff_rate3: Effective rate values
	:rev1, rev2, rev3: Revenue values
	:total_rev: Total Revenue 
	:base_rate1, base_rate2, base_rate3: Base Rate
	:prev_yr_fct: Previous Year
	:curr_fct: Current Year
	
	:CharField: dealid_fct_ref, chan, dis, band1, band2, band3
	:IntegerField: fct1, fct2, fct3, base_rate1, base_rate2, base_rate3, prev_yr_fct, curr_fct
	:DecimalField: eff_rate1, eff_rate2, eff_rate3, rev1, rev2, rev3, total_rev"""

	dealid_fct_ref = models.CharField(max_length=100, default='default', primary_key=True)
	chan = models.CharField(max_length=1000,blank=True,null=True)
	# deal_id = models.CharField(max_length=500)
	dis = models.CharField(max_length=1000,blank=True,null=True)
	band1 = models.CharField(max_length=1000,blank=True,null=True)
	band2 = models.CharField(max_length=1000,blank=True,null=True)
	band3 = models.CharField(max_length=1000,blank=True,null=True)
	fct1 = models.IntegerField(blank=True,null=True,default='0')
	fct2 = models.IntegerField(blank=True,null=True,default='0')
	fct3 = models.IntegerField(blank=True,null=True,default='0')
	eff_rate1 = models.DecimalField(blank=True,null=True, max_digits=12, decimal_places=2)
	eff_rate2 = models.DecimalField(blank=True,null=True, max_digits=12, decimal_places=2)
	eff_rate3 = models.DecimalField(blank=True,null=True, max_digits=12, decimal_places=2)
	rev1 = models.DecimalField(blank=True,null=True, max_digits=12, decimal_places=2)
	rev2 = models.DecimalField(blank=True,null=True, max_digits=12, decimal_places=2)
	rev3 = models.DecimalField(blank=True,null=True, max_digits=12, decimal_places=2)
	total_rev = models.DecimalField(blank=True,null=True, max_digits=12, decimal_places=2)
	base_rate1 = models.IntegerField(blank=True,null=True)
	base_rate2 = models.IntegerField(blank=True,null=True)
	base_rate3 = models.IntegerField(blank=True,null=True)
	prev_yr_fct = models.IntegerField(blank=True,null=True)
	curr_fct = models.IntegerField(blank=True,null=True)

class Base(models.Model):
	"""Model for saving baserate
	
	:date: to save the current date
	:channel: Channels selection
	:dispersion: Dispersion selection
	:bands: Bands Selection
	:br: Saveing Base rate
	
	:DateTimeField: date
	:CharField: channel, dispersion, bands
	:IntegerField: br"""

	CHANNEL_CHOICES = [
	('INN','INN'),
	('NX','NX'),
	('IN UP','IN UP'),
	('MP','MP'),
	('RAJ','RAJ'),
	('PUN','PUN'),
	('HAR','HAR'),
	('GUJ','GUJ'),
	('NE NEWS','NE NEWS'),
	]
	date = models.DateTimeField(default=timezone.now)
	channel = models.CharField(max_length=1000,null=True,blank=True,choices=CHANNEL_CHOICES)
	dispersion = models.CharField(max_length=1000,null=True,blank=True)
	bands = models.CharField(max_length=1000,null=True,blank=True)
	br = models.IntegerField(null=True,blank=True)


class Disper(models.Model):
	"""Model for saving Dispersion
	
	:dis_list: Saving Dispersions
	
	:CharField: dis_list"""

	dis_list = models.CharField(max_length=255,primary_key=True)
	def __str__(self):
		return self.dis_list
	

class Channel(models.Model):
	"""Model for saving Channel
	
	:c_list: Saving Channel
	
	:CharField: c_list"""

	c_list = models.CharField(max_length=255,primary_key=True)

	def __str__(self):
		return self.c_list
	
class Band(models.Model):
	"""Model for saving Band
	
	:b_list: Saving Bands
	
	:CharField: b_list """

	b_list = models.CharField(max_length=255,primary_key=True)
	def __str__(self):
		return self.b_list

class Base_rate_table(models.Model):
	"""Model for saving baserate
	
	:unique_key: Stores the unique key
	:br: Saveing Base rate 
	
	:CharField: unique_key
	:IntegerField: br"""

	unique_key = models.CharField(max_length=255,default="default",null=True,blank=True)
	br = models.IntegerField()
	

	def __str__(self):
		return self.br


# single Fct_deal


class FinalFCT(models.Model):
	"""Model of FCT Common form for saving the details
	
	:deal_id: Saving Deal id
	:created_at: Saving date and time
	:executive: Executive Name from accounts app
	:reporting_manager: Reporting Manager from accounts app
	:RO_number: Release Order Number
	:RO_value: Realease Order Value
	:client_name_ref: Client Name reference from agency_client app
	:client_contact_ref: Client Contact details reference from agency_client app
	:agency_name_ref: Agency Name Reference from agency_client app
	:agency_contact_ref: Agency Contact details reference from agency_client app
	:brand_name_ref: Brand Name reference from agency_client app
	:fct_total_rev: FCT Total Revenue from deal_fct_nfct_deal app
	
	:CharField: deal_id, executive, reporting_manager, RO_number
	:DateTimeField: created_at
	:ForiegnKey: client_name_ref, client_contact_ref, agency_name_ref, agency_contact_ref, brand_name_ref
	:DecimalField: fct_total_rev """

	deal_id             = models.CharField(max_length = 100, primary_key = True, unique = True)
	created_at          = models.DateTimeField(auto_now_add = True)
	executive           = models.CharField(max_length= 255)
	reporting_manager   = models.CharField(max_length= 255)
	RO_number           = models.CharField(max_length=255)
	RO_value            = models.DecimalField(max_digits=12, decimal_places=2)
	client_name_ref     = models.ForeignKey(CustomerName,on_delete = models.CASCADE,default = 'default',related_name = 'clientfct')
	client_contact_ref  = models.ForeignKey(CustomerContact,on_delete = models.CASCADE,default = 'default')
	agency_name_ref     = models.ForeignKey(AgencyDetail,on_delete = models.CASCADE,default = 'default')
	agency_contact_ref  = models.ForeignKey(AgencyContact,on_delete = models.CASCADE,default = 'default')
	brand_name_ref      = models.ForeignKey(CustomerName,on_delete = models.CASCADE, default = 'default', related_name = 'brandfct')
	fct_total_rev = models.DecimalField(blank=True,null=True, max_digits=12, decimal_places=2)
	
	def __str__(self):
		return self.deal_id

class DealFct(models.Model):
	"""Model for Only FCT
	
	:dealid_fct: Deal id of form
	:chan: Channel
	:dis: Dispersion
	:band1, band2, band3: Bands(0600-1200, 1200-1800, 1800-2400)
	:fct1, fct2, fct3: FCT values
	:eff_rate1, eff_rate2, eff_rate3: Effective rate values
	:rev1, rev2, rev3: Revenue values
	:total_rev: Total Revenue 
	:base_rate1, base_rate2, base_rate3: Base Rate
	:prev_yr_fct: Previous Year
	:curr_fct: Current Year
	
	:CharField: dealid_fct, chan, dis, band1, band2, band3
	:IntegerField: fct1, fct2, fct3, base_rate1, base_rate2, base_rate3, prev_yr_fct, curr_fct
	:DecimalField: eff_rate1, eff_rate2, eff_rate3, rev1, rev2, rev3, total_rev"""

	dealid_fct = models.CharField(max_length=100, default='default', primary_key=True)
	chan = models.CharField(max_length=1000,blank=True,null=True)
	# deal_id = models.CharField(max_length=500)
	dis = models.CharField(max_length=1000,blank=True,null=True)
	band1 = models.CharField(max_length=1000,blank=True,null=True)
	band2 = models.CharField(max_length=1000,blank=True,null=True)
	band3 = models.CharField(max_length=1000,blank=True,null=True)
	fct1 = models.IntegerField(blank=True,null=True)
	fct2 = models.IntegerField(blank=True,null=True)
	fct3 = models.IntegerField(blank=True,null=True)
	eff_rate1 = models.DecimalField(blank=True,null=True, max_digits=12, decimal_places=2)
	eff_rate2 = models.DecimalField(blank=True,null=True,max_digits=12, decimal_places=2)
	eff_rate3 = models.DecimalField(blank=True,null=True, max_digits=12, decimal_places=2)
	rev1 = models.DecimalField(blank=True,null=True, max_digits=12, decimal_places=2)
	rev2 = models.DecimalField(blank=True,null=True, max_digits=12, decimal_places=2)
	rev3 = models.DecimalField(blank=True,null=True, max_digits=12, decimal_places=2)
	total_rev = models.DecimalField(blank=True,null=True, max_digits=12, decimal_places=2)
	base_rate1 = models.IntegerField(blank=True,null=True, default='0')
	base_rate2 = models.IntegerField(blank=True,null=True, default='0')
	base_rate3 = models.IntegerField(blank=True,null=True, default='0')
	prev_yr_fct = models.IntegerField(blank=True,null=True)
	curr_fct = models.IntegerField(blank=True,null=True)


