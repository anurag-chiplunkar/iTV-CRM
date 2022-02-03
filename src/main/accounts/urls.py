from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path('emp_registration/',views.emp_registration),
	path('emp_login/',views.emp_login),


]