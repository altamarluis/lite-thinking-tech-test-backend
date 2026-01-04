from django.http import FileResponse
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
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
from .services.emailsender import send_email
from .services.aisummary import generate_inventory_summary

class HealthCheckView(APIView):
    """
    Simple health check endpoint.
    """

    permission_classes = [AllowAny]
    def get(self, request):
        return Response({"status": "ok"})


class CompanyListCreateView(generics.ListCreateAPIView):
    """
    - GET: List companies (authenticated users)
    - POST: Create company (admin only)
    """

    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    - GET: Retrieve company (admin & user)
    - PUT/PATCH: Update company (admin only)
    - DELETE: Delete company (admin only)
    """
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    lookup_field = "nit"


class ProductListCreateView(generics.ListCreateAPIView):
    """
    - GET: List products (authenticated users)
    - POST: Create product (admin only)
    """

    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    - GET: Retrieve product (admin & user)
    - PUT/PATCH: Update product (admin only)
    - DELETE: Delete product (admin only)
    """

    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    lookup_field = "code"


class InventoryListCreateView(generics.ListCreateAPIView):
    """
    - GET: List inventory items (authenticated users)
    - POST: Add product to inventory (admin only)
    """
   
    queryset = InventoryItemModel.objects.select_related("company", "product")
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

class InventoryDetailView(generics.DestroyAPIView):
    """
    - DELETE: Remove product from inventory (admin only)
    """

    queryset = InventoryItemModel.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class InventoryByCompanyView(generics.ListAPIView):
    """
    - GET: List inventory items by company NIT (admin & user)
    """

    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        nit = self.kwargs["nit"]
        return InventoryItemModel.objects.filter(company__nit=nit).select_related(
            "company", "product"
        )

class ProductsByCompanyView(generics.ListAPIView):
    """
    - GET: List products by company NIT (admin & user)
    """

    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        nit = self.kwargs["nit"]
        return ProductModel.objects.filter(
            inventoryitemmodel__company__nit=nit
        ).distinct()


class InventoryPDFView(APIView):
    """
    Generates and downloads a PDF with the full inventory.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        inventory = InventoryItemModel.objects.select_related(
            "company", "product"
        )
        pdf_buffer = generate_inventory_pdf(inventory)
        return FileResponse(pdf_buffer, as_attachment=True, filename="inventory.pdf")
    
class SendEmailView(APIView):
    """
    Sends the inventory PDF to a given email address.
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):
        email = request.data.get("email")
        if not email:
            return Response(
                {"error": "email is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        send_email(email)
        return Response({"status": "sent"}, status=status.HTTP_200_OK)
    
class InventorySummaryAIView(APIView):
    """
    Returns an AI-generated summary of the inventory.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        summary = generate_inventory_summary()
        return Response({"summary": summary})
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    """
    Returns basic information about the authenticated user.
    """
    return Response({
        'username': request.user.username,
        'is_admin': request.user.is_staff or request.user.is_superuser,
        'user_id': request.user.id
    })