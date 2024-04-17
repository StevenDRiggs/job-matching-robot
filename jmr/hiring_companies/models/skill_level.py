from django.db import models

from .job_requirements import JobRequirements
from .skill import Skill


class SkillLevel(models.Model):
    job_requirement = models.ForeignKey(JobRequirements, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='desired_skills')

    level = models.SmallIntegerField()
    required = models.BooleanField(default=False)
