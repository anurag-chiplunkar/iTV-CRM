from django.contrib import admin
from django.urls import path,include
from . import views
app_name = 'customer'
urlpatterns = [
	path('ctype/',views.ctype),
	path('cname/',views.cname,name='cname'),
	path('ccontact/',views.ccontact,name='ccontact'),
]