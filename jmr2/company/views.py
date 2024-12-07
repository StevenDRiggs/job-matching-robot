from django.views import generic

from .models import (
    Benefit,
    Company,
    Position,
    Task,
)


class BenefitIndexView(generic.ListView):
    model = Benefit
    context_object_name = 'benefits'

class BenefitDetailView(generic.DetailView):
    model = Benefit


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


class TaskIndexView(generic.ListView):
    model = Task
    context_object_name = 'tasks'

class TaskDetailView(generic.DetailView):
    model = Task


