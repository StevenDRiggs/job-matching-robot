from django.test import TestCase

from hiring_companies.models import (
    Company,
    JobLocation,
    JobRequirements,
)
from job_seekers.models import (
    Address,
    Preferences,
    User,
)
from matching.models import Match


class MatchModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create(
            full_name_original='test user 1',
            sort_by=['1', 'user', 'test'],
            preferences=Preferences.objects.create(),
        )
        cls.user1.addresses.add(
            Address.objects.create(
                street_address='3895 W 119th Mews',
                city='Westminster',
                state='CO',
                country='USA',
                user=cls.user1,
            ),
            Address.objects.create(
                street_address='8466 Cook Way',
                city='Thornton',
                state='CO',
                country='USA',
                user=cls.user1,
            ),
        )
        cls.user1.save()
        cls.user2 = User.objects.create(
            full_name_original='test user 2',
            sort_by=['2', 'user', 'test'],
            preferences=Preferences.objects.create(),
        )
        cls.user2.addresses.add(
            Address.objects.create(
                street_address='10395 South Crosset Hill Drive',
                city='Pickerington',
                state='OH',
                country='USA',
                user=cls.user2,
            ),
        )
        cls.user2.save()
        cls.company1 = Company.objects.create(
            company_name_original='test company 1',
        )
        cls.company1.job_requirements = JobRequirements.objects.create(
            company=cls.company1,
        )
        cls.company1.job_requirements.job_locations.add(
            JobLocation.objects.create(
                city='Denver',
                state='CO',
                country='USA',
            ),
            JobLocation.objects.create(
                city='Washington',
                state='DC',
                country='USA',
            ),
        )
        cls.company1.save()

    def test_can_match_by_remote(self):
        user1 = self.user1
        user1.preferences.remote = True
        user1.preferences.save()
        user2 = self.user2
        user2.preferences.hybrid = True
        user2.preferences.days_and_hours = ''
        user2.preferences.save()
        company1 = self.company1
        company1.job_requirements.remote = True
        company1.job_requirements.save()
        matches = Match.find_exact(company=company1)
        self.assertEqual(matches, [user1])

    def test_can_match_by_hybrid(self):
        user1 = self.user1
        user1.preferences.hybrid = True
        user1.preferences.save()
        user2 = self.user2
        user2.preferences.remote = True
        user2.preferences.days_and_hours = ''
        user2.preferences.save()
        company1 = self.company1
        company1.job_requirements.hybrid = True
        company1.job_requirements.save()
        matches = Match.find_exact(company=company1)
        self.assertEqual(matches, [user1])

    def test_can_match_by_days_and_hours(self):
        user1 = self.user1
        user1.preferences.days_and_hours = {
            'MON': ('1000', '1400'),
            'WED': ('1000', '1400'),
            'FRI': ('1000', '1400'),
        }
        user1.preferences.save()
        user2 = self.user2
        user2.preferences.remote = True
        user2.preferences.hybrid = True
        user2.preferences.save()
        company1 = self.company1
        company1.job_requirements.days_and_hours = {
            'MON': ('1000', '1400'),
            'WED': ('1000', '1400'),
            'FRI': ('1000', '1400'),
        }
        company1.job_requirements.save()
        matches = Match.find_exact(company=company1)
        self.assertEqual(matches, [user1])
