from django.db import models


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

    tasks = models.ManyToManyField('Task')

    skills = models.ManyToManyField('Skill', through='SkillDetail')

    traits = models.ManyToManyField('Trait', through='TraitDetail')

    def __str__(self):
        return f'{self.title} ({self.company})'

class Task(models.Model):
    tag = models.CharField()

    @property
    def stub(self):
        return '-'.join(self.tag.strip().lower().replace(r'[^a-z -]', '').split()[:5])

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
