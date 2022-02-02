from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path('program-names/',views.afp_pname),
	path('channel-names/',views.afp_chname),
	path('afp-deal/',views.afp_deal),
	path('category-name/',views.cat_name),
	# path('event-deal/',views.event_deal),

]