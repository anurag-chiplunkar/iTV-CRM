from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'accounts'

urlpatterns = [
	path('emp_registration/',views.emp_registration, name = 'emp_registration'),
	path('emp_login/',views.emp_login, name = 'emp_login'),


]