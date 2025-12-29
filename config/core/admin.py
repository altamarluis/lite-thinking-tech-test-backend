from django.contrib import admin
from .models import CompanyModel, ProductModel, InventoryItemModel

admin.site.register(CompanyModel)
admin.site.register(ProductModel)
admin.site.register(InventoryItemModel)
