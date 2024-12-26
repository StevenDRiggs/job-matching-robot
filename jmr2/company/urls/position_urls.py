from django.urls import path

from company.views import (
    PositionDetailView,
    PositionIndexView,
)


app_name = 'position'
urlpatterns = [
    path('<int:pk>/', PositionDetailView.as_view(), name='position-detail'),
    path('', PositionIndexView.as_view(), name='positions-index'),
]
