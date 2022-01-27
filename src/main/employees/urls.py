from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('emp_signup/',views.emp_signup),
    path('emp_login/',views.emp_login),
    
]