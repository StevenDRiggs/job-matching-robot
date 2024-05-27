import googlemaps

from django.conf import settings
from django.db import models
from dotenv import dotenv_values


GMAK = dotenv_values(f'{settings.BASE_DIR}/.env')['GOOGLE_MAPS_API_KEY']
gmaps_client = googlemaps.Client(GMAK)


class JobLocation(models.Model):
    city = models.CharField()
    county = models.CharField(null=True)
    state = models.CharField(null=True)  # also refers to province, prefecture, etc.
    country = models.CharField()

    @property
    def gaddr(self):
        return f'''place_id:{gmaps_client.geocode(f'{self.city}{f", {self.county}" if self.county else ""}{f", {self.state}" if self.state else ""}, {self.country}')[0]['place_id']}'''
