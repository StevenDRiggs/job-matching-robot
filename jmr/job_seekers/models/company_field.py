from django.db import models


class CompanyField(models.Model):
    name = models.CharField()
