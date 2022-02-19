from django.urls import path

from . import views

app_name = 'deal_fct_nonfct'

urlpatterns = [ 
path('', views.home, name="home"),
path('fct_details/', views.fct_details, name="fct_details"),
path('br_details/', views.br_details, name="br_details"),
path('enter_channels/', views.enter_channels, name="enter_channels"),
path('enter_disper/',views.enter_disper,name="enter_disper"),
path('enter_band/',views.enter_band,name="enter_band"),
path('enter_base_rate/',views.enter_base_rate,name="enter_base_rate"),
path('load_br/',views.load_br,name="load_br"),
path('load_br1/',views.load_br1,name="load_br1"),
path('load_br2/',views.load_br2,name="load_br2"),
]