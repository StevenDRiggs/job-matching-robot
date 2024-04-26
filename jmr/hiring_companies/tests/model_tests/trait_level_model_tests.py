from django.db.utils import IntegrityError
from django.test import TestCase

from hiring_companies.models import (
    JobRequirements,
    Trait,
    TraitLevel,
)


class TraitLevelModelTests(TestCase):
    def test_can_create_trait_level_with_job_requirements_and_trait_and_minimal_args(self):
        job_requirements = JobRequirements.objects.create()
        trait = Trait.objects.create(name='test trait')
        trait_level = TraitLevel.objects.create(
            job_requirement=job_requirements,
            trait=trait,
            level=5,
        )
        self.assertEqual(len(TraitLevel.objects.all()), 1)

    def test_can_create_trait_level_with_job_requirements_and_trait_and_all_args(self):
        job_requirements = JobRequirements.objects.create()
        trait = Trait.objects.create(name='test trait')
        trait_level = TraitLevel.objects.create(
            job_requirement=job_requirements,
            trait=trait,
            level=5,
            required=True,
        )
        self.assertEqual(len(TraitLevel.objects.all()), 1)

    def test_cannot_create_trait_level_without_job_requirements(self):
        trait = Trait.objects.create(name='test trait')
        trait_level = TraitLevel(
            trait=trait,
            level=5,
        )
        self.assertRaises(IntegrityError, trait_level.save)

    def test_cannot_create_trait_level_without_trait(self):
        job_requirements = JobRequirements.objects.create()
        trait_level = TraitLevel(
            job_requirement=job_requirements,
            level=5,
        )
        self.assertRaises(IntegrityError, trait_level.save)
