from django.test import TestCase

from job_seekers.models import Industry


class IndustryModelTests(TestCase):
    def test_can_create_industry(self):
        industry = Industry(name='test industry')
        industry.save()
        self.assertEqual(len(Industry.objects.all()), 1)
