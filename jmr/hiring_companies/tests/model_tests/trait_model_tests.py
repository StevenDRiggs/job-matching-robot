from django.test import TestCase

from hiring_companies.models import Trait


class TraitModelTests(TestCase):
    def test_can_create_trait(self):
        Trait.objects.create(name='trait test')
        self.assertEqual(len(Trait.objects.all()), 1)
