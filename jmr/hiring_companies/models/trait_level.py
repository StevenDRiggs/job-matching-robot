from django.db import models

from .job_requirements import JobRequirements
from .trait import Trait


class TraitLevel(models.Model):
    job_requirement = models.ForeignKey(JobRequirements, on_delete=models.CASCADE)
    trait = models.ForeignKey(Trait, on_delete=models.CASCADE, related_name='desired_traits')

    level = models.SmallIntegerField()
    required = models.BooleanField(default=False)

