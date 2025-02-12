from django.urls import path

from company.views import (
    CompanyDetailView,
    CompanyIndexView,
)


app_name = 'company'
urlpatterns = [
    path('<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('', CompanyIndexView.as_view(), name='companies-index'),
]
