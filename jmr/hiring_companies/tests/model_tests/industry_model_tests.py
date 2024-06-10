from django.test import TestCase

from hiring_companies.models import Industry


class IndustryModelTests(TestCase):
    def test_can_create_industry(self):
        Industry.objects.create(name='test industry')
        self.assertEqual(len(Industry.objects.all()), 1)
