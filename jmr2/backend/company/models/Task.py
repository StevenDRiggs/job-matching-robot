from django.db import models


class Task(models.Model):
    tag = models.CharField()
    description = models.TextField()

    @property
    def stub(self):
        return '-'.join(self.tag.strip().lower().replace(r'[^a-z -]', '').split())

    def __str__(self):
        return self.tag
