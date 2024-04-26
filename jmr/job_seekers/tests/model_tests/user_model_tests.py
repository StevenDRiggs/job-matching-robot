import json

from django.test import TestCase

from job_seekers.models import (
    Preferences,
    Skill,
    SkillLevel,
    Trait,
    TraitLevel,
    User,
)


class UserModelTests(TestCase):
    def test_can_create_user_with_minimal_args(self):
        user = User.objects.create(full_name_original='test user', sort_by=json.dumps(['user', 'test']))
        self.assertEqual(len(User.objects.all()), 1)

    def test_can_create_user_with_all_args(self):
        preferences = Preferences.objects.create()
        skill = Skill.objects.create(name='test skill', hard=True)
        trait = Trait.objects.create(name='test trait')
        user = User.objects.create(
            full_name_original='test user original',
            full_name_latinized='test user latinized',
            sort_by=json.dumps(['user', 'test']),
            preferences=preferences,
        )
        skill_level = SkillLevel.objects.create(
            skill=skill,
            user=user,
            level=5,
        )
        trait_level = TraitLevel.objects.create(
            trait=trait,
            user=user,
            level=5,
        )
        self.assertEqual(len(User.objects.all()), 1)
