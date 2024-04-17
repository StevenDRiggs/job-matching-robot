from django.db import models

from .address import Address
from .preferences import Preferences
from .skill import Skill
from .trait import Trait


class User(models.Model):
    full_name_original = models.CharField()
    full_name_latinized = models.CharField(null=True)
    sort_by = models.JSONField()

    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    preferences = models.OneToOneField(Preferences, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill, through='SkillLevel')
    traits = models.ManyToManyField(Trait, through='TraitLevel')
