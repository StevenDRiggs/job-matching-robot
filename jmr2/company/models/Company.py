from django.db import models


class Company(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'companies'
