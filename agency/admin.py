from django.contrib import admin

# Register your models here.
from . models import AgencyDetail, AgencyContact

admin.site.register(AgencyDetail)
admin.site.register(AgencyContact)