from django.test import TestCase

from job_seekers.models import Skill


class SkillModelTests(TestCase):
    def test_can_create_hard_skill(self):
        hard_skill = Skill(name='hard skill test', hard=True)
        hard_skill.save()
        self.assertEqual(len(Skill.objects.all()), 1)

    def test_can_create_soft_skill(self):
        soft_skill = Skill(name='soft skill test', hard=False)
        soft_skill.save()
        self.assertEqual(len(Skill.objects.all()), 1)
