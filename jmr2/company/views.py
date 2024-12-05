from django.views import generic

from .models import Company, Position


class CompanyIndexView(generic.ListView):
    model = Company
    context_object_name = 'companies'

class CompanyDetailView(generic.DetailView):
    model = Company


class PositionIndexView(generic.ListView):
    model = Position
    context_object_name = 'positions'

class PositionDetailView(generic.DetailView):
    model = Position
