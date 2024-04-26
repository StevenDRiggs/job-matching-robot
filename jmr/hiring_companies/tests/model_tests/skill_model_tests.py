from django.test import TestCase

from hiring_companies.models import Skill


class SkillModelTests(TestCase):
    def test_can_create_hard_skill(self):
        hard_skill = Skill.objects.create(name='hard skill test', hard=True)
        self.assertEqual(len(Skill.objects.all()), 1)

    def test_can_create_soft_skill(self):
        soft_skill = Skill.objects.create(name='soft skill test', hard=False)
        self.assertEqual(len(Skill.objects.all()), 1)
