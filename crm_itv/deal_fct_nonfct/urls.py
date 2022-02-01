from django.urls import path

from . import views

urlpatterns = [ 
path('', views.home, name="home"),
path('fct_details/', views.fct_details, name="fct_details"),
path('br_details/', views.br_details, name="br_details"),
]