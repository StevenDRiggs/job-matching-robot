from django.db.utils import IntegrityError
from django.test import TestCase

from hiring_companies.models import (
    Company,
    JobRequirements,
)


class CompanyModelTests(TestCase):
    def test_can_create_company_with_minimal_args(self):
        job_requirements = JobRequirements.objects.create()
        company = Company.objects.create(
            company_name_original='test company name',
            job_requirements=job_requirements,
        )
        self.assertEqual(len(Company.objects.all()), 1)

    def test_can_create_company_with_all_args(self):
        job_requirements = JobRequirements.objects.create()
        company = Company.objects.create(
            company_name_original='test company name original',
            company_name_latinized='test company name latinized',
            job_requirements=job_requirements,
        )
        self.assertEqual(len(Company.objects.all()), 1)

    def test_cannot_create_company_without_job_requiements(self):
        company = Company(
            company_name_original='test company name original',
        )
        self.assertRaises(IntegrityError, company.save)
