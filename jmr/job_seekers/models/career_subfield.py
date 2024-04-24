from django.db import models

from .career_field import CareerField


class CareerSubfield(models.Model):
    name = models.CharField()

    career_field = models.ForeignKey(CareerField, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.career_field})'
