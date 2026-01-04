"""
URL configuration for the Lite Thinking backend project.

Defines global routes for authentication, admin panel,
health checks, and API endpoints.
"""

from django.contrib import admin
from django.urls import path, include
from core.views import HealthCheckView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Authentication (JWT)
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    
    # Django admin
    path('admin/', admin.site.urls),

    # Health check
    path("health/", HealthCheckView.as_view()),

    # Core API
    path("api/", include("core.urls")),
]
