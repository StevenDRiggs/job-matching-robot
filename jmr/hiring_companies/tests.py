from datetime import date, timedelta
from django.db.utils import IntegrityError
from django.test import TestCase

from .models import (
    CareerField,
    CareerSubfield,
    Company,
    CompanyField,
    JobLocation,
    JobRequirements,
    Skill,
    Trait,
    WorkTask,
)


class CareerFieldModelTests(TestCase):
    def test_can_create_career_field(self):
        career_field = CareerField(name='test career field')
        career_field.save()
        self.assertEqual(len(CareerField.objects.all()), 1)


class CareerSubfieldModelTests(TestCase):
    def test_can_create_career_subfield_with_career_field(self):
        career_field = CareerField(name='test career field')
        career_field.save()
        career_subfield = CareerSubfield(name='test career subfield', career_field=career_field)
        career_subfield.save()
        self.assertEqual(len(CareerSubfield.objects.all()), 1)

    def test_cannot_create_career_subfield_without_career_field(self):
        career_subfield = CareerSubfield(name='test career subfield')
        self.assertRaises(IntegrityError, career_subfield.save)


class CompanyFieldModelTests(TestCase):
    def test_can_create_company_field(self):
        company_field = CompanyField(name='test company field')
        company_field.save()
        self.assertEqual(len(CompanyField.objects.all()), 1)


class JobLocationModelTests(TestCase):
    def test_can_create_job_location_with_minimal_args(self):
        job_location = JobLocation(
            city='test city',
            country='test country',
        )
        job_location.save()
        self.assertEqual(len(JobLocation.objects.all()), 1)

    def test_can_create_job_location_with_all_args(self):
        job_location = JobLocation(
            city='test city',
            county='test county',
            state='test state',
            country='test country',
        )
        job_location.save()
        self.assertEqual(len(JobLocation.objects.all()), 1)


class SkillModelTests(TestCase):
    def test_can_create_hard_skill(self):
        hard_skill = Skill(name='hard skill test', hard=True)
        hard_skill.save()
        self.assertEqual(len(Skill.objects.all()), 1)

    def test_can_create_soft_skill(self):
        soft_skill = Skill(name='soft skill test', hard=False)
        soft_skill.save()
        self.assertEqual(len(Skill.objects.all()), 1)


class TraitModelTests(TestCase):
    def test_can_create_trait(self):
        trait = Trait(name='trait test')
        trait.save()
        self.assertEqual(len(Trait.objects.all()), 1)


class WorkTaskModelTests(TestCase):
    def test_can_create_work_task(self):
        work_task = WorkTask(name='test work task', description='test work description')
        work_task.save()
        self.assertEqual(len(WorkTask.objects.all()), 1)


class JobRequirementsModelTests(TestCase):
    def test_can_create_job_requirements_with_minimal_args(self):
        job_requirements = JobRequirements()
        job_requirements.save()
        self.assertEqual(len(JobRequirements.objects.all()), 1)

    def test_can_create_job_requirements_with_all_args(self):
        job_location1 = JobLocation(
            city='test city 1',
            county='test county 1',
            state='test state 1',
            country='test country 1',
        )
        job_location1.save()
        job_location2 = JobLocation(
            city='test city 2',
            county='test county 2',
            state='test state 2',
            country='test country 2',
        )
        job_location2.save()
        company_field1 = CompanyField(name='company field 1')
        company_field1.save()
        company_field2 = CompanyField(name='company field 2')
        company_field2.save()
        career_field1 = CareerField(name='career field 1')
        career_field1.save()
        career_field2 = CareerField(name='career field 2')
        career_field2.save()
        career_subfield1 = CareerSubfield(name='career subfield 1', career_field=career_field1)
        career_subfield1.save()
        career_subfield2 = CareerSubfield(name='career subfield 2', career_field=career_field1)
        career_subfield2.save()
        career_subfield3 = CareerSubfield(name='career subfield 3', career_field=career_field2)
        career_subfield3.save()
        career_subfield4 = CareerSubfield(name='career subfield 4', career_field=career_field2)
        career_subfield4.save()
        skill1 = Skill(name='skill 1', hard=True)
        skill1.save()
        skill2 = Skill(name='skill 2', hard=False)
        skill2.save()
        trait1 = Trait(name='trait 1')
        trait1.save()
        trait2 = Trait(name='trait 2')
        trait2.save()
        work_task1 = WorkTask(name='work task 1', description='work task 1 description')
        work_task1.save()
        work_task2 = WorkTask(name='work task 2', description='work task 2 description')
        work_task2.save()
        job_requirements = JobRequirements(
            remote_or_hybrid=True,
            required_onsite_time=timedelta(days=3),
            relocation_assistance_available=True,
            maximum_relocation_distance=25,
            distance_measurement='km',
            maximum_relocation_assistance_amount=5000.00,
            pay_low=125_000.00,
            pay_high=225_000.00,
            position_days_and_hours='[[["MON", "0900"], ["MON", "1700"]], [["WED", "0800"], ["WED", "1600"]], [["FRI", "0800"], ["FRI", "1200"]]]',
            start_date_requested = date.today() + timedelta(days=7),
            position_availability_start_date=date.today() + timedelta(days=7),
            position_availability_end_date=date.today() + timedelta(weeks=26),
        )
        job_requirements.save()
        job_requirements.job_locations.set([job_location1, job_location2])
        job_requirements.company_fields_available.set([company_field1, company_field2])
        job_requirements.career_fields_available.set([career_field1, career_field2])
        job_requirements.career_subfields_available.set([career_subfield1, career_subfield2, career_subfield3, career_subfield4])
        job_requirements.required_skills.set([skill1, skill2])
        job_requirements.required_traits.set([trait1, trait2])
        job_requirements.work_tasks.set([work_task1, work_task2])
        self.assertEqual(len(JobRequirements.objects.all()), 1)


class CompanyModelTests(TestCase):
    def test_can_create_company_with_minimal_args(self):
        job_requirements = JobRequirements()
        job_requirements.save()
        company = Company(company_name_original='test company', job_requirements=job_requirements)
        company.save()
        self.assertEqual(len(Company.objects.all()), 1)

    def test_can_create_company_with_all_args(self):
        job_location1 = JobLocation(
            city='test city 1',
            county='test county 1',
            state='test state 1',
            country='test country 1',
        )
        job_location1.save()
        job_location2 = JobLocation(
            city='test city 2',
            county='test county 2',
            state='test state 2',
            country='test country 2',
        )
        job_location2.save()
        company_field1 = CompanyField(name='company field 1')
        company_field1.save()
        company_field2 = CompanyField(name='company field 2')
        company_field2.save()
        career_field1 = CareerField(name='career field 1')
        career_field1.save()
        career_field2 = CareerField(name='career field 2')
        career_field2.save()
        career_subfield1 = CareerSubfield(name='career subfield 1', career_field=career_field1)
        career_subfield1.save()
        career_subfield2 = CareerSubfield(name='career subfield 2', career_field=career_field1)
        career_subfield2.save()
        career_subfield3 = CareerSubfield(name='career subfield 3', career_field=career_field2)
        career_subfield3.save()
        career_subfield4 = CareerSubfield(name='career subfield 4', career_field=career_field2)
        career_subfield4.save()
        skill1 = Skill(name='skill 1', hard=True)
        skill1.save()
        skill2 = Skill(name='skill 2', hard=False)
        skill2.save()
        trait1 = Trait(name='trait 1')
        trait1.save()
        trait2 = Trait(name='trait 2')
        trait2.save()
        work_task1 = WorkTask(name='work task 1', description='work task 1 description')
        work_task1.save()
        work_task2 = WorkTask(name='work task 2', description='work task 2 description')
        work_task2.save()
        job_requirements = JobRequirements(
            remote_or_hybrid=True,
            required_onsite_time=timedelta(days=3),
            relocation_assistance_available=True,
            maximum_relocation_distance=25,
            distance_measurement='km',
            maximum_relocation_assistance_amount=5000.00,
            pay_low=125_000.00,
            pay_high=225_000.00,
            position_days_and_hours='[[["MON", "0900"], ["MON", "1700"]], [["WED", "0800"], ["WED", "1600"]], [["FRI", "0800"], ["FRI", "1200"]]]',
            start_date_requested = date.today() + timedelta(days=7),
            position_availability_start_date=date.today() + timedelta(days=7),
            position_availability_end_date=date.today() + timedelta(weeks=26),
        )
        job_requirements.save()
        job_requirements.job_locations.set([job_location1, job_location2])
        job_requirements.company_fields_available.set([company_field1, company_field2])
        job_requirements.career_fields_available.set([career_field1, career_field2])
        job_requirements.career_subfields_available.set([career_subfield1, career_subfield2, career_subfield3, career_subfield4])
        job_requirements.required_skills.set([skill1, skill2])
        job_requirements.required_traits.set([trait1, trait2])
        job_requirements.work_tasks.set([work_task1, work_task2])
