from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('agency_detail/',views.agency_detail),
    path('agency_contact/',views.agency_contact),
    path('agency_info/',views.agency_info),
    path('agency_contact_info/', views.agency_contact_info),
    
]