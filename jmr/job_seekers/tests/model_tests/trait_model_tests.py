from django.test import TestCase

from job_seekers.models import Trait


class TraitModelTests(TestCase):
    def test_can_create_trait(self):
        trait = Trait(name='trait test')
        trait.save()
        self.assertEqual(len(Trait.objects.all()), 1)
