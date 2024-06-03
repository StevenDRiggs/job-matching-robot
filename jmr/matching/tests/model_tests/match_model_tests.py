from datetime import date, timedelta
from django.test import TestCase
from djmoney.money import Money

from hiring_companies.models import (
    CareerField,
    CareerSubfield,
    Company,
    Industry,
    JobLocation,
    JobRequirements,
    Skill,
    Trait,
    WorkTask,
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
                user=cls.user1,
                street_address='3895 W 119th Mews',
                city='Westminster',
                state='CO',
                country='USA',
            ),
            Address.objects.create(
                user=cls.user1,
                street_address='8466 Cook Way',
                city='Thornton',
                state='CO',
                country='USA',
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
                user=cls.user2,
                street_address='10395 South Crosset Hill Drive',
                city='Pickerington',
                state='OH',
                country='USA',
            ),
        )
        cls.user2.save()

        cls.company1 = Company.objects.create(
            company_name_original='test company 1',
        )
        jr = cls.company1.job_requirements = JobRequirements.objects.create(
            company=cls.company1,
            remote=True,
            hybrid=True,
            days_and_hours={
                'MON': ('1000', '1400'),
                'WED': ('1000', '1400'),
                'FRI': ('1000', '1400'),
            },
            start_date_earliest=date.today() + timedelta(weeks=52),
            start_date_latest=date.today() + timedelta(weeks=104),
            maximum_commute=1,
            relocate=True,
            maximum_relocation_distance=0,
            distance_measurement='km',
            relocation_assistance_amount=Money(50_000, 'EUR'),
            pay_low=Money(150_000, 'EUR'),
            pay_high=Money(200_000, 'EUR'),
            position_availability_start_date=date.today() + timedelta(weeks=3),
            position_availability_end_date=date.today() + timedelta(weeks=4),
        )
        jr.work_tasks.add(
            WorkTask.objects.create(
                name='test work task 1',
                description='test work task 1 description',
            ),
            WorkTask.objects.create(
                name='test work task 2',
                description='test work task 2 description',
            ),
        )
        jr.job_locations.add(
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
        jr.industries_available.add(
            Industry.objects.create(
                name='test industry 1',
            ),
            Industry.objects.create(
                name='test industry 2',
            ),
        )
        jr.career_fields_available.add(
            CareerField.objects.create(
                name='test career field 1',
            ),
            CareerField.objects.create(
                name='test career field 2',
            ),
        )
        cf1, cf2 = jr.career_fields_available.all()
        jr.career_subfields_available.add(
            CareerSubfield.objects.create(
                career_field=cf1,
                name='test career subfield 1',
            ),
            CareerSubfield.objects.create(
                career_field=cf1,
                name='test career subfield 2',
            ),
            CareerSubfield.objects.create(
                career_field=cf2,
                name='test career subfield 3',
            ),
            CareerSubfield.objects.create(
                career_field=cf2,
                name='test career subfield 4',
            ),
        )
        jr.save()
        jr.skills.add(
            Skill.objects.create(
                name='test skill 1',
                hard=False,
            ),
            through_defaults={
                'level': 5,
                'required': True,
            },
        )
        jr.skills.add(
            Skill.objects.create(
                name='test skill 2',
                hard=True,
            ),
            through_defaults={
                'level': 3,
                'required': False,
            },
        )
        jr.traits.add(
            Trait.objects.create(
                name='test trait 1',
            ),
            through_defaults={
                'level': 5,
                'required': True,
            },
        )
        jr.traits.add(
            Trait.objects.create(
                name='test trait 2',
            ),
            through_defaults={
                'level': 3,
                'required': False,
            },
        )
        jr.save()


    def test_matches_no_users_on_initial_setup(self):
        company1 = self.company1

        matches = Match.find_exact(company=company1)
        self.assertEqual(len(matches), 0)


    def test_can_match_by_remote(self):
        user1 = self.user1
        company1 = self.company1

        user1.preferences.remote = True
        user1.preferences.save()

        matches = Match.find_exact(company=company1)
        self.assertEqual(matches, [user1])


    def test_can_match_by_hybrid(self):
        user2 = self.user2
        company1 = self.company1

        user2.preferences.hybrid = True
        user2.preferences.save()

        matches = Match.find_exact(company=company1)
        self.assertEqual(matches, [user2])


    def test_can_match_by_days_and_hours(self):
        user1 = self.user1
        company1 = self.company1

        user1.preferences.days_and_hours = {
            'MON': ('1000', '1400'),
            'WED': ('1000', '1400'),
            'FRI': ('1000', '1400'),
        }
        user1.preferences.save()

        matches = Match.find_exact(company=company1)
        self.assertEqual(matches, [user1])

    def test_can_match_by_start_date(self):
        user2 = self.user2
        company1 = self.company1

        user2.preferences.start_date = date.today() + timedelta(weeks=78)
        user2.preferences.save()

        matches = Match.find_exact(company=company1)
        self.assertEqual(matches, [user2])
