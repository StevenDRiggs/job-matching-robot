from django.db import models


class JobLocation(models.Model):
    city = models.CharField()
    county = models.CharField(null=True)
    state = models.CharField(null=True)  # also refers to province, prefecture, etc.
    country = models.CharField()
