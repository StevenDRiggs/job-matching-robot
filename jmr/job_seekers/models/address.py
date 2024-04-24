from django.db import models

from .user import User


class Address(models.Model):
    street_address = models.CharField()
    city = models.CharField()
    county = models.CharField(blank=True, null=True)
    state = models.CharField(blank=True, null=True)  # also refers to province, prefecture, etc.
    country = models.CharField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')

    class Meta:
        verbose_name_plural = 'addresses'

    def __str__(self):
        return f'{self.street_address}, {self.city}, {f"{self.county}, " if self.county else ""}{f"{self.state}, " if self.state else ""}{self.country}'
