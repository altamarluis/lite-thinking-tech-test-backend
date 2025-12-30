from django.urls import path
from .views import (
    CompanyListCreateView,
    ProductListCreateView,
    InventoryListCreateView,
    InventoryPDFView,
    SendEmailView,
)

urlpatterns = [
    path("companies/", CompanyListCreateView.as_view()),
    path("products/", ProductListCreateView.as_view()),
    path("inventory/", InventoryListCreateView.as_view()),
    path("inventory/pdf/", InventoryPDFView.as_view()),
    path("email/send/", SendEmailView.as_view()),
]
