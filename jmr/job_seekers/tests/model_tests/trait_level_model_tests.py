import json

from django.db.utils import IntegrityError
from django.test import TestCase

from job_seekers.models import (
    Trait,
    TraitLevel,
    User,
)


class TraitLevelModelTests(TestCase):
    def test_can_create_trait_level_with_trait_and_user(self):
        trait = Trait.objects.create(name='test trait')
        user = User.objects.create(full_name_original='test user', sort_by=json.dumps(['user', 'test']))
        trait_level = TraitLevel.objects.create(
            trait=trait,
            user=user,
            level=5,
        )
        self.assertEqual(len(TraitLevel.objects.all()), 1)

    def test_cannot_create_trait_level_without_trait(self):
        user = User.objects.create(full_name_original='test user', sort_by=json.dumps(['user', 'test']))
        trait_level = TraitLevel(
            user=user,
            level=5,
        )
        self.assertRaises(IntegrityError, trait_level.save)

    def test_cannot_create_trait_level_without_user(self):
        trait = Trait.objects.create(name='test trait')
        trait_level = TraitLevel(
            trait=trait,
            level=5,
        )
        self.assertRaises(IntegrityError, trait_level.save)
