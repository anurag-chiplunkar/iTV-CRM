from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'afp_deal'

urlpatterns = [
    path('afp_program_name/',views.afp_program_name),
    path('afp_channel_name/',views.afp_channel_name),
    path('afp_promo_name/',views.afp_promo_name),
    path('afp_slot_name/',views.afp_slot_name),
    path('afp_baserates/',views.afp_br),
    path('afp_deal_load_br/',views.afp_deal_load_br, name = 'afp_deal_load_br'),
    path('create_afp_deal/', views.create_afp_deal, name='create_afp_deal'),
    path('afp_final_deallist/', views.AFPDealListView, name='afp_final_deallist'),
    path('ajax/load_afp_client_contacts/',views.load_afp_client_contacts, name='load_afp_client_contacts'),
    path('ajax/load_afp_agency_contacts/',views.load_afp_agency_contacts, name='load_afp_agency_contacts'),
    path('ajax/load_afp_agency_client/',views.load_afp_agency_client, name='load_afp_agency_client'),

]