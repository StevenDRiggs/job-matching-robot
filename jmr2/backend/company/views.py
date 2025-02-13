from django.core import serializers
from django.http import JsonResponse

from .models import *


def benefits_index(req):
    benefits = serializers.serialize('json', Benefit.objects.all())

    return JsonResponse(benefits, safe=False)

def benefit_page(req, pk):
    benefit = serializers.serialize('json', Benefit.objects.filter(pk=pk))

    return JsonResponse(benefit, safe=False)


def companies_index(req):
    companies = serializers.serialize('json', Company.objects.all())

    return JsonResponse(companies, safe=False)

def company_page(req, pk):
    company = serializers.serialize('json', Company.objects.filter(pk=pk))

    return JsonResponse(company, safe=False)
