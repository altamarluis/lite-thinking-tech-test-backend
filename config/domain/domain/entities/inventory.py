from domain.entities.company import Company
from domain.entities.product import Product

class InventoryItem:
    """
    Domain entity that represents a product assigned to a company inventory.
    """

    def __init__(self, company: Company, product: Product):
        """
        Initializes an InventoryItem entity.

        Args:
            company (Company): Company that owns the product.
            product (Product): Product stored in inventory.

        Raises:
            ValueError: If company or product is not provided.
        """

        if company is None:
            raise ValueError("Inventory item must belong to a company")
        if product is None:
            raise ValueError("Inventory item must have a product")
        
        self.company = company
        self.product = product
        