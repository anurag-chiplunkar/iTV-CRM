from django.contrib import admin
from django.urls import path,include
from .views import *

app_name = 'nfct'
	
urlpatterns = [
    path('nfct_channel/', nfct_chname, name = 'nfct_channel'),
    path('nfct_element/', nfct_elename, name = 'nfct_element'),
    path('nfct_baserate/', nfct_enter_base_rate, name = 'nfct_enter_base_rate'),
    path('nfct_deal/', nfct_deal_form, name = 'nfct_deal_form'),
    path('nfct_load_br/', nfct_load_br, name = 'nfct_load_br'),
    path('nfctformset/', nfctformset, name = 'nfctformset'),

    
    path('add_nfct/', Add_NFCT_Deal.as_view(), name = 'add_nfct'),
    path('', NFCT_Deal.as_view(), name = 'nfct_list'),

]