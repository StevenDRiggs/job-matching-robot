from django.db import models
from djmoney.models.fields import MoneyField


class Company(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'companies'

class Position(models.Model):
    company = models.ForeignKey(Company, models.CASCADE)

    title = models.CharField()
    description = models.TextField()
    location = models.JSONField(default=dict) # includes address, remote, hybrid
    relocation_assistance = models.JSONField(default=dict)
    position_type = models.CharField(
        max_length=3,
        choices={
            'fth': 'Full-time',
            'pth': 'Part-time',
            'sal': 'Salary',
            'con': 'Contract',
            'c2h': 'Contract-to-hire',
            'sea': 'Seasonal',
            'oth': 'Other',
        }
    )
    pay = MoneyField(
        max_digits=19,
        decimal_places=2,
    )
    pay_timing = models.CharField(
        max_length = 1,
        choices = {
            'h': 'per hour',
            'w': 'per week',
            'b': 'every two weeks',
            'm': 'per month',
            'q': 'every three months',
            'y': 'per year',
        }
    )
    hours = models.JSONField(default=dict)

    benefits = models.ManyToManyField('Benefit', through='BenefitAvailable')

    tasks = models.ManyToManyField('Task')

    skills = models.ManyToManyField('Skill', through='SkillDetail')

    traits = models.ManyToManyField('Trait', through='TraitDetail')

    def __str__(self):
        return f'{self.title} ({self.company})'

class Benefit(models.Model):
    tag = models.CharField()
    description = models.TextField()

    @property
    def stub(self):
        return '-'.join(self.tag.strip().lower().replace(r'[^a-z -]', '').split())

class BenefitAvailable(models.Model):
    position = models.ForeignKey(Position, models.CASCADE)
    benefit = models.ForeignKey(Benefit, models.CASCADE)

    available = models.DurationField()

class Task(models.Model):
    tag = models.CharField()
    description = models.TextField()

    @property
    def stub(self):
        return '-'.join(self.tag.strip().lower().replace(r'[^a-z -]', '').split())

    def __str__(self):
        return self.tag

class Skill(models.Model):
    tag = models.CharField(max_length=25)

    @property
    def stub(self):
        return self.tag.strip().lower().replace(r'\s+', '-')

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

class Trait(models.Model):
    tag = models.CharField(max_length=25)

    @property
    def stub(self):
        return self.tag.strip().lower().replace(r'\s+', '-')

    def __str__(self):
        return self.tag

class TraitDetail(models.Model):
    position = models.ForeignKey(Position, models.CASCADE)
    trait = models.ForeignKey(Trait, models.CASCADE)

    level = models.PositiveSmallIntegerField()
    requirement_level = models.CharField(
        choices={
            'required': 'Required',
            'preferred': 'Preferred',
            'bonus': 'Bonus',
        }
    )
