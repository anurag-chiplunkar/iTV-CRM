from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path('final_deal/',views.final_deal),
]