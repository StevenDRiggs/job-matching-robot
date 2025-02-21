from datetime import datetime
from uuid import uuid4

from django.db import models


class Company(models.Model):
    name = models.CharField()
    company_id = models.UUIDField(default=uuid4 , editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'companies'
