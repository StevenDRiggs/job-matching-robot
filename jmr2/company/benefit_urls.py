from django.urls import path

from .views import (
    BenefitDetailView,
    BenefitIndexView,
)


app_name = 'benefit'
urlpatterns = [
    path('<int:pk>/', BenefitDetailView.as_view(), name='benefit-detail'),
    path('', BenefitIndexView.as_view(), name='benefits-index'),
]
