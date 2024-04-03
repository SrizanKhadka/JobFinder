"""
URL configuration for JobFinder project.

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

'''
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
'''

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.contrib import admin 
from authentication.api.views import UserRegistrationAPIView, UserLoginAPIView
from jobs.api.views import *

router = DefaultRouter()
router.register("registration", UserRegistrationAPIView, basename="registration")
router.register("jobs", CreateJobsView, basename="createJobs")
router.register("applications",CreateApplicationsView,basename="applicationsView")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('jobFinder/login/', UserLoginAPIView.as_view(), name='loginView'),
    path("jobFinder/", include(router.urls))
]

