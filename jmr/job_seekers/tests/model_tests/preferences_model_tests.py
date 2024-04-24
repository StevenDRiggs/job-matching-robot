from datetime import datetime, timedelta
from django.test import TestCase

from job_seekers.models import (
    CareerField,
    CareerSubfield,
    Industry,
    Preferences,
    WorkTask,
)


class PreferencesModelTests(TestCase):
    def test_can_create_preferences_with_minimal_args(self):
        preferences = Preferences()
        preferences.save()
        self.assertEqual(len(Preferences.objects.all()), 1)

    def test_can_create_preferences_with_all_args(self):
        preferred_industry1 = Industry(name='preferred industry 1')
        preferred_industry1.save()
        preferred_industry2 = Industry(name='preferred industry 2')
        preferred_industry2.save()
        non_preferred_industry1 = Industry(name='non-preferred industry 1')
        non_preferred_industry1.save()
        non_preferred_industry2 = Industry(name='non-preferred industry 2')
        non_preferred_industry2.save()
        preferred_career_field1 = CareerField(name='preferred career field 1')
        preferred_career_field1.save()
        preferred_career_field2 = CareerField(name='preferred career field 2')
        preferred_career_field2.save()
        non_preferred_career_field1 = CareerField(name='non-preferred career field 1')
        non_preferred_career_field1.save()
        non_preferred_career_field2 = CareerField(name='non-preferred career field 2')
        non_preferred_career_field2.save()
        preferred_career_subfield1 = CareerSubfield(name='preferred career subfield 1', career_field=preferred_career_field1)
        preferred_career_subfield1.save()
        preferred_career_subfield2 = CareerSubfield(name='preferred career subfield 2', career_field=preferred_career_field1)
        preferred_career_subfield2.save()
        non_preferred_career_subfield1 = CareerSubfield(name='non-preferred career subfield 1', career_field=preferred_career_field2)
        non_preferred_career_subfield1.save()
        non_preferred_career_subfield2 = CareerSubfield(name='non-preferred career subfield 2', career_field=preferred_career_field2)
        non_preferred_career_subfield2.save()
        preferred_work_task1 = WorkTask(name='preferred work task 1', description='preferred work task 1 description')
        preferred_work_task1.save()
        preferred_work_task2 = WorkTask(name='preferred work task 2', description='preferred work task 2 description')
        preferred_work_task2.save()
        preferences = Preferences(
            remote=True,
            relocate=True,
            relocation_distance=25,
            distance_measurement='mi',
            relocation_assistance_needed=True,
            relocation_assistance_amount=1000.00,
            # preferred_locations='["here", "there"]',  # TODO: update for correct assignment (using .set())
            # non_preferred_locations = '["everywhere else"]',
            preferred_pay_low=1000.00,
            preferred_pay_high=10000.00,
            desired_onsite_time=1,
            days_and_hours_available='[[["SUN", "0900"], ["SUN", "1700"]], [["WED", "1000"], ["WED", "1800"]], [["SAT", "1200"], ["SAT", "1400"]]]',
            start_date_available=datetime.today() + timedelta(days=10),
            start_search_date=datetime.today() + timedelta(days=1),
            end_search_date=datetime.today() + timedelta(days=5),
        )
        preferences.save()
        preferences.preferred_industries.set([preferred_industry1, preferred_industry2])
        preferences.non_preferred_industries.set([non_preferred_industry1, non_preferred_industry2])
        preferences.preferred_career_fields.set([preferred_career_field1, preferred_career_field2])
        preferences.non_preferred_career_fields.set([non_preferred_career_field1, non_preferred_career_field2])
        preferences.preferred_career_subfields.set([preferred_career_subfield1, preferred_career_subfield2])
        preferences.non_preferred_career_subfields.set([non_preferred_career_subfield1, non_preferred_career_subfield2])
        preferences.preferred_work_tasks.set([preferred_work_task1, preferred_work_task2])
        self.assertEqual(len(Preferences.objects.all()), 1)