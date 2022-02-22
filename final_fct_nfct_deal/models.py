from django.db import models

class FinalFctNfctDeal(models.Model):
    deal_id             = models.CharField(max_length = 10, primary_key = True, unique = True)
    client_name_ref     = models.ForeignKey(CustomerName,on_delete = models.CASCADE,default = 'default')
    client_contact_ref  = models.ForeignKey(CustomerContact,on_delete = models.CASCADE,default = 'default')
    agency_name_ref     = models.ForeignKey(AgencyDetail,on_delete = models.CASCADE,default = 'default')
    agency_contact_ref  = models.ForeignKey(AgencyContact,on_delete = models.CASCADE,default = 'default')
    brand_name_ref      = models.ForeignKey(CustomerName,on_delete = models.CASCADE, default = 'default')
    fct_total           = models.IntegerField()
    nfct_total          = models.IntegerField()
    grandtotal          = models.IntegerField()

    def __str__(self):
        return self.deal_id
