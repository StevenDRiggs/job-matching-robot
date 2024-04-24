from django.test import TestCase

from job_seekers.models import WorkTask


class WorkTaskModelTests(TestCase):
    def test_can_create_work_task(self):
        work_task = WorkTask(name='test work task', description='test work description')
        work_task.save()
        self.assertEqual(len(WorkTask.objects.all()), 1)
