import json

from django.test import TestCase

from job_seekers.models import (
    Address,
    User,
)


class AddressModelTests(TestCase):
    def test_can_create_address_with_minimal_args(self):
        user = User(
            full_name_original='test user',
            sort_by=json.dumps(['user', 'test']),
        )
        user.save()
        address = Address(
            street_address='test street address',
            city='test city',
            country='test country',
            user=user,
        )
        address.save()
        self.assertEqual(len(Address.objects.all()), 1)

    def test_can_create_address_with_all_args(self):
        user = User(  # TODO: update for full args
            full_name_original='test user',
            sort_by=json.dumps(['user', 'test']),
        )
        user.save()
        address = Address(
            street_address='test street address',
            city='test city',
            county='test county',
            state='test state',
            country='test country',
            user=user,
        )
        address.save()
        self.assertEqual(len(Address.objects.all()), 1)
