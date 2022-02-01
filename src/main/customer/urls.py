from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path('ctype/',views.ctype),
	path('cname/',views.cname),
	path('ccontact/',views.ccontact),
]