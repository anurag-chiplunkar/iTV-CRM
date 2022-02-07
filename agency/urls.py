from django.contrib import admin
from django.urls import path,include
from . import views

##this app_name is given because we have defined the namespace for agency app
app_name = 'agency'

urlpatterns = [

    path('agency_detail/',views.agency_detail, name = 'agency_detail'),
    path('agency_contact/',views.agency_contact, name = 'agency_contact'),
    path('agency_info/',views.agency_info),
    path('agency_contact_info/', views.agency_contact_info),
    
]