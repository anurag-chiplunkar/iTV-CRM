from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path('program-names/',views.afp_pname),
	path('channel-names/',views.afp_chname),

	path('category-name/',views.cat_name),
	
	path('enter_disper/',views.enter_disper,name="enter_disper"),
	path('enter_band/',views.enter_band,name="enter_band"),
	path('enter_base_rate/',views.enter_base_rate,name="enter_base_rate"),
	path('load_br/',views.load_br,name="load_br"),
	path('load_br1/',views.load_br1,name="load_br1"),
	path('load_br2/',views.load_br2,name="load_br2"),
	
	path('afp_enter_base_rate/',views.afp_enter_base_rate,name="afp_enter_base_rate"),
	path('afp_load_br/',views.afp_load_br,name="afp_load_br"),
    path('events/', views.events,name='events'),
    path('afp1/', views.afp,name='afp1'),

]