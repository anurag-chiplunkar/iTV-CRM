from django.db import models

# Create your models here.
class AFP_ProgramName(models.Model):
	"""docstring for AFP_ProgramName
	Registration of Program Names"""
	program_name = models.CharField(max_length = 100, primary_key = True, unique = True)

	def __str__(self):
		return self.program_name


class AFP_Channels(models.Model):
	"""docstring for AFP_Channels
	Registration of Channel Names"""
	channels = models.CharField(max_length = 200, primary_key = True, unique = True)

	def __str__(self):
		return self.channels

promos_choices = (
    ("10", "10"),
    ("20", "20"),
    ("30", "30"),
)

slot_choices = (
	("10", "10"),
    ("22", "22"),
)

class AFP_Deal(models.Model):
	"""docstring for AFP_Deal
	Registration of AFP Deals"""
	ref_program_name = models.ForeignKey(AFP_ProgramName, on_delete = models.CASCADE)
	ref_channels = models.ForeignKey(AFP_Channels, on_delete = models.CASCADE)
	promos = models.CharField(max_length = 20, choices = promos_choices, blank = True, null = True)
	slot = models.CharField(max_length = 20, choices = slot_choices, blank = True, null = True)
	eff_rate = models.CharField(max_length = 200)

	# total = models.CharField(max_length = 200)
		
	# def __str__(self):
	# 	return self.ref_channels


class Events_Category(models.Model):
	"""docstring for Events_Category
	Registation of Categories"""
	category_name = models.CharField(max_length = 100, primary_key = True, unique = True)

	def __str__(self):
		return self.category_name


class Events_Deal(models.Model):
	"""docstring for Events_Deal
	Registration of Events Deals"""
	ref_category_name = models.ForeignKey(Events_Category, on_delete = models.CASCADE)
	description = models.CharField(max_length = 500)
	ref_channels = models.ForeignKey(AFP_Channels, on_delete = models.CASCADE)
	amount = models.CharField(max_length = 200)
	merit_money = models.CharField(max_length = 200)

	
