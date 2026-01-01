from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.colors import black, grey
from datetime import datetime
from io import BytesIO


def generate_inventory_pdf(inventory_items):
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
    p.drawString(x_margin + 200, y, "Product")
    y -= 15

    p.line(x_margin, y, width - x_margin, y)
    y -= 15

    # Table rows
    p.setFont("Helvetica", 9)

    for item in inventory_items:
        p.drawString(x_margin, y, item.company.name)
        p.drawString(x_margin + 200, y, item.product.name)
        y -= 15

        if y < y_margin:
            p.showPage()
            y = height - y_margin

            # Re-draw header on new page
            p.setFont("Helvetica-Bold", 10)
            p.drawString(x_margin, y, "Company")
            p.drawString(x_margin + 200, y, "Product")
            y -= 15
            p.line(x_margin, y, width - x_margin, y)
            y -= 15
            p.setFont("Helvetica", 9)

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer
