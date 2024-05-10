from datetime import date
from django.db import models
from django.db.models import Q

from hiring_companies.models import Company
from job_seekers.models import User


class Match(models.Model):
    hiring_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def find_exact(cls, *, company=None, user=None):
        if company and user:
            return [Match.objects.create(hiring_company=company, job_seeker=user)]
        elif company:
            users = []
            users_to_check = User.objects.filter(
                Q(preferences__start_search_date__lte=date.today),
                Q(preferences__end_search_date__isnull=True) | Q(preferences__end_search_date__gte=date.today()),
            )
            users_by_remote = users_to_check.filter(preferences__remote=company.job_requirements.remote)
            users_by_hybrid = users_to_check.filter(preferences__hybrid=company.job_requirements.hybrid)
            users_by_days_and_hours = users_to_check.filter(preferences__days_and_hours=company.job_requirements.days_and_hours)
            users_by_start_date = users_to_check.filter(
                preferences__start_date__gte=company.job_requirements.start_date_earliest,
                preferences__start_date__lte=company.job_requirements.start_date_latest,
            )
            # Users_by_relocation
            # users_by_pay
            # users_by_work_task

            users.append(*users_by_remote, *users_by_hybrid, *users_by_days_and_hours)

            for user in set(users):
                Match.objects.create(hiring_company=company, job_seeker=user)
            return list(Match.objects.filter(hiring_company=company))

