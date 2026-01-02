from domain.entities.company import Company
from domain.entities.product import Product

class InventoryItem:
    def __init__(self, company: Company, product: Product):
        if company is None:
            raise ValueError("Inventory item must belong to a company")
        if product is None:
            raise ValueError("Inventory item must have a product")
        
        self.company = company
        self.product = product
