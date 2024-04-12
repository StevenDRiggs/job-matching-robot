from datetime import datetime, timedelta
from django.db.utils import IntegrityError
from django.test import TestCase

from .models import (
    Address,
    CareerField,
    CareerSubfield,
    CompanyField,
    Preferences,
    Skill,
    Trait,
    User,
    WorkTask
)


class AddressModelTests(TestCase):
    def test_can_create_address_with_minimal_args(self):
        address = Address(
            street_address='test street address',
            city='test city',
            country='test country',
        )
        address.save()
        self.assertEqual(len(Address.objects.all()), 1)

    def test_can_create_address_with_all_args(self):
        address = Address(
            street_address='test street address',
            city='test city',
            county='test county',
            state='test state',
            country='test country',
        )
        address.save()
        self.assertEqual(len(Address.objects.all()), 1)


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


class WorkTaskModelTests(TestCase):
    def test_can_create_work_task(self):
        work_task = WorkTask(name='test work task', description='test work description')
        work_task.save()
        self.assertEqual(len(WorkTask.objects.all()), 1)


class PreferencesModelTests(TestCase):
    def test_can_create_preferences_with_minimal_args(self):
        preferences = Preferences()
        preferences.save()
        self.assertEqual(len(Preferences.objects.all()), 1)

    def test_can_create_preferences_with_all_args(self):
        preferred_company_field1 = CompanyField(name='preferred company field 1')
        preferred_company_field1.save()
        preferred_company_field2 = CompanyField(name='preferred company field 2')
        preferred_company_field2.save()
        non_preferred_company_field1 = CompanyField(name='non-preferred company field 1')
        non_preferred_company_field1.save()
        non_preferred_company_field2 = CompanyField(name='non-preferred company field 2')
        non_preferred_company_field2.save()
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
            preferred_locations='["here", "there"]',
            non_preferred_locations = '["everywhere else"]',
            preferred_pay_low=1000.00,
            preferred_pay_high=10000.00,
            desired_onsite_time=timedelta(days=1),
            days_and_hours_available='[[["SUN", "0900"], ["SUN", "1700"]], [["WED", "1000"], ["WED", "1800"]], [["SAT", "1200"], ["SAT", "1400"]]]',
            start_date_available=datetime.today() + timedelta(days=10),
            start_search_date=datetime.today() + timedelta(days=1),
            end_search_date=datetime.today() + timedelta(days=5),
        )
        preferences.save()
        preferences.preferred_company_fields.set([preferred_company_field1, preferred_company_field2])
        preferences.non_preferred_company_fields.set([non_preferred_company_field1, non_preferred_company_field2])
        preferences.preferred_career_fields.set([preferred_career_field1, preferred_career_field2])
        preferences.non_preferred_career_fields.set([non_preferred_career_field1, non_preferred_career_field2])
        preferences.preferred_career_subfields.set([preferred_career_subfield1, preferred_career_subfield2])
        preferences.non_preferred_career_subfields.set([non_preferred_career_subfield1, non_preferred_career_subfield2])
        preferences.preferred_work_tasks.set([preferred_work_task1, preferred_work_task2])
        self.assertEqual(len(Preferences.objects.all()), 1)


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


class UserModelTests(TestCase):
    def test_can_create_user_with_minimal_args(self):
        preferences = Preferences()
        preferences.save()
        user = User(
            full_name_original='User Test',
            sort_by=['Test', 'User'],
            preferences=preferences,
        )
        user.save()
        self.assertEqual(len(User.objects.all()), 1)

    def test_can_create_user_with_all_args(self):
        address = Address(
            street_address='test street address',
            city='test city',
            county='test county',
            state='test state',
            country='test country',
        )
        address.save()
        preferred_company_field = CompanyField(name='preferred company field')
        preferred_company_field.save()
        non_preferred_company_field = CompanyField(name='non-preferred company field')
        non_preferred_company_field.save()
        preferred_career_field = CareerField(name='preferred career field')
        preferred_career_field.save()
        non_preferred_career_field = CareerField(name='non-preferred career field')
        non_preferred_career_field.save()
        preferred_career_subfield = CareerSubfield(name='preferred career subfield', career_field=preferred_career_field)
        preferred_career_subfield.save()
        non_preferred_career_subfield = CareerSubfield(name='non-preferred career subfield', career_field=non_preferred_career_field)
        non_preferred_career_subfield.save()
        preferred_work_task = WorkTask(name='preferred work task', description='preferred work task description')
        preferred_work_task.save()
        preferences = Preferences(
            remote=True,
            relocate=True,
            relocation_distance=25,
            distance_measurement='km',
            relocation_assistance_needed=True,
            relocation_assistance_amount=15000.00,
            preferred_locations='["over here", "rot thar"]',
            non_preferred_locations='["your place", "my place"]',
            preferred_pay_low=15.00,
            preferred_pay_high=1_500_000.25,
            desired_onsite_time=timedelta(days=7),
            days_and_hours_available='[[["SUN", "2359"], ["MON", "0001"]]]',
            start_search_date=datetime.today() + timedelta(days=365),
            end_search_date=datetime.today() + timedelta(days=367),
        )
        preferences.save()
        preferences.preferred_company_fields.set([preferred_company_field])
        preferences.non_preferred_company_fields.set([non_preferred_company_field])
        preferences.preferred_career_fields.set([preferred_career_field])
        preferences.non_preferred_career_fields.set([non_preferred_career_field])
        preferences.preferred_career_subfields.set([preferred_career_subfield])
        preferences.non_preferred_career_subfields.set([non_preferred_career_subfield])
        preferences.preferred_work_tasks.set([preferred_work_task])
        skill = Skill(name='test skill', hard=False)
        skill.save()
        trait = Trait(name='test trait')
        trait.save()
        user = User(
            full_name_original='test user',
            full_name_latinized='test user',
            sort_by='["user", "test"]',
            address=address,
            preferences=preferences,
        )
        user.save()
        user.skills.set([skill])
        user.traits.set([trait])
        self.assertEqual(len(User.objects.all()), 1)
