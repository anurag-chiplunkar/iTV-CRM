from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path('final_deal/',views.final_deal),
	path('ajax/load_client_contacts/', views.load_client_contacts, name='load_client_contacts'),
	path('ajax/load_agency_contacts/', views.load_agency_contacts, name='load_agency_contacts'),
]