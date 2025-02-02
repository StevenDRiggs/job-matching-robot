from django.views import generic

from company.models import Position


class PositionIndexView(generic.ListView):
    model = Position
    context_object_name = 'positions'

class PositionDetailView(generic.DetailView):
    model = Position
