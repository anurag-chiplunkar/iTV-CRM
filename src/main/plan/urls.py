from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('plan_detail/',views.plan_detail),
]