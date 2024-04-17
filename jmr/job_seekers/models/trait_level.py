from django.db import models

from .trait import Trait
from .user import User


class TraitLevel(models.Model):
    trait = models.ForeignKey(Trait, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    level = models.SmallIntegerField()
