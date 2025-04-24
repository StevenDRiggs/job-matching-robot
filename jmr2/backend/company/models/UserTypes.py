from django.contrib.auth.models import User
from django.db import models

from .Company import Company


class CompanyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
