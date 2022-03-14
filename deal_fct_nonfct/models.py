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
	"""Saving FCT deal in database
	:dealid_fct_ref: saves fct deal id in database
	:chan: saves channel
	:dis: saves dispersion
	:band1: saves first band
	:band2: saves second band
	:band3: saves third band
	:fct1: saves first fct seconds
	:fct2: saves second fct seconds
	:fct3: saves third fct seconds
	:eff_rate1: saves first effective rate
	:eff_rate2: saves second effective rate
	:eff_rate3: saves third effective rate
	:rev1: saves first revenue
	:rev2: saves second revenue
	:rev3: saves third revenue
	:total_rev: saves sum of 3 revenues
	:base_rate1: saves base rate of first row
	:base_rate2: saves base rate of second row
	:base_rate3: saves base rate of third row
	:CharField: dealid_fct_ref, chan, dis, band1, band2, band3
	:DecimalField: eff_rate1, eff_rate2, eff_rate3, rev1, rev2, rev3, total_rev
	:IntegerField: base_rate1, base_rate2, base_rate3, prev_yr_fct,  curr_fct
	"""
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
	"""Saves Dispersion into database
	:dis_list: saves dispersion
	:CharField: dis_list
	:Primary Key: dis_list"""
	dis_list = models.CharField(max_length=255,primary_key=True)
	def __str__(self):
		return self.dis_list
	

class Channel(models.Model):
	"""Saves channels into database
	:c_list: saves channels
	:CharField: c_list
	:Primary Key: c_list"""
	c_list = models.CharField(max_length=255,primary_key=True)

	def __str__(self):
		return self.c_list
	
class Band(models.Model):
	"""Saves Band into database
	:b_list: saves band
	:CharField: b_list
	:Primary Key: b_list"""
	b_list = models.CharField(max_length=255,primary_key=True)
	def __str__(self):
		return self.b_list

class Base_rate_table(models.Model):
	"""Filling base rates for AFP
	
	:br_unique_key: Stores the unique key for base rates
	:br: saves base rate

	:CharField: br_unique_key
	:IntegerField: saves base rates for respective unique key"""
	unique_key = models.CharField(max_length=255,default="default",null=True,blank=True)
	br = models.IntegerField()
	

	def __str__(self):
		return self.br


# single Fct_deal


class FinalFCT(models.Model):
	"""Saves common form and some other fields
	:deal_id saves deal id of fct common form
	:created_at: saves date and time of FCT form creation
	:executive: saves executive name
	:reporting_manager: saves reporting manager of current executive
	:RO_number: saves RO number
	:RO_value: saves RO value or RO amount
	:client_name_ref: saves client name in database from CustomerName model
	:client_contact_ref: saves client contact from CustomerContact model
	:agency_name_ref: saves agency name from AgencyDetail model
	:agency_contact_ref: saves agency contact from AgencyContact model
	:brand_name_ref: saves brand name from CustomerName model
	:fct_total_rev: saves FCT total revenue

	:CharField: deal_id, executive, reporting_manager, RO_number
	:DecimalField: RO_value, fct_total_rev
	:DateTimeField: created_at
	:Primary Key: deal_id
	:Unique Key: deal_id
	"""
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


