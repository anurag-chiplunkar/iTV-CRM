from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path('register_cust_custcontact/',views.customer_registration),
    # path('contact_form/',views.contact_form),
    # path('customer_name/',views.customer_name),
    # path('customer_type/',views.customer_type),
    # path('customer_contact/',views.customer_contact),
    path('cust_info/',views.cust_info),
    path('cust_contact_info/',views.cust_contact_info),
    path('cust_type_info/',views.cust_type_info),
    
]