from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from hospital.models import HospitalDirection, PointOfInterest, Comment


AdminSite.site_header = "Medic Finder"
# Register your models here.
admin.site.register(HospitalDirection)
admin.site.register(PointOfInterest)
admin.site.register(Comment)
