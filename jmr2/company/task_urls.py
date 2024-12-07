from django.urls import path

from .views import (
    TaskDetailView,
    TaskIndexView,
)


app_name = 'task'
urlpatterns = [
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('', TaskIndexView.as_view(), name='tasks-index'),
]
