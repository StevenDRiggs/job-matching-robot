from django.db import models
from djmoney.models.fields import MoneyField


class Company(models.Model):
    name = models.CharField()

    def __str__(self):
        return f'{self.name} ({self.positions.count()} position{'' if self.positions.count() == 1 else 's'})'

    class Meta:
        verbose_name_plural = 'companies'

class Position(models.Model):
    company = models.ForeignKey(Company, models.CASCADE, related_name='positions')

    title = models.CharField()
    description = models.TextField()
    location = models.JSONField(default=dict) # includes address, remote, hybrid
    def get_location(self):
        output = ''
        loc = self.location
        if loc.get('remote'):
            output += 'Remote'
            if loc.get('hybrid') or loc.get('address'):
                output += '; '
        if loc.get('hybrid'):
            output += 'Hybrid'
            if loc.get('address'):
                output += '; '
        if loc.get('address'):
            output += loc['address']
        return output

    relocation_assistance = models.JSONField(default=dict)
    def get_relocation_assistance(self):
        ra = self.relocation_assistance
        if not ra.get('available'):
            return 'Not available'
        else:
            output = f'{ra.get('amount')}'
            if ra.get('notes'):
                output += f' ({ra['notes']})'
            return output

    position_type_dict = {
        'fth': 'Full-time',
        'pth': 'Part-time',
        'sal': 'Salary',
        'con': 'Contract',
        'c2h': 'Contract-to-hire',
        'sea': 'Seasonal',
        'oth': 'Other',
    }
    position_type = models.CharField(
        max_length=3,
        choices=position_type_dict,
    )
    def get_position_type(self):
        return self.position_type_dict[self.position_type]

    pay = MoneyField(
        max_digits=19,
        decimal_places=2,
    )
    pay_frequency_dict = {
        'h': 'per hour',
        'w': 'per week',
        'b': 'every two weeks',
        'm': 'per month',
        'q': 'every three months',
        'y': 'per year',
        'e': 'per event',
        'o': 'per other (see description)',
    }
    pay_frequency = models.CharField(
        max_length = 1,
        choices = pay_frequency_dict,
    )
    def get_pay_frequency(self):
        return self.pay_frequency_dict[self.pay_frequency]

    hours = models.JSONField(default=dict)
    def get_hours(self):
        h = self.hours
        output = ''
        days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        flex = h.get('flexible')
        wt = h.get('weekly_total')
        core = any([h.get(day) for day in days])
        if flex:
            output += 'Flexible'
            if wt or core:
                output += '; '
        if wt:
            output += f'{h['weekly_total']} total hours per week'
            if core:
                output += '; '
        if (flex or wt) and core:
            output += 'Required Core Hours: '
        for day in days:
            if h.get(day):
                output += f'{day} {h[day]}; '
        if output[-2:] == '; ':
            output = output[:-2]
        return output

    benefits = models.ManyToManyField('Benefit', through='BenefitAvailable')

    tasks = models.ManyToManyField('Task')

    skills = models.ManyToManyField('Skill', through='SkillDetail')
    def get_required_skills(self):
        return [(skill, skill.skilldetail_set.filter(position=self).first().level) for skill in self.skills.filter(skilldetail__requirement_level='required')]
    def get_preferred_skills(self):
        return [(skill, skill.skilldetail_set.filter(position=self).first().level) for skill in self.skills.filter(skilldetail__requirement_level='preferred')]
    def get_bonus_skills(self):
        return [(skill, skill.skilldetail_set.filter(position=self).first().level) for skill in self.skills.filter(skilldetail__requirement_level='bonus')]

    traits = models.ManyToManyField('Trait', through='TraitDetail')
    def get_required_traits(self):
        return [(trait, trait.traitdetail_set.filter(position=self).first().level) for trait in self.traits.filter(traitdetail__requirement_level='required')]
    def get_preferred_traits(self):
        return [(trait, trait.traitdetail_set.filter(position=self).first().level) for trait in self.traits.filter(traitdetail__requirement_level='preferred')]
    def get_bonus_traits(self):
        return [(trait, trait.traitdetail_set.filter(position=self).first().level) for trait in self.traits.filter(traitdetail__requirement_level='bonus')]


    def __str__(self):
        return f'{self.title} ({self.company})'

class Benefit(models.Model):
    tag = models.CharField()
    description = models.TextField()

    @property
    def stub(self):
        return '-'.join(self.tag.strip().lower().replace(r'[^a-z -]', '').split())

    def __str__(self):
        return self.tag

class BenefitAvailable(models.Model):
    position = models.ForeignKey(Position, models.CASCADE)
    benefit = models.ForeignKey(Benefit, models.CASCADE)

    available = models.CharField()  # use for 'after 30 days', e.g.

    class Meta:
        verbose_name_plural = 'benefits available'

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

class Trait(models.Model):
    tag = models.CharField(max_length=25)

    @property
    def stub(self):
        return '-'.join(self.tag.strip().lower().replace(r'[^a-z -]', '').split())

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
