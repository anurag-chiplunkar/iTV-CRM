from django.db import models

# Create your models here.


class ElementNFCT(models.Model):
	element = models.CharField(max_length = 100, primary_key = True, unique = True)

	def __str__(self):
		return self.element

class BaseRateNFCT(models.Model):
	unique_key	= models.CharField(max_length = 100, primary_key = True,unique = True,default = 'default')
	base_rate	= models.IntegerField()

	def __str__(self):
		return self.base_rate


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
	afp_pri_key = models.CharField(max_length = 20, primary_key = True, unique = True)
	ref_program_name = models.ForeignKey(AFP_ProgramName, on_delete = models.CASCADE)
	ref_channels = models.ForeignKey(AFP_Channels, on_delete = models.CASCADE)
	promos = models.CharField(max_length = 20, choices = promos_choices, blank = True, null = True)
	slot = models.CharField(max_length = 20, choices = slot_choices, blank = True, null = True)
	eff_rate = models.CharField(max_length = 200)

	


class Events_Deal(models.Model):
	"""docstring for Events_Deal
	Registration of Events Deals"""
	event_pri_key = models.CharField(max_length = 20, primary_key = True, unique = True)
	ref_category_name = models.ForeignKey(Events_Category, on_delete = models.CASCADE)
	description = models.CharField(max_length = 500)
	ref_channels = models.ForeignKey(AFP_Channels, on_delete = models.CASCADE)
	
	merit_money = models.CharField(max_length = 200)

class fct_deal(models.Model):
	fct_pri_key = models.CharField(max_length = 1000, primary_key = True, unique = True)
	chan = models.CharField(max_length=1000,blank=True,null=True)
	dis = models.CharField(max_length=1000,blank=True,null=True)
	band1 = models.CharField(max_length=1000,blank=True,null=True)
	band2 = models.CharField(max_length=1000,blank=True,null=True)
	band3 = models.CharField(max_length=1000,blank=True,null=True)
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
	# total_fct = models.IntegerField()
	prev_yr_fct = models.IntegerField(blank=True,null=True)
	curr_fct = models.IntegerField(blank=True,null=True)

class DealNFCT(models.Model):
	nonfct_pri_key = models.CharField(max_length = 100, primary_key = True, unique = True)
	seconds		= models.IntegerField(null = True, blank = True)
	days		= models.IntegerField(null = True, blank = True)
	months		= models.IntegerField(null = True, blank = True)
	eff_rate 	= models.IntegerField()
	frequency 	= models.IntegerField()
	total_sec 	= models.IntegerField()
	total_cost 	= models.IntegerField()

	channel_nfct 	= models.ForeignKey(ChannelNFCT,on_delete = models.CASCADE,default = 'default')
	element_nfct 	= models.ForeignKey(ElementNFCT,on_delete = models.CASCADE,default = 'default')
	baserate_nfct 	= models.ForeignKey(BaseRateNFCT,on_delete = models.CASCADE,default = 'default')


class FinalDeal(models.Model):
	"""doc string to create final deal"""
	reference_no = models.CharField(max_length =100, primary_key = True, unique = True)

	ref_event_pri_key = models.ForeignKey(Events_Deal, on_delete = models.RESTRICT)
	ref_fct_pri_key = models.ForeignKey(fct_deal, on_delete = models.RESTRICT)
	ref_nonfct_pri_key = models.ForeignKey(DealNFCT, on_delete = models.RESTRICT)
	ref_afp_pri_key = models.ForeignKey(AFP_Deal, on_delete = models.RESTRICT)
	
	

# fct
class Disper(models.Model):
	dis_list = models.CharField(max_length=1000,primary_key=True)
	def __str__(self):
		return self.dis_list
	# ref_c_list = models.ForeignKey(Channel,on_delete=models.PROTECT,blank=True)


	
class Band(models.Model):
	b_list = models.CharField(max_length=1000,primary_key=True)
	def __str__(self):
		return self.b_list

class base_rate_table(models.Model):
	unique_key = models.CharField(max_length=100,default="default",null=True,blank=True)
	br = models.IntegerField()
	# ref_c_list = models.ForeignKey(Channel,on_delete=models.PROTECT,blank=True,null=True)
	# ref_b_list = models.ForeignKey(Band,on_delete=models.PROTECT,blank=True,null=True)

	def __str__(self):
		return self.br



# # AFP
class AFP_Base_Rate(models.Model):
	afp_unique_key = models.CharField(max_length=100,null=True,blank=True)
	baserate = models.IntegerField()
	def __str__(self):
		return self.baserate

