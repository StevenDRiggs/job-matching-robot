from django.db import models

from .job_location import JobLocation
from .job_requirements import JobRequirements
from .skill import Skill
from .trait import Trait


class Company(models.Model):
    company_name_original = models.CharField()
    company_name_latinized = models.CharField(null=True)

    job_requirements = models.OneToOneField(JobRequirements, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'companies'
