from django.db import models
from agency_client.models import *
from nfct.forms import *
from nfct.models import *
from deal_fct_nonfct.forms import *
from deal_fct_nonfct.models import *


class FinalFctNfctDeal(models.Model):
    deal_id             = models.CharField(max_length = 100, primary_key = True, unique = True)
    client_name_ref     = models.ForeignKey(CustomerName,on_delete = models.CASCADE,default = 'default',related_name = 'client')
    client_contact_ref  = models.ForeignKey(CustomerContact,on_delete = models.CASCADE,default = 'default')
    agency_name_ref     = models.ForeignKey(AgencyDetail,on_delete = models.CASCADE,default = 'default')
    agency_contact_ref  = models.ForeignKey(AgencyContact,on_delete = models.CASCADE,default = 'default')
    brand_name_ref      = models.ForeignKey(CustomerName,on_delete = models.CASCADE, default = 'default', related_name = 'brand')
    fct_total           = models.IntegerField(null=True,blank=True)
    nfct_total          = models.IntegerField(null=True,blank=True)
    grandtotal          = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.deal_id
