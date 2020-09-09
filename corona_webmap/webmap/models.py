from django.contrib.gis.db import models
from django.contrib.gis.db.models import PointField
from django.core.validators import MaxValueValidator, MinValueValidator


# Create a Country table for the database

class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


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
    Ominus = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    Oplus = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    Aminus = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    Aplus = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    Bminus = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    Bplus = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    ABminus = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    ABplus = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )


class Healthcare(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    rank = models.IntegerField()
    score = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )


class Smoking(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    male = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    female = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    total = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )


class GDP(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    rank = models.IntegerField()
    gdpPerCapita = models.FloatField()
