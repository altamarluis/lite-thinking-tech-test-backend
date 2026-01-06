from rest_framework import serializers
from .models import CompanyModel, ProductModel, InventoryItemModel
from core.services.business_validations import (
    validate_company,
    validate_product,
    validate_inventory,
)

class CompanySerializer(serializers.ModelSerializer):
    """
    Serializer for CompanyModel with domain-level validation.
    """

    class Meta:
        model = CompanyModel
        fields = "__all__"

    def validate(self, data):
        """
        Applies business validation rules for company data.
        """
        validate_company(data)
        return data


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for ProductModel with domain-level validation.
    """

    class Meta:
        model = ProductModel
        fields = ["code", "name", "features", "prices"]

    def validate(self, data):
        """
        Applies business validation rules for product data.
        """
        validate_product(data)
        return data

class InventoryItemSerializer(serializers.ModelSerializer):
    """
    Serializer for InventoryItemModel.

    Allows creation of inventory items by providing company NIT
    and product code instead of full nested objects.
    """

    company = CompanySerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    company_nit = serializers.CharField(write_only=True)
    product_code = serializers.CharField(write_only=True)

    class Meta:
        model = InventoryItemModel
        fields = [
            "company",
            "product",
            "company_nit",
            "product_code",
        ]

    def validate(self, data):
        """
        Validates inventory business rules before creation.
        """
        try:
            company = CompanyModel.objects.get(nit=data["company_nit"])
        except CompanyModel.DoesNotExist:
            raise serializers.ValidationError("Company not found")

        try:
            product = ProductModel.objects.get(code=data["product_code"])
        except ProductModel.DoesNotExist:
            raise serializers.ValidationError("Product not found")
        
        validate_inventory(company, product)
        
        data["company"] = company
        data["product"] = product
        return data

    def create(self, validated_data):
        """
        Creates an InventoryItemModel from company NIT and product code.
        """
        validated_data.pop("company_nit")
        validated_data.pop("product_code")

        return InventoryItemModel.objects.create(
            company=validated_data["company"],
            product=validated_data["product"]
        )
