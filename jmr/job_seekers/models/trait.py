from django.db import models


class Trait(models.Model):
    name = models.CharField()


    def __str__(self):
        return self.name
