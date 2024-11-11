from django.views import generic

from .models import Company


class CompanyIndexView(generic.ListView):
    model = Company
    context_object_name = 'companies'


class CompanyDetailView(generic.DetailView):
    model = Company
