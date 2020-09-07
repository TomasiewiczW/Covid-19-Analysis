from django.db import models
from django.contrib.gis.db.models import PointField


# Create a Country table for the database
class Country(models.Model):
    country_id = models.IntegerField()
    name = models.CharField(max_length=255)
    population = models.IntegerField()
    area = models.FloatField()
    location = PointField()

    @property
    def lat_lng(self):
        return list(getattr(self.location, 'coords', [])[::-1])
