from django.contrib import admin
from django.urls import path,include
from .views import *
from . import views

app_name = 'nfct'
	
 
urlpatterns = [path('create_deal_model_form/', views.create_deal_model_form, name='create_deal_model_form'),
path('deallist/', DealListView.as_view(), name='deallist'),
 path('nfct_load_br/', views.nfct_load_br, name = 'nfct_load_br'),
 path('nfct_baserate/', views.nfct_enter_base_rate, name = 'nfct_enter_base_rate'),
]


# urlpatterns = [
#     path('nfct_channel/', views.nfct_chname, name = 'nfct_channel'),
#     path('nfct_element/', views.nfct_elename, name = 'nfct_element'),
#     path('nfct_baserate/', views.nfct_enter_base_rate, name = 'nfct_enter_base_rate'),
#     path('nfct_deal/', views.nfct_deal_form, name = 'nfct_deal_form'),
#     path('nfct_load_br/', views.nfct_load_br, name = 'nfct_load_br'),
#     # path('nfctformset/', views.nfctformset, name = 'nfctformset'),

    
#     path('add_nfct/', Add_NFCT_Deal.as_view(), name = 'add_nfct'),
#     path('', NFCT_Deal.as_view(), name = 'nfct_list'),

# ]