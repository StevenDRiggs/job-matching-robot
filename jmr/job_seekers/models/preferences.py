from datetime import date, timedelta
from django.db import models

from .career_field import CareerField
from .career_subfield import CareerSubfield
from .company_field import CompanyField
from .work_task import WorkTask


class Preferences(models.Model):
    remote = models.BooleanField(default=False)
    relocate = models.BooleanField(default=False)
    relocation_distance = models.SmallIntegerField(null=True)
    distance_measurement = models.CharField(max_length=2, choices={'mi': 'mi', 'km': 'km'}, null=True)
    relocation_assistance_needed = models.BooleanField(default=False)
    relocation_assistance_amount = models.DecimalField(max_digits=10, decimal_places=2,  default=0.00)
    preferred_locations = models.JSONField(null=True)
    non_preferred_locations = models.JSONField(null=True)

    preferred_company_fields = models.ManyToManyField(CompanyField, related_name='company_preferred_by')
    non_preferred_company_fields = models.ManyToManyField(CompanyField, related_name='company_non_preferred_by')
    preferred_career_fields = models.ManyToManyField(CareerField, related_name='career_preferred_by')
    non_preferred_career_fields = models.ManyToManyField(CareerField, related_name='career_non_preferred_by')
    preferred_career_subfields = models.ManyToManyField(CareerSubfield, related_name='career_preferred_by')
    non_preferred_career_subfields = models.ManyToManyField(CareerSubfield, related_name='career_non_preferred_by')

    preferred_work_tasks = models.ManyToManyField(WorkTask)

    preferred_pay_low = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    preferred_pay_high = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    desired_onsite_time = models.DurationField(default=timedelta(days=5))
    def default_days_and_hours_available():
        return '[[["MON", "0900"], ["MON", "1700"]], [["TUE", "0900"], ["TUE", "1700"]], [["WED", "0900"], ["WED", "1700"]], [["THU", "0900"], ["THU", "1700"]], [["FRI", "0900"], ["FRI", "1700"]]]'
    days_and_hours_available = models.JSONField(default=default_days_and_hours_available)
    start_date_available = models.DateField(default=date.today)

    start_search_date = models.DateField(default=date.today)
    end_search_date = models.DateField(null=True)
