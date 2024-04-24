from django.db.utils import IntegrityError
from django.test import TestCase

from job_seekers.models import (
    CareerField,
    CareerSubfield,
)


class CareerSubfieldModelTests(TestCase):
    def test_can_create_career_subfield_with_career_field(self):
        career_field = CareerField(name='test career field')
        career_field.save()
        career_subfield = CareerSubfield(name='test career subfield', career_field=career_field)
        career_subfield.save()
        self.assertEqual(len(CareerSubfield.objects.all()), 1)

    def test_cannot_create_career_subfield_without_career_field(self):
        career_subfield = CareerSubfield(name='test career subfield')
        self.assertRaises(IntegrityError, career_subfield.save)
