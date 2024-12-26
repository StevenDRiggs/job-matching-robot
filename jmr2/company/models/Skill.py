from django.db import models

from .Position import Position


class Skill(models.Model):
    tag = models.CharField(max_length=25)

    @property
    def stub(self):
        return '-'.join(self.tag.strip().lower().replace(r'[^a-z -]', '').split())

    def __str__(self):
        return self.tag

class SkillDetail(models.Model):
    position = models.ForeignKey(Position, models.CASCADE)
    skill = models.ForeignKey(Skill, models.CASCADE)

    level = models.PositiveSmallIntegerField()
    requirement_level = models.CharField(
        choices={
            'required': 'Required',
            'preferred': 'Preferred',
            'bonus': 'Bonus',
        }
    )
