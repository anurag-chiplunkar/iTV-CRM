from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path('final_deal/',views.final_deal),
	path('load_br/',views.load_br,name="load_br"),
]