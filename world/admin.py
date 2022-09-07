from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from world.models import World


@admin.register(World)
class WorldAdmin(OSMGeoAdmin):
    list_display = ('name', 'pop2005', 'fips',)
    list_filter = ('name', 'pop2005', 'fips',)
    search_fields = ('name', 'fips', 'pop2005',)
    list_per_page = 20
