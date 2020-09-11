from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.gis.geos import Point


class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the world borders shapefile.

    name = models.CharField(max_length=50, primary_key=True)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005', default="")
    fips = models.CharField('FIPS Code', max_length=2,  null=True)
    iso2 = models.CharField('2 Digit ISO', max_length=2, default="")
    iso3 = models.CharField('3 Digit ISO', max_length=3, default="")
    un = models.IntegerField('United Nations Code', default="")
    region = models.IntegerField('Region Code', default="")
    subregion = models.IntegerField('Sub-Region Code', default="")
    lon = models.FloatField(default="")
    lat = models.FloatField(default="")

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField(default="")

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


class Confirmed(models.Model):

    date = models.CharField(max_length=15)
    total = models.IntegerField()
    country = models.ForeignKey(WorldBorder, default="", on_delete=models.CASCADE, blank=True, null=True)

class Deaths(models.Model):

    date = models.CharField(max_length=15)
    total = models.IntegerField()
    country = models.ForeignKey(WorldBorder, default="", on_delete=models.CASCADE, blank=True, null=True)

class Recovered(models.Model):
    date = models.CharField(max_length=15)
    total = models.IntegerField()
    country = models.ForeignKey(WorldBorder, default="", on_delete=models.CASCADE, blank=True, null=True)

class Bloodtype(models.Model):
    Ominus = models.CharField(max_length=10)
    Oplus = models.CharField(max_length=10)
    Aminus = models.CharField(max_length=10)
    Aplus = models.CharField(max_length=10)
    Bminus = models.CharField(max_length=10)
    Bplus = models.CharField(max_length=10)
    ABminus = models.CharField(max_length=10)
    ABplus = models.CharField(max_length=10)
    country = models.ForeignKey(WorldBorder, default="", on_delete=models.CASCADE, blank=True, null=True)


class Healthcare(models.Model):
    rank = models.IntegerField()
    score = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    country = models.ForeignKey(WorldBorder, default="", on_delete=models.CASCADE, blank=True, null=True)


class Smoking(models.Model):
    male = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    female = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    total = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    country = models.ForeignKey(WorldBorder, default="", on_delete=models.CASCADE, blank=True, null=True)


class GDP(models.Model):
    rank = models.IntegerField()
    gdpPerCapita = models.FloatField()
    country = models.ForeignKey(WorldBorder, default="", on_delete=models.CASCADE, blank=True, null=True)
