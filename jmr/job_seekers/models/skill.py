from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=25)
    hard = models.BooleanField()
