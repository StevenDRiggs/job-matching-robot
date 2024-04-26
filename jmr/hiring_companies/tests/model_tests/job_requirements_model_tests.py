import json

from datetime import date, timedelta
from django.test import TestCase
from djmoney.money import Money

from hiring_companies.models import (
    CareerField,
    CareerSubfield,
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
    def test_can_create_job_requirements_with_minimal_args(self):
        job_requirements = JobRequirements.objects.create()
        self.assertEqual(len(JobRequirements.objects.all()), 1)

    def test_can_create_job_requirements_with_all_args(self):
        job_location = JobLocation.objects.create(city='test city', country='test country')
        industry = Industry.objects.create(name='test industry')
        career_field = CareerField.objects.create(name='test career field')
        career_subfield = CareerSubfield.objects.create(name='test career subfield', career_field=career_field)
        skill = Skill.objects.create(name='test skill', hard=True)
        trait = Trait.objects.create(name='test trait')
        work_task = WorkTask.objects.create(name='test work task name', description='test work task description')
        job_requirements = JobRequirements.objects.create(
            remote_or_hybrid=True,
            required_onsite_time=timedelta(days=3),
            relocation_assistance_available=True,
            maximum_relocation_distance=150,
            distance_measurement='mi',
            maximum_relocation_assistance_amount=Money(10000.25, 'EUR'),
            pay_low=Money(125000.25, 'EUR'),
            pay_high=Money(155000.25, 'EUR'),
            position_days_and_hours=json.dumps({
                'MON': ('1000', '1800'),
                'WED': ('1000', '1800'),
                'FRI': ('1100', '1700'),
            }),
            start_date_requested=date.today() + timedelta(days=7),
            position_availability_start_date=date.today() + timedelta(days=7),
            position_availability_end_date=date.today() + timedelta(weeks=10),
        )
        job_requirements.job_locations.set([job_location])
        job_requirements.industries_available.set([industry])
        job_requirements.career_fields_available.set([career_field])
        job_requirements.career_subfields_available.set([career_subfield])
        skill_level = SkillLevel.objects.create(
            job_requirement=job_requirements,
            skill=skill,
            level=3,
        )
        trait_level = TraitLevel.objects.create(
            job_requirement=job_requirements,
            trait=trait,
            level=4,
        )
        job_requirements.work_tasks.set([work_task])
        self.assertEqual(len(JobRequirements.objects.all()), 1)
