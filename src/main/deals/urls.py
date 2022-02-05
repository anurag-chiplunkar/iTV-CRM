from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('register_channel/',views.register_channel),
    path('register_element/',views.register_element),
    path('register_deal/',views.register_deal),
    path('register_base_rate/', views.register_base_rate),
 
]