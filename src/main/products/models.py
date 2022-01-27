from django.db import models

# Create your models here.

class Prod(models.Model):

	disp = models.CharField(max_length = 20)

	band = models.CharField(max_length = 20)

	base_rate = models.CharField(max_length = 20)

	eff_rate = models.CharField(max_length = 20)

	other_dispersion = models.CharField(max_length = 20)	

	def __str__(self):
		return self.disp