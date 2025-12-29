"""
URL configuration for config project.

"""
from django.contrib import admin
from django.urls import path, include
from core.views import HealthCheckView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("api/auth/token/", TokenObtainPairView.as_view()),
    path("api/auth/token/refresh/", TokenRefreshView.as_view()),
    
    path('admin/', admin.site.urls),
    path("health/", HealthCheckView.as_view()),
    path("api/", include("core.urls")),
]
