from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Country


@admin.register(Country)
class CountryAdmin(OSMGeoAdmin):
    default_lon = 0  # underscores for readability
    default_lat = 0
    default_zoom = 1
