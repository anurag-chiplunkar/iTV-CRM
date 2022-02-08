from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'nfct'
	
urlpatterns = [
    path('nfct/', views.nfct_chname, name = 'nfct_channel')
]