from django.db import models

from hiring_companies.models import Company
from job_seekers.models import User


class Match(models.Model):
    hiring_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def find(cls, *, company=None, user=None):
        if company and user:
            return [Match.objects.create(hiring_company=company, job_seeker=user)]
        elif company:
            users = []
            users_by_remote = User.objects.filter(preferences__remote=company.job_requirements.remote)
            users.append(*users_by_remote)
            users_by_hybrid = User.objects.filter(preferences__hybrid=company.job_requirements.hybrid)
            users.append(*users_by_hybrid)
            for user_ in set(users):
                Match.objects.create(hiring_company=company, job_seeker=user_)
            return list(Match.objects.filter(hiring_company=company))

