from django.test import TestCase

from job_seekers.models import CareerField


class CareerFieldModelTests(TestCase):
    def test_can_create_career_field(self):
        career_field = CareerField(name='test career field')
        career_field.save()
        self.assertEqual(len(CareerField.objects.all()), 1)