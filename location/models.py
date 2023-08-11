from django.db import models

# Create your models here.
class Location(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    location_name = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)