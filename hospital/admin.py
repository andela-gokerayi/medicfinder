from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from hospital.models import HospitalDirection


AdminSite.site_header = "Medic Finder"
# Register your models here.
admin.site.register(HospitalDirection)
