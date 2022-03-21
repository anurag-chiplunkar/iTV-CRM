from pyexpat import model
from django.db import models
# from final_fct_nfct_deal.models import FinalFctNfctDeal
from agency_client.models import *

# from deal_fct_nonfct.models import (Fct_deal,)
CHANNEL_CHOICE = [
        ('INN','INN'),
        ('NX','NX'),
        ('GUJ','GUJ'),
        ('HAR','HAR'),
        ('MP','MP'),
        ('NE NEWS','NE NEWS'),
        ('PUN','PUN'),
        ('RAJ','RAJ'),
        ('UP','UP'),
    ]

ELEMENT_CHOICE = [
        ('Aston','Aston'),
        ('L Band','L Band'),
        ('Logo Bug','Logo Bug'),
        ('Headline Sponsership Tag','Headline Sponsership Tag'),
        ('Ticker','Ticker'),
        ('Weather Branding','Weather Branding'),
    ]

durations_choices = (
    ('days', 'Days'),
    ('months', 'Months')

)

class NFCT_Base_Rate(models.Model):
    """docstring for NFCT_Base_Rate
	Adding of Base Rates
    :nfct_unique_key: saves unique key for each base rate
    :channel: saves channels
    :element: saves element
    :nfct_baserate: saves NFCT base rates

    :CharField: nfct_unique_key, channel, element
    :IntegerField: nfct_baserate"""

    nfct_unique_key = models.CharField(max_length=100,null=True,blank=True)
    channel = models.CharField(max_length=255,choices=CHANNEL_CHOICE)
    element = models.CharField(max_length=255,choices=ELEMENT_CHOICE)
    nfct_baserate = models.IntegerField(null=True,blank=True)

class Deal_nfct(models.Model):
    """Saves NFCT deal
    
    :main_dealid_nfct_ref: saves deal id of NFCT
    :channel: saves channels
    :element: saves element
    :durations: saves durations
    :duration_in: saves duration_in
    :er: saves effective rate
    :freq: saves frequency
    :total_seconds: saves calculted total seconds
    :base_rate: saves base rate for chosen channel and element
    :fct_total: saves FCT total
    :nfct_total: saves NFCT total
    :total: saves calculated total of FCT and NFCT
    :created_at: saves date and time of deal creation

    :CharField: main_dealid_nfct_ref, channel, element, durations
    :DecimalField: er, fct_total, nfct_total, total
    :IntegerField: duration_in, freq, base_rate
    :DateTimeField: created_at
    """
    main_dealid_nfct_ref = models.CharField(max_length=100, default='default', null=True, blank=True)
    channel = models.CharField(max_length=255,choices=CHANNEL_CHOICE)
    element = models.CharField(max_length=255,choices=ELEMENT_CHOICE)
    durations = models.CharField(max_length = 6, null = True, blank = True, choices = durations_choices)
    duration_in = models.IntegerField(null = True, blank = True)
    er = models.DecimalField(null=True,blank=True, max_digits=12, decimal_places=2)
    freq = models.IntegerField(null=True,blank=True)
    total_seconds = models.IntegerField(null=True,blank=True)
    base_rate = models.IntegerField(null = True, blank = True)
    fct_total = models.DecimalField(null=True,blank=True, max_digits=12, decimal_places=2)
    nfct_total = models.DecimalField(null=True,blank=True, max_digits=12, decimal_places=2)
    total = models.DecimalField(null=True,blank=True, max_digits=12, decimal_places=2)
    created_at  = models.DateTimeField(auto_now_add = True)
    

class NFCTGrandTotal(models.Model):
    """Saves NFCT grand total
    
    :dealid_nfct_ref: saves deal id of NFCT
    :nfct_grandtotal: saves calculated NFCT grand total
    
    :CharField: dealid_nfct_ref
    :DecimalField: nfct_grandtotal
    :Primary Key: nfct_grandtotal
    """
    dealid_nfct_ref = models.CharField(max_length=100, default='default')
    nfct_grandtotal = models.DecimalField(primary_key=True, max_digits=12, decimal_places=2)


# single NFCT

class FinalNFCT(models.Model):
    """Saves common form and some other fields
	:deal_id: saves deal id of fct common form
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
	:grandtotal: saves grand total revenue

	:CharField: deal_id, executive, reporting_manager, RO_number
	:DecimalField: RO_value, grandtotal
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
    client_name_ref     = models.ForeignKey(CustomerName,on_delete = models.CASCADE,default = 'default',related_name = 'clientnfct')
    client_contact_ref  = models.ForeignKey(CustomerContact,on_delete = models.CASCADE,default = 'default')
    agency_name_ref     = models.ForeignKey(AgencyDetail,on_delete = models.CASCADE,default = 'default')
    agency_contact_ref  = models.ForeignKey(AgencyContact,on_delete = models.CASCADE,default = 'default')
    brand_name_ref      = models.ForeignKey(CustomerName,on_delete = models.CASCADE, default = 'default', related_name = 'brandnfct')
    grandtotal = models.DecimalField(null=True,blank=True, max_digits=12, decimal_places=2)

    def __str__(self):
        return self.deal_id




class NFCTDeal(models.Model):
    dealid_nfct = models.CharField(max_length=100, default='default', null=True, blank=True)
    channel = models.CharField(max_length=255,choices=CHANNEL_CHOICE)
    element = models.CharField(max_length=255,choices=ELEMENT_CHOICE)
    durations = models.CharField(max_length = 6, null = True, blank = True, choices = durations_choices)
    duration_in = models.IntegerField(null = True, blank = True)
    er = models.DecimalField(null=True,blank=True, max_digits=12, decimal_places=2)
    freq = models.IntegerField(null=True,blank=True)
    total_seconds = models.IntegerField(null=True,blank=True)
    base_rate = models.IntegerField(null = True, blank = True)
    nfct_total = models.DecimalField(null=True,blank=True, max_digits=12, decimal_places=2)
    
    

class DealNFCTGrandTotal(models.Model):
    dealid_nfct_ref = models.CharField(max_length=100, default='default')
    nfct_grand_total = models.DecimalField(primary_key=True, max_digits=12, decimal_places=2)















# class NFCT_Channels(models.Model):
# 	"""docstring for NFCT_Channels
# 	Registration of Channel Names"""
# 	nfct_channels = models.CharField(max_length = 200, primary_key = True, unique = True)

# 	def __str__(self):
# 		return self.nfct_channels

# class NFCT_Elements(models.Model):
#     """docstring for NFCT_Elements
# 	Registration of Elements Names"""
#     nfct_elements = models.CharField(max_length = 200, primary_key = True, unique = True)

#     def __str__(self):
#         return self.nfct_elements

# class NFCT_Base_Rate(models.Model):
#     """docstring for NFCT_Base_Rate
# 	Adding of Base Rates"""
#     nfct_unique_key = models.CharField(max_length=100,null=True,blank=True)
#     nfct_baserate = models.IntegerField(null=True,blank=True)
    
#     # def __str__(self):
#     #     return self.nfct_baserate

# durations_choices = (
#     ('days', 'Days'),
#     ('months', 'Months')

# )

# class NFCTDeal(models.Model):
#     """docstring for NFCT_Deal
#     Creating NFCT Deal Form"""
#     # nfct_reference_no = models.IntegerField(primary_key = True, unique = True)
#     ref_nfct_channels_id = models.ForeignKey(NFCT_Channels, on_delete = models.RESTRICT, null = True, blank = True)
#     ref_nfct_elements_id = models.ForeignKey(NFCT_Elements, on_delete = models.RESTRICT)
#     durations = models.CharField(max_length = 6, null = True, blank = True, choices = durations_choices)
#     duration_in = models.IntegerField(null = True, blank = True)
#     effective_rate = models.IntegerField(null = True, blank = True)
#     frequency = models.IntegerField(null = True, blank = True)
#     total_seconds = models.IntegerField(null = True, blank = True)
#     base_rate = models.IntegerField(null = True, blank = True)
#     nfct_total = models.IntegerField(null = True, blank = True)



# def add_reference_no(sender,instance, *args, **kwargs):
#     info = {"count": 0000000000}
#     def number():
#         info["count"] += 1
#         return info["count"]
#     return number
#     nfct_reference_no = number


# pre_save.connect(add_reference_no,sender=NFCTDeal)




