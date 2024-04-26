from django.db.utils import IntegrityError
from django.test import TestCase

from hiring_companies.models import (
    JobRequirements,
    Skill,
    SkillLevel,
)


class SkillLevelModelTests(TestCase):
    def test_can_create_skill_level_with_job_requirements_and_skill_and_minimal_args(self):
        job_requirements = JobRequirements.objects.create()
        skill = Skill.objects.create(name='test skill', hard=False)
        skill_level = SkillLevel.objects.create(
            job_requirement=job_requirements,
            skill=skill,
            level=5,
        )
        self.assertEqual(len(SkillLevel.objects.all()), 1)

    def test_can_create_skill_level_with_job_requirements_and_skill_and_all_args(self):
        job_requirements = JobRequirements.objects.create()
        skill = Skill.objects.create(name='test skill', hard=False)
        skill_level = SkillLevel.objects.create(
            job_requirement=job_requirements,
            skill=skill,
            level=5,
            required=True,
        )
        self.assertEqual(len(SkillLevel.objects.all()), 1)

    def test_cannot_create_skill_level_without_job_requirements(self):
        skill = Skill.objects.create(name='test skill', hard=False)
        skill_level = SkillLevel(
            skill=skill,
            level=5,
        )
        self.assertRaises(IntegrityError, skill_level.save)

    def test_cannot_create_skill_level_without_skill(self):
        job_requirements = JobRequirements.objects.create()
        skill_level = SkillLevel(
            job_requirement=job_requirements,
            level=5,
        )
        self.assertRaises(IntegrityError, skill_level.save)
