from django.test import TestCase

from hiring_companies.models import CareerField


class CareerFieldModelTests(TestCase):
    def test_can_create_career_field(self):
        CareerField.objects.create(name='test career field')
        self.assertEqual(len(CareerField.objects.all()), 1)
