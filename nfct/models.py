from django.db import models
from django.db.models.signals import pre_save
from django.forms import ModelForm



# Create your models here.

class NFCT_Channels(models.Model):
	"""docstring for NFCT_Channels
	Registration of Channel Names"""
	nfct_channels = models.CharField(max_length = 200, primary_key = True, unique = True)

	def __str__(self):
		return self.nfct_channels

class NFCT_Elements(models.Model):
    """docstring for NFCT_Elements
	Registration of Elements Names"""
    nfct_elements = models.CharField(max_length = 200, primary_key = True, unique = True)

    def __str__(self):
        return self.nfct_elements

class NFCT_Base_Rate(models.Model):
    """docstring for NFCT_Base_Rate
	Adding of Base Rates"""
    nfct_unique_key = models.CharField(max_length=100,null=True,blank=True)
    nfct_baserate = models.IntegerField(null=True,blank=True)
    
    # def __str__(self):
    #     return self.nfct_baserate

durations_choices = (
    ('days', 'Days'),
    ('months', 'Months')

)

class NFCTDeal(models.Model):
    """docstring for NFCT_Deal
    Creating NFCT Deal Form"""
    # nfct_reference_no = models.IntegerField(primary_key = True, unique = True)
    ref_nfct_channels_id = models.ForeignKey(NFCT_Channels, on_delete = models.RESTRICT, null = True, blank = True)
    ref_nfct_elements_id = models.ForeignKey(NFCT_Elements, on_delete = models.RESTRICT)
    durations = models.CharField(max_length = 6, null = True, blank = True, choices = durations_choices)
    duration_in = models.IntegerField(null = True, blank = True)
    effective_rate = models.IntegerField(null = True, blank = True)
    frequency = models.IntegerField(null = True, blank = True)
    total_seconds = models.IntegerField(null = True, blank = True)
    base_rate = models.IntegerField(null = True, blank = True)
    nfct_total = models.IntegerField(null = True, blank = True)



# def add_reference_no(sender,instance, *args, **kwargs):
#     info = {"count": 0000000000}
#     def number():
#         info["count"] += 1
#         return info["count"]
#     return number
#     nfct_reference_no = number


# pre_save.connect(add_reference_no,sender=NFCTDeal)




