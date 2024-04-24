import json

from datetime import date, timedelta
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from djmoney.models.fields import MoneyField

from .career_field import CareerField
from .career_subfield import CareerSubfield
from .industry import Industry
from .work_task import WorkTask


class Preferences(models.Model):
    remote = models.BooleanField(default=False)
    relocate = models.BooleanField(default=False)
    relocation_distance = models.SmallIntegerField(default=0, null=True, blank=True)
    distance_measurement = models.CharField(max_length=2, choices={'mi': 'mi', 'km': 'km'}, null=True, blank=True)
    relocation_assistance_needed = models.BooleanField(default=False)
    relocation_assistance_amount = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', default=0, blank=True)
    preferred_locations = models.ManyToManyField('hiring_companies.JobLocation', related_name='location_preferred_by', blank=True)
    non_preferred_locations = models.ManyToManyField('hiring_companies.JobLocation', related_name='location_non_preferred_by', blank=True)

    preferred_industries = models.ManyToManyField(Industry, related_name='company_preferred_by', blank=True)
    non_preferred_industries = models.ManyToManyField(Industry, related_name='company_non_preferred_by', blank=True)
    preferred_career_fields = models.ManyToManyField(CareerField, related_name='career_preferred_by', blank=True)
    non_preferred_career_fields = models.ManyToManyField(CareerField, related_name='career_non_preferred_by', blank=True)
    preferred_career_subfields = models.ManyToManyField(CareerSubfield, related_name='career_preferred_by', blank=True)
    non_preferred_career_subfields = models.ManyToManyField(CareerSubfield, related_name='career_non_preferred_by', blank=True)

    preferred_work_tasks = models.ManyToManyField(WorkTask, blank=True)

    preferred_pay_low = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', null=True, blank=True)
    preferred_pay_high = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', null=True, blank=True)

    desired_onsite_time = models.SmallIntegerField(
        default=5,
        choices=[
            (0, 'None'),
            (1, '1 day'),
            (2, '2 days'),
            (3, '3 days'),
            (4, '4 days'),
            (5, '5 days'),
            (6, '6 days'),
            (7, '7 days'),
        ],
    )
    def default_days_and_hours_available():
        return {
            'MON': ('0900', '1700'),
            'TUE': ('0900', '1700'),
            'WED': ('0900', '1700'),
            'THU': ('0900', '1700'),
            'FRI': ('0900', '1700'),
        }
    days_and_hours_available = models.JSONField(default=default_days_and_hours_available)
    start_date_available = models.DateField(default=date.today)

    start_search_date = models.DateField(default=date.today)
    end_search_date = models.DateField(null=True, blank=True)


    def __str__(self):
        try:
            return f'User {self.user.id} preferences'
        except ObjectDoesNotExist as e:
            return f'Unassigned preferences {self.id}'

    class Meta:
        verbose_name_plural = 'preferences'
