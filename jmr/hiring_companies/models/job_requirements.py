import json

from datetime import date, timedelta
from django.db import models
from djmoney.models.fields import MoneyField

from .career_field import CareerField
from .career_subfield import CareerSubfield
from .industry import Industry
from .job_location import JobLocation
from .skill import Skill
from .trait import Trait
from .work_task import WorkTask


class JobRequirements(models.Model):
    remote = models.BooleanField(default=False)
    hybrid = models.BooleanField(default=False)
    def default_days_and_hours():
        return {
            'MON': ('0900', '1700'),
            'TUE': ('0900', '1700'),
            'WED': ('0900', '1700'),
            'THU': ('0900', '1700'),
            'FRI': ('0900', '1700'),
        }
    days_and_hours = models.JSONField(default=default_days_and_hours)
    start_date_earliest = models.DateField(default=date.today)
    start_date_latest = models.DateField(default=date.today)
    relocate = models.BooleanField(default=False)
    maximum_relocation_distance = models.SmallIntegerField(default=0, null=True, blank=True)
    distance_measurement = models.CharField(max_length=2, choices={'mi': 'mi', 'km': 'km'}, null=True, blank=True)
    relocation_assistance_amount = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', default=0, blank=True)
    pay_low = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', null=True, blank=True)
    pay_high = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', null=True, blank=True)
    work_tasks = models.ManyToManyField(WorkTask, related_name='jobs_available')

    position_availability_start_date = models.DateField(default=date.today)
    position_availability_end_date = models.DateField(null=True, blank=True)

    job_locations = models.ManyToManyField(JobLocation, related_name='jobs_available')

    industries_available = models.ManyToManyField(Industry, related_name='jobs_available')

    career_fields_available = models.ManyToManyField(CareerField,related_name='jobs_available')

    career_subfields_available = models.ManyToManyField(CareerSubfield, related_name='jobs_available')

    skills = models.ManyToManyField(Skill, related_name='jobs_available', through='SkillLevel')
    traits = models.ManyToManyField(Trait, related_name='jobs_available', through='TraitLevel')

    company = models.ForeignKey('Company', on_delete=models.CASCADE)


    def __str__(self):
        try:
            return f'{self.company.name} job requirements'
        except ObjectDoesNotExist as e:
            return f'Unassigned job requirements {self.id}'

    class Meta:
        verbose_name_plural = 'job requirements'
