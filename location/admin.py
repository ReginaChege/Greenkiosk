from django.contrib import admin
from .models import Location

# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'address', 'location_name', 'longitude')
admin.site.register(Location, LocationAdmin)