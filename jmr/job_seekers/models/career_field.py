from django.db import models


class CareerField(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name
