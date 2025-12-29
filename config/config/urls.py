"""
URL configuration for config project.

"""
from django.contrib import admin
from django.urls import path, include
from core.views import HealthCheckView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("health/", HealthCheckView.as_view()),
    path("api/", include("core.urls")),
]
