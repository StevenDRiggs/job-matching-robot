from django.db import models
from djmoney.models.fields import MoneyField

from .Company import Company


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
    def get_pay(self):
        return {
            'amount': float(self.pay.amount),
            'currency': str(self.pay.currency)
        }

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
    def get_benefits(self):
        output = []
        for benefit in self.benefits.all():
            output.append({
                'pk': benefit.pk,
                'tag': benefit.tag,
                'available': self.benefits_available.get(benefit=benefit).available,
            })

        return output

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
