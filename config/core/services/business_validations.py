from domain.entities.company import Company
from domain.entities.product import Product
from domain.entities.inventory import InventoryItem
from core.models import InventoryItemModel


def validate_company(data: dict):
    Company(**data)


def validate_product(data: dict):
    Product(
        code=data["code"],
        name=data["name"],
        features=data.get("features", ""),
        prices=data["prices"],
    )


def validate_inventory(company, product):
    InventoryItem(company=company, product=product)

    exists = InventoryItemModel.objects.filter(
        company=company,
        product=product,
    ).exists()

    if exists:
        raise ValueError("Product already exists in inventory for this company")
