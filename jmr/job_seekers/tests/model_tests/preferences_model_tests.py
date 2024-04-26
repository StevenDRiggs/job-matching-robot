import json

from datetime import date, timedelta
from django.test import TestCase
from djmoney.money import Money

from hiring_companies.models import JobLocation
from job_seekers.models import (
    CareerField,
    CareerSubfield,
    Industry,
    Preferences,
    WorkTask,
)


class PreferencesModelTests(TestCase):
    def test_can_create_preferences_with_minimal_args(self):
        preferences = Preferences.objects.create()
        self.assertEqual(len(Preferences.objects.all()), 1)

    def test_can_create_preferences_with_all_args(self):
        preferred_job_location = JobLocation.objects.create(
            city='preferred city',
            country='preferred country',
        )
        non_preferred_job_location = JobLocation.objects.create(
            city='non preferred city',
            country='non preferred country',
        )
        preferred_industry = Industry.objects.create(name='preferred industry')
        non_preferred_industry = Industry.objects.create(name='non preferred industry')
        preferred_career_field = CareerField.objects.create(name='preferred career field')
        non_preferred_career_field = CareerField.objects.create(name='non preferred career field')
        preferred_career_subfield = CareerSubfield.objects.create(name='preferred career subfield', career_field=preferred_career_field)
        non_preferred_career_subfield = CareerSubfield.objects.create(name='non preferred career subfield', career_field=non_preferred_career_field)
        work_task = WorkTask.objects.create(name='test work task', description='test work task description')
        preferences = Preferences.objects.create(
            remote=True,
            relocate=True,
            relocation_distance=25,
            distance_measurement='mi',
            relocation_assistance_needed=True,
            relocation_assistance_amount=Money(10000.25, 'EUR'),
            preferred_pay_low=Money(150000.25, 'EUR'),
            preferred_pay_high=Money(250000.25, 'EUR'),
            desired_onsite_time=3,
            days_and_hours_available=json.dumps({
                'MON': ('1000', '1800'),
                'WED': ('1000', '1800'),
                'FRI': ('1100', '1700'),
            }),
            start_date_available=date.today() + timedelta(days=7),
            start_search_date=date.today() + timedelta(days=1),
            end_search_date=date.today() + timedelta(weeks=10),
        )
        preferences.preferred_locations.set([preferred_job_location])
        preferences.non_preferred_locations.set([non_preferred_job_location])
        preferences.preferred_industries.set([preferred_industry])
        preferences.non_preferred_industries.set([non_preferred_industry])
        preferences.preferred_career_fields.set([preferred_career_field])
        preferences.non_preferred_career_fields.set([non_preferred_career_field])
        preferences.preferred_career_subfields.set([preferred_career_subfield])
        preferences.non_preferred_career_subfields.set([non_preferred_career_subfield])
        preferences.preferred_work_tasks.set([work_task])
        self.assertEqual(len(Preferences.objects.all()), 1)
