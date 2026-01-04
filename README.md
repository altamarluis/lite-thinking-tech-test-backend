# Lite Thinking – Technical Test (Backend)

Inventory management system built as a technical test using **Django, PostgreSQL and React** principles, with clean architecture, PDF generation, email integration and an AI-powered feature.

---

## Tech Stack

**Backend**
- Python 3.12
- Django + Django REST Framework
- PostgreSQL
- JWT Authentication (SimpleJWT)

**Domain**
- Pure Python package
- Managed with Poetry
- Clean Architecture principles

**Integrations**
- PDF generation: ReportLab
- Email service: SendGrid
- AI summary: Hugging Face (DeepSeek)

---

## Architecture Overview

The project follows a **Clean Architecture–inspired separation**:

Backend (Django)
- core
  - views        : API layer (HTTP, permissions)
  - serializers  : Data validation & transformation
  - models       : Persistence (Django ORM)
  - services     : External integrations (PDF, Email, AI)
- domain
  - entities     : Business entities & rules (framework-agnostic)

---

## Features

- Company management (Admin only CRUD)
- Product management with multi-currency pricing
- Inventory per company
- Role-based access (Admin / External user)
- JWT authentication
- Inventory PDF export
- Email delivery of inventory PDF
- AI-generated inventory summary (extra feature)

---

## User Roles

### Administrator
- Create, update and delete companies
- Register products
- Manage inventory per company
- Generate PDFs and send emails

### External User
- View companies
- View products and inventory

---

## Environment Variables

Create a `.env` file:

SECRET_KEY=your-secret-key  
DEBUG=True  

DB_NAME=postgres  
DB_USER=postgres  
DB_PASSWORD=postgres  
DB_HOST=localhost  
DB_PORT=5432  

SENDGRID_API_KEY=your-sendgrid-key  
EMAIL_FROM=your@email.com  

HF_API_KEY=your-huggingface-key  

---

## Installation (Backend)

python -m venv .venv  
source .venv/bin/activate  

pip install -r requirements.txt  

python manage.py migrate  
python manage.py createsuperuser  
python manage.py runserver  

---

## Domain Package

The domain layer is managed independently using Poetry.

cd domain  
poetry build  
pip install dist/domain-0.1.0-py3-none-any.whl  

---

## API Endpoints (Main)

- POST /api/auth/login/
- GET /api/companies/
- POST /api/companies/ (admin)
- GET /api/products/
- POST /api/inventory/
- GET /api/inventory/pdf/
- POST /api/email/send/
- GET /api/inventory/summary/

---

## AI Feature

AI-powered endpoint that generates a natural-language summary of the inventory using a Hugging Face hosted LLM.

---

## Author

Luis Andrés Altamar  
Technical Test – Lite Thinking
