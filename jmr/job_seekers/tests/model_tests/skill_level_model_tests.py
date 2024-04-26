import json

from django.db.utils import IntegrityError
from django.test import TestCase

from job_seekers.models import (
    Skill,
    SkillLevel,
    User,
)


class SkillLevelModelTests(TestCase):
    def test_can_create_skill_level_with_skill_and_user(self):
        skill = Skill.objects.create(name='test skill', hard=False)
        user = User.objects.create(full_name_original='test user', sort_by=json.dumps(['user', 'test']))
        skill_level = SkillLevel.objects.create(
            skill=skill,
            user=user,
            level=5,
        )
        self.assertEqual(len(SkillLevel.objects.all()), 1)

    def test_cannot_create_skill_level_without_skill(self):
        user = User.objects.create(full_name_original='test user', sort_by=json.dumps(['user', 'test']))
        skill_level = SkillLevel(
            user=user,
            level=5,
        )
        self.assertRaises(IntegrityError, skill_level.save)

    def test_cannot_create_skill_level_without_user(self):
        skill = Skill.objects.create(name='test skill', hard=False)
        skill_level = SkillLevel(
            skill=skill,
            level=5,
        )
        self.assertRaises(IntegrityError, skill_level.save)
