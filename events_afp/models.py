from django.db import models

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

class ChannelNFCT(models.Model):
	channel = models.CharField(max_length = 100, primary_key = True, unique = True)

	def __str__(self):
		return self.channel


class Events_Category(models.Model):
	"""docstring for Events_Category
	Registation of Categories"""
	category_name = models.CharField(max_length = 100, primary_key = True, unique = True)

	def __str__(self):
		return self.category_name


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

	


class Events_Deal(models.Model):
	"""docstring for Events_Deal
	Registration of Events Deals"""
	ref_category_name = models.ForeignKey(Events_Category, on_delete = models.CASCADE)
	description = models.CharField(max_length = 255)
	ref_channels = models.ForeignKey(AFP_Channels, on_delete = models.CASCADE)
	
	merit_money = models.CharField(max_length = 200)

class fct_deal(models.Model):
	chan = models.CharField(max_length=255,blank=True,null=True)
	dis = models.CharField(max_length=255,blank=True,null=True)
	band1 = models.CharField(max_length=255,blank=True,null=True)
	band2 = models.CharField(max_length=255,blank=True,null=True)
	band3 = models.CharField(max_length=255,blank=True,null=True)
	fct1 = models.IntegerField(blank=True,null=True)
	fct2 = models.IntegerField(blank=True,null=True)
	fct3 = models.IntegerField(blank=True,null=True)
	eff_rate1 = models.IntegerField(blank=True,null=True)
	eff_rate2 = models.IntegerField(blank=True,null=True)
	eff_rate3 = models.IntegerField(blank=True,null=True)
	rev1 = models.IntegerField(blank=True,null=True)
	rev2 = models.IntegerField(blank=True,null=True)
	rev3 = models.IntegerField(blank=True,null=True)
	total_rev = models.IntegerField()
	prev_yr_fct = models.IntegerField(blank=True,null=True)
	curr_fct = models.IntegerField(blank=True,null=True)


# fct
class Disper(models.Model):
	dis_list = models.CharField(max_length=255,primary_key=True)
	def __str__(self):
		return self.dis_list


	
class Band(models.Model):
	b_list = models.CharField(max_length=255,primary_key=True)
	def __str__(self):
		return self.b_list

class base_rate_table(models.Model):
	unique_key = models.CharField(max_length=100,default="default",null=True,blank=True)
	br = models.IntegerField()
	
	def __str__(self):
		return self.br



# # AFP
class AFP_Base_Rate(models.Model):
	afp_unique_key = models.CharField(max_length=100,null=True,blank=True)
	baserate = models.IntegerField()
	def __str__(self):
		return self.baserate

