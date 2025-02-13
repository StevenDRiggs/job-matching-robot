from django.core import serializers
from django.http import JsonResponse

from .models import *


def companies_index(req):
    companies = serializers.serialize('json', Company.objects.all())

    return JsonResponse(companies, safe=False)
