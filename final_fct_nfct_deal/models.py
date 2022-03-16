from django.db import models
from agency_client.models import *

from nfct.models import *

from deal_fct_nonfct.models import *


class FinalFctNfctDeal(models.Model):
    """Saves common form of FCT and Nfct
    :deal_id: saves deal id
    :created_at: saves date and time of deal creation
    :executive: saves executive's name
    :reporting_manager: saves reporting manager of current executive
    :RO_number: saves RO number
    :RO_value: saves RO value
    :client_name_ref: saves client name from CustomerName model from agency_client app
    :client_contact_ref: saves client contact wrt client name from CustomerContact model from agency_client app
    :agency_name_ref: saves agency name from AgencyDetail model
	:agency_contact_ref: saves agency contact from AgencyContact model
	:brand_name_ref: saves brand name from CustomerName model
	:fct_total: saves FCT total revenue
    :nfct_total: saves Nfct total revenue
    :grandtotal: saves grandtotal of FCT and Nfct
    
    :CharField: deal_id, executive, reporting_manager, RO_number
    :DecimalField: RO_value, fct_total, nfct_total, grandtotal
    :DateTimeField: created_at
    :ForeignKey: client_name_ref, client_contact_ref, agency_name_ref, agency_contact_ref, brand_name_ref
    :Primary Key: deal_id
    :Unique Key: deal_id"""
    deal_id             = models.CharField(max_length = 100, primary_key = True, unique = True)
    created_at  = models.DateTimeField(auto_now_add = True)
    executive           = models.CharField(max_length= 255)
    reporting_manager   = models.CharField(max_length= 255)
    RO_number           = models.CharField(max_length=255)
    RO_value            = models.DecimalField(max_digits=12, decimal_places=2)
    client_name_ref     = models.ForeignKey(CustomerName,on_delete = models.CASCADE,default = 'default',related_name = 'client')
    client_contact_ref  = models.ForeignKey(CustomerContact,on_delete = models.CASCADE,default = 'default')
    agency_name_ref     = models.ForeignKey(AgencyDetail,on_delete = models.CASCADE,default = 'default')
    agency_contact_ref  = models.ForeignKey(AgencyContact,on_delete = models.CASCADE,default = 'default')
    brand_name_ref      = models.ForeignKey(CustomerName,on_delete = models.CASCADE, default = 'default', related_name = 'brand')
    fct_total           = models.DecimalField(null=True,blank=True,default='0', max_digits=12, decimal_places=2)
    nfct_total          = models.DecimalField(null=True,blank=True,default='0', max_digits=12, decimal_places=2)
    grandtotal          = models.DecimalField(null=True,blank=True, max_digits=12, decimal_places=2)

    def __str__(self):
        return self.deal_id
