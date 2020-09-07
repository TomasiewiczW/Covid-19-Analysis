from django.db import models
from django.contrib.gis.db.models import PointField


# Create a Country table for the database
class Country(models.Model):
    name = models.CharField(max_length=255)
    population = models.IntegerField()
    area = models.FloatField()
    location = PointField()

    @property
    def lat_lng(self):
        return list(getattr(self.location, 'coords', [])[::-1])

    def __str__(self):
        return self.name

class Confirmed(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    date = models.DateField()
    total = models.IntegerField()

class Deaths(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    date = models.DateField()
    total = models.IntegerField()

class Recovered(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    date = models.DateField()
    total = models.IntegerField()

class Bloodtype(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    Ominus = models.FloatField()
    Oplus = models.FloatField()
    Aminus = models.FloatField()
    Aplus = models.FloatField()
    Bminus = models.FloatField()
    Bplus = models.FloatField()
    ABminus = models.FloatField()
    ABplus = models.FloatField()

class Healthcare(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    rank = models.IntegerField()
    score = models.FloatField()

class Smoking(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    male = models.FloatField()
    female = models.FloatField()
    total = models.FloatField()

class GPD(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    rank = models.IntegerField()
    gpdPerCapita = models.FloatField()