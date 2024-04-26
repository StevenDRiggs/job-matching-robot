from django.test import TestCase

from job_seekers.models import Industry


class IndustryModelTests(TestCase):
    def test_can_create_industry(self):
        industry = Industry.objects.create(name='test industry')
        self.assertEqual(len(Industry.objects.all()), 1)
