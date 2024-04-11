from django.db import models


class WorkTask(models.Model):
    name = models.CharField()
    description = models.TextField()
