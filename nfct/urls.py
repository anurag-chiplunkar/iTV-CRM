from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views

app_name = 'nfct'


urlpatterns = [
               # path('create_deal_model_form/', views.create_deal_model_form, name='create_deal_model_form'),
      path('deal426846list/', DealListView.as_view(), name='deallist'),
      path('nfct_load_br/', views.nfct_load_br, name='nfct_load_br'),
      path('nfct_baserate/', views.nfct_enter_base_rate, name='nfct_enter_base_rate'),
      path('dealnfct/', views.nfct_finaldeal, name='nfct_finaldeal'),
      path('nfctdeallist/', views.nfctfinal, name='nfctfinaldeallist'),
      path('ajax/load_client_contacts/', views.load_client_contacts, name='load_client_contacts'),
      path('ajax/load_agency_contacts/', views.load_agency_contacts, name='load_agency_contacts'),
      path('ajax/load_agency_client/',views.load_agency_client, name='load_agency_client'),

               ]
