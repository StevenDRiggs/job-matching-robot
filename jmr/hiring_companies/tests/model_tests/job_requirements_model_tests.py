import json

from datetime import date, timedelta
from django.test import TestCase
from djmoney.money import Money

from hiring_companies.models import (
    CareerField,
    CareerSubfield,
    Company,
    Industry,
    JobLocation,
    JobRequirements,
    Skill,
    SkillLevel,
    Trait,
    TraitLevel,
    WorkTask,
)


class JobRequirementsModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.company = Company.objects.create(
            company_name_original='test company'
        )

    def test_can_create_job_requirements_with_minimal_args(self):
        JobRequirements.objects.create(
            company=self.company,
        )
        self.assertEqual(len(JobRequirements.objects.all()), 1)

    def test_can_create_job_requirements_with_all_args(self):
        job_requirements = JobRequirements.objects.create(
            company=self.company,
            remote=True,
            hybrid=True,
            days_and_hours={
                'MON': ('1000', '1800'),
                'WED': ('1000', '1800'),
                'FRI': ('1000', '1400'),
            },
            start_date_earliest=date.today() + timedelta(weeks=1),
            start_date_latest=date.today() + timedelta(weeks=2),
            maximum_commute=25,
            relocate=True,
            maximum_relocation_distance=25,
            distance_measurement='mi',
            _relocation_assistance_amount=Money(5000, 'USD'),
            pay_low=Money(100_000, 'USD'),
            pay_high=Money(125_000, 'USD'),
            position_availability_start_date=date.today() + timedelta(weeks=1),
            position_availability_end_date=date.today() + timedelta(weeks=2),
        )
        job_requirements.work_tasks.add(
            WorkTask.objects.create(
                name='test work task',
                description='test description',
            ),
        )
        job_requirements.job_locations.add(
            JobLocation.objects.create(
                city='Washington',
                state='DC',
                country='USA',
            ),
        )
        job_requirements.industries_available.add(
            Industry.objects.create(
                name='test industry',
            ),
        )
        job_requirements.career_fields_available.add(
            CareerField.objects.create(
                name='test career field',
            ),
        )
        job_requirements.career_subfields_available.add(
            CareerSubfield.objects.create(
                name='test career subfield',
                career_field=CareerField.objects.first(),
            ),
        )
        job_requirements.skills.add(
            Skill.objects.create(
                name='test skill',
                hard=True,
            ),
            through_defaults={
                'level': 2,
                'required': True,
            },
        )
        job_requirements.traits.add(
            Trait.objects.create(
                name='test trait',
            ),
            through_defaults={
                'level': 2,
                'required': False,
            },
        )
        job_requirements.save()
        self.assertEqual(len(JobRequirements.objects.all()), 1)
