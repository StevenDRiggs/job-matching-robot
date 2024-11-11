from django.urls import path

from .views import CompanyDetailView, CompanyIndexView


app_name = 'company'
urlpatterns = [
    path('<int:pk>/', CompanyDetailView.as_view(), name='company_detail'),
    path('', CompanyIndexView.as_view(), name='companies_index'),
]
