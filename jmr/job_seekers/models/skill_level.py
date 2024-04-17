from django.db import models

from .skill import Skill
from .user import User


class SkillLevel(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    level = models.SmallIntegerField()
