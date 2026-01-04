from django.contrib import admin

from .models import CompanyModel, ProductModel, InventoryItemModel


@admin.register(CompanyModel)
class CompanyAdmin(admin.ModelAdmin):
    """
    Admin configuration for CompanyModel.
    """

    list_display = ("nit", "name", "phone")
    search_fields = ("nit", "name")


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin configuration for ProductModel.
    """

    list_display = ("code", "name")
    search_fields = ("code", "name")


@admin.register(InventoryItemModel)
class InventoryItemAdmin(admin.ModelAdmin):
    """
    Admin configuration for InventoryItemModel.
    """

    list_display = ("company", "product")
    list_filter = ("company",)
