from django.db import models


class Company(models.Model):
    name = models.CharField()

class Position(models.Model):
    company = models.ForeignKey(Company, models.CASCADE)

    title = models.CharField()
    description = models.TextField()

    required_skills = models.ManyToManyField('Skill', related_name='required_by')
    preferred_skills = models.ManyToManyField('Skill', related_name='preferred_by')
    bonus_skills = models.ManyToManyField('Skill', related_name='bonus_for')



