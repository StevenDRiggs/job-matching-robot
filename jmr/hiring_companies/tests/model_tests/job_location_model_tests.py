from django.test import TestCase

from hiring_companies.models import JobLocation


class JobLocationModelTests(TestCase):
    def test_can_create_job_location_with_minimal_args(self):
        job_location = JobLocation.objects.create(
            city='test city',
            country='test country',
        )
        self.assertEqual(len(JobLocation.objects.all()), 1)

    def test_can_create_job_location_with_all_args(self):
        job_location = JobLocation.objects.create(
            city='test city',
            county='test county',
            state='test state',
            country='test country',
        )
        self.assertEqual(len(JobLocation.objects.all()), 1)
