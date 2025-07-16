from django.db import models

from .Position import Position


class Benefit(models.Model):
    tag = models.CharField()
    description = models.TextField()

    @property
    def stub(self):
        return '-'.join(self.tag.strip().lower().replace(r'[^a-z -]', '').split())

    def __str__(self):
        return self.tag

class BenefitAvailable(models.Model):
    benefit = models.ForeignKey(Benefit, models.CASCADE, related_name='benefits_available')
    position = models.ForeignKey(Position, models.CASCADE, related_name='benefits_available')

    available = models.CharField()  # use for 'after 30 days', e.g.

    class Meta:
        verbose_name_plural = 'benefits available'
