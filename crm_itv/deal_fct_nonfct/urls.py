from django.urls import path

from . import views

urlpatterns = [ 
path('', views.home, name="home"),
path('fct_details/', views.fct_details, name="fct_details"),
path('br_details/', views.br_details, name="br_details"),
path('enter_channels/', views.enter_channels, name="enter_channels"),
path('enter_disper/',views.enter_disper,name="enter_disper"),
path('enter_band/',views.enter_band,name="enter_band"),
path('enter_base_rate/',views.enter_base_rate,name="enter_base_rate"),
]