from django.db.utils import IntegrityError
from django.test import TestCase

from hiring_companies.models import (
    Company,
    JobRequirements,
    Trait,
    TraitLevel,
)


class TraitLevelModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.company = Company.objects.create(
            company_name_original='test company',
        )
        cls.job_requirements = JobRequirements.objects.create(
            company=cls.company,
        )
        cls.trait = Trait.objects.create(
            name='test trait',
        )

    def test_can_create_trait_level_with_job_requirements_and_trait_and_minimal_args(self):
        TraitLevel.objects.create(
            job_requirement=self.job_requirements,
            trait=self.trait,
            level=5,
        )
        self.assertEqual(len(TraitLevel.objects.all()), 1)

    def test_can_create_trait_level_with_job_requirements_and_trait_and_all_args(self):
        trait_level = TraitLevel.objects.create(
            job_requirement=self.job_requirements,
            trait=self.trait,
            level=5,
            required=True,
        )
        self.assertEqual(len(TraitLevel.objects.all()), 1)

    def test_cannot_create_trait_level_without_job_requirements(self):
        trait_level = TraitLevel(
            trait=self.trait,
            level=5,
        )
        self.assertRaises(IntegrityError, trait_level.save)

    def test_cannot_create_trait_level_without_trait(self):
        trait_level = TraitLevel(
            job_requirement=self.job_requirements,
            level=5,
        )
        self.assertRaises(IntegrityError, trait_level.save)
