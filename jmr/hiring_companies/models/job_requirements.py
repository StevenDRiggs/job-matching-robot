from datetime import date, timedelta
from django.db import models

from .career_field import CareerField
from .career_subfield import CareerSubfield
from .company_field import CompanyField
from .job_location import JobLocation
from .skill import Skill
from .trait import Trait
from .work_task import WorkTask


class JobRequirements(models.Model):
    job_locations = models.ManyToManyField(JobLocation, related_name='jobs_available')
    remote_or_hybrid = models.BooleanField(default=False)
    required_onsite_time = models.DurationField(default=timedelta(days=5))

    relocation_assistance_available = models.BooleanField(default=False)
    maximum_relocation_distance = models.SmallIntegerField(null=True)
    distance_measurement = models.CharField(max_length=2, choices={'mi': 'mi', 'km': 'km'}, null=True)
    maximum_relocation_assistance_amount = models.DecimalField(max_digits=10, decimal_places=2,  default=0.00)

    company_fields_available = models.ManyToManyField(CompanyField, related_name='jobs_available')
    career_fields_available = models.ManyToManyField(CareerField,related_name='jobs_available')
    career_subfields_available = models.ManyToManyField(CareerSubfield, related_name='jobs_available')

    skills = models.ManyToManyField(Skill, related_name='jobs_available', through='SkillLevel')
    required_traits = models.ManyToManyField(Trait, related_name='jobs_available')
    work_tasks = models.ManyToManyField(WorkTask, related_name='jobs_available')

    pay_low = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    pay_high = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def default_position_days_and_hours():
        return '[[["MON", "0900"], ["MON", "1700"]], [["TUE", "0900"], ["TUE", "1700"]], [["WED", "0900"], ["WED", "1700"]], [["THU", "0900"], ["THU", "1700"]], [["FRI", "0900"], ["FRI", "1700"]]]'
    position_days_and_hours = models.JSONField(default=default_position_days_and_hours)
    start_date_requested = models.DateField(default=date.today)

    position_availability_start_date = models.DateField(default=date.today)
    position_availability_end_date = models.DateField(null=True)
