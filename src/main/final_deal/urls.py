from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('deal_detail/',views.deal_detail),
    
]