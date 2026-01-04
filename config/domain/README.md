# Domain Layer

This package contains the **business domain entities** for the inventory
management system, following **Clean Architecture principles**.

## Purpose

The domain layer defines the core business rules and entities, completely
independent from frameworks, databases, or external services.

It must NOT depend on:
- Django
- Django REST Framework
- HTTP logic
- Serializers or Views

## Entities

- **Company**
  - Represents a company that owns products.
  - Validates NIT and required attributes.

- **Product**
  - Represents a product with prices in multiple currencies.
  - Ensures valid pricing rules.

- **InventoryItem**
  - Represents the relationship between a company and a product.

## Installation

This package is managed using **Poetry** and consumed by the Django backend.

Build the package:

```bash
poetry build
```

Install it in the backend:
```bash
pip install dist/domain-0.1.0-py3-none-any.whl
```

## Design Decisions

- Business validations live in the domain, not in the ORM.
- Entities are pure Python objects.
- Persistence and framework concerns are handled by the backend layer.

This separation improves testability, maintainability, and clarity of the system.
