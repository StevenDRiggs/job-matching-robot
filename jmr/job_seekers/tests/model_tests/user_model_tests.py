from datetime import datetime, timedelta
from django.test import TestCase

from job_seekers.models import (
    CareerField,
    CareerSubfield,
    Industry,
    Preferences,
    Skill,
    SkillLevel,
    Trait,
    TraitLevel,
    User,
    WorkTask,
)


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
        # address = Address(  # TODO: update for correct assignment
        #     street_address='test street address',
        #     city='test city',
        #     county='test county',
        #     state='test state',
        #     country='test country',
        # )
        # address.save()
        preferred_industry = Industry(name='preferred industry')
        preferred_industry.save()
        non_preferred_industry = Industry(name='non-preferred industry')
        non_preferred_industry.save()
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
            # preferred_locations='["over here", "rot thar"]',  # TODO: update for correct assignment
            # non_preferred_locations='["your place", "my place"]',
            preferred_pay_low=15.00,
            preferred_pay_high=1_500_000.25,
            desired_onsite_time=7,
            days_and_hours_available='[[["SUN", "2359"], ["MON", "0001"]]]',
            start_search_date=datetime.today() + timedelta(days=365),
            end_search_date=datetime.today() + timedelta(days=367),
        )
        preferences.save()
        preferences.preferred_industries.set([preferred_industry])
        preferences.non_preferred_industries.set([non_preferred_industry])
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
            # address=address,  # TODO: update for correct assignment
            preferences=preferences,
        )
        user.save()
        skill_level = SkillLevel(skill=skill, user=user, level=1)
        skill_level.save()
        user.skills.set([skill])
        trait_level = TraitLevel(trait=trait, user=user, level=1)
        trait_level.save()
        user.traits.set([trait])
        self.assertEqual(len(User.objects.all()), 1)
