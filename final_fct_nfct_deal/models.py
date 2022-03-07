from django.db import models
from agency_client.models import *

from nfct.models import *

from deal_fct_nonfct.models import *


class FinalFctNfctDeal(models.Model):
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
