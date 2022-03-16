from django.db import models

# Create your models here.
from agency_client.models import *
# from nfct.models import *
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
    """Model to create tables of Events Common form
    
    :deal_id: Saving Deal id
	:created_at: Saving date and time
	:executive: Executive Name from accounts app
	:reporting_manager: Reporting Manager from accounts app
	:ro_number: Release Order Number
	:ro_value: Realease Order Value
	:event_client_name_ref: Client Name reference from agency_client app
	:event_client_contact_ref: Client Contact details reference from agency_client app
	:event_agency_name_ref: Agency Name Reference from agency_client app
	:event_agency_contact_ref: Agency Contact details reference from agency_client app
	:event_brand_name_ref: Brand Name reference from agency_client app
    :category: Category Name
    :description: Description
    :channel: Channel
    :merit_money: Merit Money
    :fct_seconds: FCT Seconds form FCT model
    :fct_total_amt: FCT Total Amount form FCT model
    :nfct_total_amt: NFCt Total from NFCT model
    :grandtotal_amt: Grand Total of FCT, NFCT and Merit Money
	
	:CharField: deal_id, executive, reporting_manager, ro_number, category, description, channel, 
	:DateTimeField: created_at
	:ForiegnKey: event_client_name_ref, event_client_contact_ref, event_agency_name_ref, event_agency_contact_ref, event_brand_name_ref
	:DecimalField: merit_money, fct_total_amt, nfct_total_amt, grandtotal_amt, ro_value
    :IntegerField: fct_seconds
    
    """
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
    merit_money         = models.DecimalField(null=True,blank=True,max_digits=12,decimal_places=2)
    fct_seconds         = models.IntegerField(null=True,blank=True)
    fct_total_amt       = models.DecimalField(null=True,blank=True,max_digits=12,decimal_places=2)
    nfct_total_amt      = models.DecimalField(null=True,blank=True,max_digits=12,decimal_places=2)
    grandtotal_amt      = models.DecimalField(null=True,blank=True,max_digits=12,decimal_places=2)
    ro_value            = models.DecimalField(null=True,blank=True,max_digits=12,decimal_places=2)
    ro_number           = models.CharField(max_length = 100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.deal_id

class EventFCTModel(models.Model):
    """Model for Event FCT
	
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
    deal_id_fct = models.CharField(max_length=255,primary_key=True,default='default')
    chan = models.CharField(max_length=1000,blank=True,null=True)
    dis = models.CharField(max_length=1000,blank=True,null=True)
    band1 = models.CharField(max_length=1000,blank=True,null=True)
    band2 = models.CharField(max_length=1000,blank=True,null=True)
    band3 = models.CharField(max_length=1000,blank=True,null=True)
    fct1 = models.IntegerField(blank=True,null=True,default=0)
    fct2 = models.IntegerField(blank=True,null=True,default=0)
    fct3 = models.IntegerField(blank=True,null=True,default=0)
    eff_rate1 = models.DecimalField(null=True,blank=True,max_digits=12,decimal_places=2,default='0')
    eff_rate2 = models.DecimalField(null=True,blank=True,max_digits=12,decimal_places=2,default='0')
    eff_rate3 = models.DecimalField(null=True,blank=True,max_digits=12,decimal_places=2,default='0')
    rev1 = models.DecimalField(null=True,blank=True,max_digits=12,decimal_places=2,default='0')
    rev2 = models.DecimalField(null=True,blank=True,max_digits=12,decimal_places=2,default='0')
    rev3 = models.DecimalField(null=True,blank=True,max_digits=12,decimal_places=2,default='0')
    total_rev = models.DecimalField(null=True,blank=True,max_digits=12,decimal_places=2,default='0')
    base_rate1 = models.IntegerField(blank=True,null=True,default=0)
    base_rate2 = models.IntegerField(blank=True,null=True,default=0)
    base_rate3 = models.IntegerField(blank=True,null=True,default=0)
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
    """Model for Event NFCT
	
	:deal_id_fct: Deal id of form
	:channel: Channel Names
	:element: Element
	:durations: Duration(Days, Months)
	:duration_in: Duration in number wrt duration selected (Days or Months)
	:er: Effective rate values
	:freq: Frequency values
	:total_seconds: Total Seconds 
	:base_rate: Base Rate
	:total: Total of single form

	:CharField: dealid_fct, channel, element, durations
	:IntegerField: total_seconds, duration_in, freq, base_rate
	:DecimalField: er, total"""

    deal_id_nfct = models.CharField(max_length=255,null=True,blank=True,default='default')
    channel = models.CharField(max_length=255,choices=CHANNEL_CHOICE)
    element = models.CharField(max_length=255,choices=ELEMENT_CHOICE)
    durations = models.CharField(max_length = 6, null = True, blank = True, choices = durations_choices)
    duration_in = models.IntegerField(null = True, blank = True)
    er = models.DecimalField(null=True,blank=True,max_digits=12,decimal_places=2,default='0')
    freq = models.IntegerField(null=True,blank=True)
    total_seconds = models.IntegerField(null=True,blank=True)
    base_rate = models.IntegerField(null = True, blank = True)
    total = models.DecimalField(null=True,blank=True,max_digits=12,decimal_places=2,default='0')

class EventNFCTGrandTotal(models.Model):
    """Model for saving NFCT Grand total
    :dealid_nfct_ref: Deal id of form
    :nfct_grandtotal: NFCt Grand Total

    :CharField: dealid_nfct_ref
    :DecimalField: nfct_grandtotal"""
    
    dealid_nfct_ref = models.CharField(max_length=100, default='default')
    nfct_grandtotal = models.DecimalField(primary_key=True,max_digits=12,decimal_places=2,default='0')
