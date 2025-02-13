from django.core import serializers
from django.http import JsonResponse

from .models import *


def companies_index(req):
    companies = serializers.serialize('json', Company.objects.all())

    return JsonResponse(companies, safe=False)

def company_page(req, pk):
    company = serializers.serialize('json', Company.objects.filter(pk=pk))

    return JsonResponse(company, safe=False)
