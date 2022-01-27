from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('item_detail/',views.item_detail),
    path('subitem_detail/',views.subitem_detail),
    
]