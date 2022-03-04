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
	eff_rate1 = models.IntegerField(blank=True,null=True)
	eff_rate2 = models.IntegerField(blank=True,null=True)
	eff_rate3 = models.IntegerField(blank=True,null=True)
	rev1 = models.IntegerField(blank=True,null=True)
	rev2 = models.IntegerField(blank=True,null=True)
	rev3 = models.IntegerField(blank=True,null=True)
	total_rev = models.IntegerField(blank=True,null=True)
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
	dis_list = models.CharField(max_length=255,primary_key=True)
	def __str__(self):
		return self.dis_list
	

class Channel(models.Model):
	c_list = models.CharField(max_length=255,primary_key=True)

	def __str__(self):
		return self.c_list
	
class Band(models.Model):
	b_list = models.CharField(max_length=255,primary_key=True)
	def __str__(self):
		return self.b_list

class Base_rate_table(models.Model):
	unique_key = models.CharField(max_length=255,default="default",null=True,blank=True)
	br = models.IntegerField()
	

	def __str__(self):
		return self.br


# single Fct_deal


class FinalFCT(models.Model):
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
    fct_total_rev = models.IntegerField(blank=True,null=True)


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
	eff_rate1 = models.IntegerField(blank=True,null=True)
	eff_rate2 = models.IntegerField(blank=True,null=True)
	eff_rate3 = models.IntegerField(blank=True,null=True)
	rev1 = models.IntegerField(blank=True,null=True)
	rev2 = models.IntegerField(blank=True,null=True)
	rev3 = models.IntegerField(blank=True,null=True)
	total_rev = models.IntegerField(blank=True,null=True)
	base_rate1 = models.IntegerField(blank=True,null=True)
	base_rate2 = models.IntegerField(blank=True,null=True)
	base_rate3 = models.IntegerField(blank=True,null=True)
	prev_yr_fct = models.IntegerField(blank=True,null=True)
	curr_fct = models.IntegerField(blank=True,null=True)


