from django.db import models

from .skill import Skill
from .trait import Trait


class User(models.Model):
    full_name_original = models.CharField()
    full_name_latinized = models.CharField(null=True)
    sort_by = models.JSONField()

    skills = models.ManyToManyField(Skill)
    traits = models.ManyToManyField(Trait)
