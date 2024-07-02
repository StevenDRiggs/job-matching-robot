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
        Preferences.objects.create()
        self.assertEqual(len(Preferences.objects.all()), 1)

    def test_can_create_preferences_with_all_args(self):
        preferences = Preferences.objects.create(
            remote=True,
            hybrid=True,
            days_and_hours={
                'MON': ('1000', '1800'),
                'WED': ('1000', '1800'),
                'FRI': ('1000', '1400'),
            },
            start_date=date.today() + timedelta(weeks=1),
            maximum_commute=25,
            relocate=True,
            maximum_relocation_distance=25,
            distance_measurement='mi',
            _relocation_assistance_amount=Money(5000, 'USD'),
            pay_low=Money(100_000, 'USD'),
            pay_high=Money(150_000, 'USD'),
            start_search_date=date.today() + timedelta(weeks=1),
            end_search_date=date.today() + timedelta(weeks=2),
        )
        preferences.work_tasks.add(
            WorkTask.objects.create(
                name='test work task',
                description='test description',
            ),
        )
        preferences.preferred_industries.add(
            Industry.objects.create(
                name='test preferred industry',
            ),
        )
        preferences.non_preferred_industries.add(
            Industry.objects.create(
                name='test non-preferred industry',
            ),
        )
        preferences.preferred_career_fields.add(
            CareerField.objects.create(
                name='test preferred career field',
            ),
        )
        preferences.non_preferred_career_fields.add(
            CareerField.objects.create(
                name='test non-preferred career field',
            ),
        )
        preferences.preferred_career_subfields.add(
            CareerSubfield.objects.create(
                career_field=CareerField.objects.first(),
                name='test preferred career subfield',
            ),
        )
        preferences.non_preferred_career_subfields.add(
            CareerSubfield.objects.create(
                career_field=CareerField.objects.last(),
                name='test non-preferred career subfield',
            ),
        )
        preferences.save()
        self.assertEqual(len(Preferences.objects.all()), 1)
