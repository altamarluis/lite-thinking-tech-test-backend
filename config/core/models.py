from django.db import models

class CompanyModel(models.Model):
    nit = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    features = models.TextField()
    prices = models.JSONField()  # {"COP": 10000, "USD": 3}

    def __str__(self):
        return self.name


class InventoryItemModel(models.Model):
    company = models.ForeignKey(
        CompanyModel,
        on_delete=models.CASCADE,
        related_name="inventory"
    )
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.CASCADE,
        related_name="inventory_items"
    )

    class Meta:
        unique_together = ("company", "product")

    def __str__(self):
        return f"{self.company} - {self.product}"

