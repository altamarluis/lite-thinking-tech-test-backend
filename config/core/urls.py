from django.urls import path
from .views import (
    CompanyListCreateView,
    CompanyDetailView,
    ProductListCreateView,
    ProductDetailView,
    InventoryListCreateView,
    InventoryDetailView,
    InventoryByCompanyView,
    ProductsByCompanyView,
    InventoryPDFView,
    SendEmailView,
    InventorySummaryAIView,
)

urlpatterns = [
    # Companies
    path("companies/", CompanyListCreateView.as_view()),
    path("companies/<str:nit>/", CompanyDetailView.as_view()),

    # Products
    path("products/", ProductListCreateView.as_view()),
    path("products/<str:code>/", ProductDetailView.as_view()),

    # Inventory
    path("inventory/", InventoryListCreateView.as_view()),
    path("inventory/<int:pk>/", InventoryDetailView.as_view()),
    path("inventory/company/<str:nit>/", InventoryByCompanyView.as_view()),
    path("products/company/<str:nit>/", ProductsByCompanyView.as_view()),

    # PDF & Email
    path("inventory/pdf/", InventoryPDFView.as_view()),
    path("email/send/", SendEmailView.as_view()),

    # AI
    path("inventory/summary/", InventorySummaryAIView.as_view()),
]
