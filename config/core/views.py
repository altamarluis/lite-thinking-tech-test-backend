from django.shortcuts import render
from django.http import FileResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsAdminOrReadOnly
from .models import CompanyModel, ProductModel, InventoryItemModel
from .serializers import (
    CompanySerializer,
    ProductSerializer,
    InventoryItemSerializer,
)
from .services.pdfgenerator import generate_inventory_pdf

class HealthCheckView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({"status": "ok"})

class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class InventoryListCreateView(generics.ListCreateAPIView):
    queryset = InventoryItemModel.objects.select_related("company", "product")
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]

class InventoryPDFView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        inventory = InventoryItemModel.objects.select_related(
            "company", "product"
        )
        pdf_buffer = generate_inventory_pdf(inventory)
        return FileResponse(pdf_buffer, as_attachment=True, filename="inventory.pdf")