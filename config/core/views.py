from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CompanyModel, ProductModel, InventoryItemModel
from .serializers import (
    CompanySerializer,
    ProductSerializer,
    InventoryItemSerializer,
)

class HealthCheckView(APIView):
    def get(self, request):
        return Response({"status": "ok"})

class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


class InventoryListCreateView(generics.ListCreateAPIView):
    queryset = InventoryItemModel.objects.select_related("company", "product")
    serializer_class = InventoryItemSerializer