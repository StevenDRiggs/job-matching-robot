from django.db.utils import IntegrityError
from django.test import TestCase

from hiring_companies.models import Company


class CompanyModelTests(TestCase):
    def test_can_create_company_with_minimal_args(self):
        company = Company.objects.create(
            company_name_original='test company name',
        )
        self.assertEqual(len(Company.objects.all()), 1)

    def test_can_create_company_with_all_args(self):
        company = Company.objects.create(
            company_name_original='test company name original',
            company_name_latinized='test company name latinized',
        )
        self.assertEqual(len(Company.objects.all()), 1)
