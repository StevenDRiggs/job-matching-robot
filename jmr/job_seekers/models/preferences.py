import json

from datetime import date, timedelta
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from djmoney.contrib.exchange.backends import OpenExchangeRatesBackend
from djmoney.contrib.exchange.models import convert_money
from djmoney.models.fields import MoneyField

from .career_field import CareerField
from .career_subfield import CareerSubfield
from .industry import Industry
from .work_task import WorkTask


class Preferences(models.Model):
    def __init__(self, *args, **kwargs):
        backend = OpenExchangeRatesBackend()
        backend.update_rates()
        super().__init__(*args, **kwargs)

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
    start_date = models.DateField(default=date.today)
    maximum_commute = models.SmallIntegerField(default=100, null=True, blank=True)
    relocate = models.BooleanField(default=False)
    maximum_relocation_distance = models.SmallIntegerField(default=0, null=True, blank=True)
    distance_measurement = models.CharField(max_length=2, choices={'mi': 'mi', 'km': 'km'}, null=True, blank=True)
    _relocation_assistance_amount = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', default=0, blank=True)
    @property
    def relocation_assistance_amount_usd(self):
        return convert_money(self._relocation_assistance_amount, 'USD')
    pay_low = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', null=True, blank=True)
    pay_high = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', null=True, blank=True)
    work_tasks = models.ManyToManyField(WorkTask, blank=True)

    start_search_date = models.DateField(default=date.today)
    end_search_date = models.DateField(null=True, blank=True)

    preferred_locations = models.ManyToManyField('hiring_companies.JobLocation', related_name='location_preferred_by', blank=True)
    non_preferred_locations = models.ManyToManyField('hiring_companies.JobLocation', related_name='location_non_preferred_by', blank=True)

    preferred_industries = models.ManyToManyField(Industry, related_name='company_preferred_by', blank=True)
    non_preferred_industries = models.ManyToManyField(Industry, related_name='company_non_preferred_by', blank=True)

    preferred_career_fields = models.ManyToManyField(CareerField, related_name='career_preferred_by', blank=True)
    non_preferred_career_fields = models.ManyToManyField(CareerField, related_name='career_non_preferred_by', blank=True)

    preferred_career_subfields = models.ManyToManyField(CareerSubfield, related_name='career_preferred_by', blank=True)
    non_preferred_career_subfields = models.ManyToManyField(CareerSubfield, related_name='career_non_preferred_by', blank=True)


    def __str__(self):
        try:
            return f'User {self.user.name} preferences'
        except ObjectDoesNotExist as e:
            return f'Unassigned preferences {self.id}'

    class Meta:
        verbose_name_plural = 'preferences'
