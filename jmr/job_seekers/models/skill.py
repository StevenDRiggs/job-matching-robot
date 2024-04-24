from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=25)
    hard = models.BooleanField()


    def __str__(self):
        return f'{self.name} ({"hard" if self.hard else "soft"})'
