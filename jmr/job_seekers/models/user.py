from django.db import models

from .preferences import Preferences
from .skill import Skill
from .trait import Trait


class User(models.Model):
    full_name_original = models.CharField()
    full_name_latinized = models.CharField(null=True, blank=True)
    sort_by = models.JSONField()

    preferences = models.OneToOneField(Preferences, on_delete=models.CASCADE, null=True, blank=True)
    skills = models.ManyToManyField(Skill, through='SkillLevel')
    traits = models.ManyToManyField(Trait, through='TraitLevel')


    @property
    def name(self):
        return self.full_name_latinized or self.full_name_original

    def __str__(self):
        return self.name
