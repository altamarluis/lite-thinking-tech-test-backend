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
    path("api/auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    
    path('admin/', admin.site.urls),
    path("health/", HealthCheckView.as_view()),
    path("api/", include("core.urls")),
]
