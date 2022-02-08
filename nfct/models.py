from django.db import models

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
