from django.db.utils import IntegrityError
from django.test import TestCase

from hiring_companies.models import (
    Company,
    JobRequirements,
    Skill,
    SkillLevel,
)


class SkillLevelModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.company = Company.objects.create(
            company_name_original='test company',
        )
        cls.job_requirements = JobRequirements.objects.create(
            company=cls.company,
        )
        cls.skill = Skill.objects.create(
            name='test skill',
            hard=True,
        )

    def test_can_create_skill_level_with_job_requirements_and_skill_and_minimal_args(self):
        SkillLevel.objects.create(
            job_requirement=self.job_requirements,
            skill=self.skill,
            level=5,
        )
        self.assertEqual(len(SkillLevel.objects.all()), 1)

    def test_can_create_skill_level_with_job_requirements_and_skill_and_all_args(self):
        SkillLevel.objects.create(
            job_requirement=self.job_requirements,
            skill=self.skill,
            level=5,
            required=True,
        )
        self.assertEqual(len(SkillLevel.objects.all()), 1)

    def test_cannot_create_skill_level_without_job_requirements(self):
        skill_level = SkillLevel(
            skill=self.skill,
            level=5,
        )
        self.assertRaises(IntegrityError, skill_level.save)

    def test_cannot_create_skill_level_without_skill(self):
        skill_level = SkillLevel(
            job_requirement=self.job_requirements,
            level=5,
        )
        self.assertRaises(IntegrityError, skill_level.save)
