from django.db import models

# Create your models here.
from agency_client.models import *
from nfct.models import *
from deal_fct_nonfct.models import *

CATEGORY_CHOICES = (
    ("Conclave","Conclave"),
    ("Cookery","Cookery"),
    ("Entertainment","Entertainment"),
    ("Fashion","Fashion"),
    ("Health /Life Style","Health /Life Style"),
    ("Infotainment","Infotainment"),
    ("Manch","Manch"),
    ("Politics","Politics"),
    ("Spirituality","Spirituality"),
    ("Sports","Sports"),
    ("Technology","Technology"),
    ("Tourism","Tourism")
)

CHANNEL_CHOICE = (
    ("INN","INN"),
    ("NX","NX"),
    ("IN UP","IN UP"),
    ("MP","MP"),
    ("RAJ","RAJ"),
    ("PUN","PUN"),
    ("HAR","HAR"),
    ("GUJ","GUJ"),
    ("NE NEWS","NE NEWS")
)

class Eventmodel(models.Model):
    deal_id             = models.CharField(max_length = 100, primary_key = True, unique = True)
    executive           = models.CharField(max_length = 100, null=True, blank=True)
    reporting_manager   = models.CharField(max_length = 100, null=True, blank=True)
    event_client_name_ref     = models.ForeignKey(CustomerName,on_delete = models.CASCADE,default = 'default',related_name = 'evt_client')
    event_client_contact_ref  = models.ForeignKey(CustomerContact,on_delete = models.CASCADE,default = 'default')
    event_agency_name_ref     = models.ForeignKey(AgencyDetail,on_delete = models.CASCADE,default = 'default')
    event_agency_contact_ref  = models.ForeignKey(AgencyContact,on_delete = models.CASCADE,default = 'default')
    event_brand_name_ref      = models.ForeignKey(CustomerName,on_delete = models.CASCADE, default = 'default',related_name='evt_brand')
    category            = models.CharField(max_length = 100, choices=CATEGORY_CHOICES)
    description         = models.CharField(max_length = 255,null=True, blank=True)
    channel             = models.CharField(max_length = 50,null=True,blank=True,choices=CHANNEL_CHOICE)
    merit_money         = models.IntegerField(null=True,blank=True)
    fct_seconds         = models.IntegerField(null=True,blank=True)
    fct_total_amt       = models.IntegerField(null=True,blank=True)
    nfct_total_amt      = models.IntegerField(null=True,blank=True)
    grandtotal_amt      = models.IntegerField(null=True,blank=True)
    ro_value            = models.CharField(max_length = 100, null=True, blank=True)
    ro_number           = models.CharField(max_length = 100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.deal_id

class EventFCTModel(models.Model):
    deal_id_fct = models.CharField(max_length=255,primary_key=True,default='default')
    chan = models.CharField(max_length=1000,blank=True,null=True)
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
    base_rate1 = models.IntegerField(blank=True,null=True,default='0')
    base_rate2 = models.IntegerField(blank=True,null=True,default='0')
    base_rate3 = models.IntegerField(blank=True,null=True,default='0')
    prev_yr_fct = models.IntegerField(blank=True,null=True)
    curr_fct = models.IntegerField(blank=True,null=True)



NFCT_CHANNEL_CHOICE = [
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

class Event_NFCT_Base_Rate(models.Model):
    """docstring for NFCT_Base_Rate
	Adding of Base Rates"""
    nfct_unique_key = models.CharField(max_length=100,null=True,blank=True)
    channel = models.CharField(max_length=255,choices=NFCT_CHANNEL_CHOICE)
    element = models.CharField(max_length=255,choices=ELEMENT_CHOICE)
    nfct_baserate = models.IntegerField(null=True,blank=True)

class Event_Deal_Nfct(models.Model):
    
    deal_id_nfct = models.CharField(max_length=255,null=True,blank=True,default='default')
    channel = models.CharField(max_length=255,choices=CHANNEL_CHOICE)
    element = models.CharField(max_length=255,choices=ELEMENT_CHOICE)
    durations = models.CharField(max_length = 6, null = True, blank = True, choices = durations_choices)
    duration_in = models.IntegerField(null = True, blank = True)
    er = models.IntegerField(null=True,blank=True)
    freq = models.IntegerField(null=True,blank=True)
    total_seconds = models.IntegerField(null=True,blank=True)
    base_rate = models.IntegerField(null = True, blank = True)
    total = models.IntegerField(null=True,blank=True)

class NFCTGrandTotal(models.Model):
    dealid_nfct_ref = models.CharField(max_length=100, default='default')
    nfct_grandtotal = models.IntegerField(primary_key=True)