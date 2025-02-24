"""
URL configuration for jmr2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('benefits/', include('company.urls.benefits_urls')),
    path('companies/', include('company.urls.companies_urls')),
    path('positions/', include('company.urls.positions_urls')),
    path('skills/', include('company.urls.skills_urls')),
    path('tasks/', include('company.urls.tasks_urls')),
    path('traits/', include('company.urls.traits_urls')),
    path('admin/', admin.site.urls),
]
