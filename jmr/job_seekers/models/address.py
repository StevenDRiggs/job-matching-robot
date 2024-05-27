import googlemaps

from django.conf import settings
from django.db import models
from dotenv import dotenv_values

from .user import User


GMAK = dotenv_values(f'{settings.BASE_DIR}/.env')['GOOGLE_MAPS_API_KEY']
gmaps_client = googlemaps.Client(GMAK)


class Address(models.Model):
    street_address = models.CharField()
    city = models.CharField()
    county = models.CharField(blank=True, null=True)
    state = models.CharField(blank=True, null=True)  # also refers to province, prefecture, etc.
    country = models.CharField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')

    @property
    def gaddr(self):
        return f'''place_id:{gmaps_client.geocode(f'{self.street_address}, {self.city}{f", {self.county}" if self.county else ""}{f", {self.state}" if self.state else ""}, {self.country}')[0]['place_id']}'''

    class Meta:
        verbose_name_plural = 'addresses'

    def __str__(self):
        return f'{self.street_address}, {self.city}, {f"{self.county}, " if self.county else ""}{f"{self.state}, " if self.state else ""}{self.country}'
