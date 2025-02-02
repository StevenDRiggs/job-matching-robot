from django.views import generic

from company.models import Task


class TaskIndexView(generic.ListView):
    model = Task
    context_object_name = 'tasks'

class TaskDetailView(generic.DetailView):
    model = Task
