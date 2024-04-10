from django.db import models

from .career_field import CareerField


class Preferences(models.Model):
    remote = models.BooleanField(default=False)
    relocate = models.BooleanField(default=False)
    relocation_distance = models.SmallIntegerField(null=True)
    distance_measurement = models.CharField(max_length=2, choices={'mi': 'mi', 'km': 'km'}, null=True)
    relocation_assistance_needed = models.BooleanField(default=False)
    relocation_assistance_amount = models.DecimalField(max_digits=10, decimal_places=2,  default=0.00)

    preferred_career_fields = models.ManyToManyField(CareerField, related_name='preferred_by')
    non_preferred_career_fields = models.ManyToManyField(CareerField, related_name='non_preferred_by')
