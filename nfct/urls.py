from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'nfct'
	
urlpatterns = [
    path('nfct_channel/', views.nfct_chname, name = 'nfct_channel'),
    path('nfct_element/', views.nfct_elename, name = 'nfct_element')
]