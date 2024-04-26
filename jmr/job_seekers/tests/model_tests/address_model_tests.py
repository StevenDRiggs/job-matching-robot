import json

from django.db.utils import IntegrityError
from django.test import TestCase

from job_seekers.models import (
    Address,
    User,
)


class AddressModelTests(TestCase):
    def test_can_create_address_with_minimal_args(self):
        user = User.objects.create(
            full_name_original='test user',
            sort_by=json.dumps(['user', 'test']),
        )
        address = Address.objects.create(
            street_address='test street address',
            city='test city',
            country='test country',
            user=user,
        )
        self.assertEqual(len(Address.objects.all()), 1)

    def test_can_create_address_with_all_args(self):
        user = User.objects.create(
            full_name_original='test user',
            sort_by=json.dumps(['user', 'test']),
        )
        address = Address.objects.create(
            street_address='test street address',
            city='test city',
            county='test county',
            state='test state',
            country='test country',
            user=user,
        )
        self.assertEqual(len(Address.objects.all()), 1)

    def test_cannot_create_address_without_user(self):
        address = Address(
            street_address='test street address',
            city='test city',
            country='test country',
        )
        self.assertRaises(IntegrityError, address.save)
