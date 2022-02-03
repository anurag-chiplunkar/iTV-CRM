from django.contrib import admin
from django.urls import path,include
from . import views

# app_name = 'profiles'

urlpatterns = [
	path('profile/',views.profile, name = 'profile'),
]