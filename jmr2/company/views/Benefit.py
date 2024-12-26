from django.views import generic

from company.models import Benefit


class BenefitIndexView(generic.ListView):
    model = Benefit
    context_object_name = 'benefits'

class BenefitDetailView(generic.DetailView):
    model = Benefit
