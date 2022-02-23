from django.contrib import admin
from django.urls import path,include
from . import views

##this app_name is given because we have defined the namespace for agency app
app_name = 'agency_client'

urlpatterns = [

    path('agency_detail_1/',views.agency_detail, name = 'agency_detail'),
    path('agency_contact_1/',views.agency_contact, name = 'agency_contact'),
    path('ctype_1/',views.ctype),
	path('cname_1/',views.cname,name='cname'),
	path('ccontact_1/',views.ccontact,name='ccontact'),
    
]
