from datetime import datetime
from io import BytesIO
from typing import Iterable

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, grey

from core.models import InventoryItemModel


def generate_inventory_pdf(
    inventory_items: Iterable[InventoryItemModel],
) -> BytesIO:
    """
    Generates a PDF report containing inventory information.

    The report includes company name, product name, and product prices
    per currency. The PDF is generated in-memory for download or email
    attachment purposes.

    Args:
        inventory_items (Iterable[InventoryItemModel]):
            Collection of inventory items with related company and product.

    Returns:
        BytesIO: In-memory PDF file ready to be returned or sent via email.
    """

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Margins
    x_margin = 2 * cm
    y_margin = 2 * cm
    y = height - y_margin

    # Header
    p.setFont("Helvetica-Bold", 16)
    p.drawString(x_margin, y, "Inventory Report")
    y -= 20

    p.setFont("Helvetica", 9)
    p.drawString(
        x_margin,
        y,
        f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    )
    y -= 30

    # Divider
    p.setStrokeColor(grey)
    p.line(x_margin, y, width - x_margin, y)
    y -= 20

    # Table header
    p.setFont("Helvetica-Bold", 10)
    p.setFillColor(black)
    p.drawString(x_margin, y, "Company")
    p.drawString(x_margin + 160, y, "Product")
    p.drawString(x_margin + 330, y, "Prices")
    y -= 15

    p.line(x_margin, y, width - x_margin, y)
    y -= 15

    # Table rows
    p.setFont("Helvetica", 9)

    for item in inventory_items:
        prices_str = ", ".join(
            f"{currency}: {price}"
            for currency, price in item.product.prices.items()
        )

        p.drawString(x_margin, y, item.company.name)
        p.drawString(x_margin + 160, y, item.product.name)
        p.drawString(x_margin + 330, y, prices_str)
        y -= 15

        if y < y_margin:
            p.showPage()
            y = height - y_margin

            # Re-draw table header on new page
            p.setFont("Helvetica-Bold", 10)
            p.drawString(x_margin, y, "Company")
            p.drawString(x_margin + 160, y, "Product")
            p.drawString(x_margin + 330, y, "Prices")
            y -= 15
            p.line(x_margin, y, width - x_margin, y)
            y -= 15
            p.setFont("Helvetica", 9)

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer
