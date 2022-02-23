from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path('final_deal/',views.final_deal),
	path('ajax/load_client_contacts/', views.load_client_contacts, name='load_client_contacts'),
	path('ajax/load_agency_contacts/', views.load_agency_contacts, name='load_agency_contacts'),
	path('final_load_br/',views.final_load_br,name="final_load_br"),
	path('final_load_br1/',views.final_load_br1,name="final_load_br1"),
	path('final_load_br2/',views.final_load_br2,name="final_load_br2"),
	path('/final_deallist',views.finalDealListView, name = 'final_deallist'),
]