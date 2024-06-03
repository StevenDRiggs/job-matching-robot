import googlemaps

from datetime import date
from django.conf import settings
from django.db import models
from django.db.models import Q
from dotenv import dotenv_values

from hiring_companies.models import Company
from job_seekers.models import Address, User


GMAK = dotenv_values(f'{settings.BASE_DIR}/.env')['GOOGLE_MAPS_API_KEY']
gmaps_client = googlemaps.Client(GMAK)


class Match(models.Model):
    hiring_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def find_exact(cls, *, company=None, user=None):
        if company and user:
            return [Match.objects.create(hiring_company=company, job_seeker=user)]
        elif company:
            users_to_check = User.objects.filter(
                Q(preferences__start_search_date__lte=date.today()),
                Q(preferences__end_search_date__isnull=True) | Q(preferences__end_search_date__gte=date.today()),
            )

            users_by_remote = users_to_check.filter(preferences__remote=company.job_requirements.remote)

            users_by_hybrid = users_to_check.filter(preferences__hybrid=company.job_requirements.hybrid)

            users_by_days_and_hours = users_to_check.filter(preferences__days_and_hours=company.job_requirements.days_and_hours)

            users_by_start_date = users_to_check.filter(
                preferences__start_date__gte=company.job_requirements.start_date_earliest,
                preferences__start_date__lte=company.job_requirements.start_date_latest,
            )

            users_by_commute = []
            for user in users_to_check:
                user_gaddrs = [address.gaddr for address in user.addresses.all()]
                job_location_gaddrs = [job_location.gaddr for job_location in company.job_requirements.job_locations.all()]
                gmaps_distance_matrix = gmaps_client.distance_matrix(user_gaddrs, job_location_gaddrs)
                distances = [gmaps_distance_matrix['rows'][i]['elements'][j]['distance']['value'] for i in range(len(user_gaddrs)) for j in range(len(job_location_gaddrs))]
                if not user.preferences.relocate:
                    if company.job_requirements.distance_measurement == 'km':
                        if any([distance <= company.job_requirements.maximum_commute * 1000 for distance in distances]):
                            users_by_commute.append(user)
                    elif company.job_requirements.distance_measurement == 'mi':
                        if any([distance * 0.000621371 <= company.job_requirements.maximum_commute for distance in distances]):
                            users_by_commute.append(user)
                else:  # user.preferences.relocate == True
                    if company.job_requirements.distance_measurement == 'km' and user.preferences.distance_measurement == 'km':
                        if any([distance - min(company.job_requirements.maximum_relocation_distance * 1000, user.preferences.maximum_relocation_distance * 1000) <= company.job_requirements.maximum_commute * 1000 for distance in distances]):
                            users_by_commute.append(user)
                    elif company.job_requirements.distance_measurement == 'km' and user.preferences.distance_measurement == 'mi':
                        if any([distance - min(company.job_requirements.maximum_relocation_distance * 1000, user.preferences.maximum_relocation_distance * 0.000621371) <= company.job_requirements.maximum_commute for distance in distances]):
                            user_by_commute.append(user)
                    elif company.job_requirements.distance_measurement == 'mi' and user.preferences.distance_measurement == 'km':
                        if any([distance - min(company.job_requirements.maximum_relocation_distance * 0.000621371, user.preferences.maximum_relocation_distance * 1000) <= company.job_requirements.maximum_relocation_distance * 0.000621371 for distance in distances]):
                            users_by_commute.append(user)
                    elif company.job_requirements.distance_measurement == 'mi' and user.preferences.distance_measurement == 'mi':
                        if any([distance - min(company.job_requirements.maximum_relocation_distance * 0.000621371, user.preferences.maximum_relocation_distance * 0.000621371) <= company.job_requirements.maximum_commute * 0.000621371 for distance in distances]):
                            users_by_commute.append(user)
            # users_by_pay
            # users_by_work_task

            users = [*users_by_remote, *users_by_hybrid, *users_by_days_and_hours, *users_by_start_date, *users_by_commute]

            for user in set(users):
                Match.objects.create(hiring_company=company, job_seeker=user)
            return [match.job_seeker for match in Match.objects.filter(hiring_company=company)]

