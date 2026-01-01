from rest_framework import serializers
from .models import CompanyModel, ProductModel, InventoryItemModel


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ["code", "name", "features", "prices"]


class InventoryItemSerializer(serializers.ModelSerializer):
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

    def create(self, validated_data):
        company_nit = validated_data.pop("company_nit")
        product_code = validated_data.pop("product_code")

        try:
            company = CompanyModel.objects.get(nit=company_nit)
        except CompanyModel.DoesNotExist:
            raise serializers.ValidationError("Company not found")

        try:
            product = ProductModel.objects.get(code=product_code)
        except ProductModel.DoesNotExist:
            raise serializers.ValidationError("Product not found")

        return InventoryItemModel.objects.create(
            company=company,
            product=product
        )
