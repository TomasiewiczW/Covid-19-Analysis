# Covid-19-Analysis

Just another simple coronavirus mapper app - prepared for Advanced Databases course on AGH.


<img src="https://scontent-waw1-1.xx.fbcdn.net/v/t1.15752-9/119447609_329753258236494_2014040091221266111_n.png?_nc_cat=102&_nc_sid=b96e70&_nc_ohc=pc0CbT1hAg0AX_OaQ-m&_nc_ht=scontent-waw1-1.xx&oh=0dedc1fce6ef41d78be07908e6332f13&oe=5F861452" align:center>

## Overview

Django website showing an interactive map of confirmed cases (based on data pulled from WHO repo).

Interaction allows for:
- selecting a country and displaying more details

Clicking a country triggers an AJAX call to the REST API of our website. This pulls additional data for the selected country and shows its geometry on the map.

## Database Schema
<img src="https://scontent-waw1-1.xx.fbcdn.net/v/t1.15752-9/119089960_789328245155282_2305347574397524466_n.png?_nc_cat=111&_nc_sid=b96e70&_nc_ohc=yX4SdTG05iYAX8qQooN&_nc_ht=scontent-waw1-1.xx&oh=ebfaf96f1717415aa87a049903750ff1&oe=5F8317E2" align:center width="800" height="600">

## Project Requirements

- Anaconda
- Python >3.7
- Django 3
- DRF (Django Rest Framework) + DRF-Gis
- LeafletJS (django-leaflet)
- PostgreSQL
- PostGIS
- GDAL

### 💪 More to come as we develop the project! 💪
