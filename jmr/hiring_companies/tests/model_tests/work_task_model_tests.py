from django.test import TestCase

from hiring_companies.models import WorkTask


class WorkTaskModelTests(TestCase):
    def test_can_create_work_task(self):
        work_task = WorkTask.objects.create(name='test work task', description='test work description')
        self.assertEqual(len(WorkTask.objects.all()), 1)
