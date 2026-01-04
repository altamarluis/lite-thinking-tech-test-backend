import os
import base64
from typing import Optional

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Mail,
    Attachment,
    FileContent,
    FileName,
    FileType,
    Disposition,
)

from core.models import InventoryItemModel
from core.services.pdfgenerator import generate_inventory_pdf

DEFAULT_SUBJECT = "Lite Thinking Inventory Notification"
FOOTER = "\n\n---\nLite Thinking Inventory System"

def send_email(to_email: str) -> None:
    """
    Sends the inventory PDF report as an email attachment.

    The PDF is generated dynamically from current inventory data
    and sent using the SendGrid API.

    Args:
        to_email (str): Recipient email address.

    Raises:
        RuntimeError: If required environment variables are missing.
    """
    if not os.getenv("SENDGRID_API_KEY"):
        raise RuntimeError("SENDGRID_API_KEY is not configured")

    if not os.getenv("EMAIL_FROM"):
        raise RuntimeError("EMAIL_FROM is not configured")

    inventory = InventoryItemModel.objects.select_related("company", "product")
    pdf_buffer = generate_inventory_pdf(inventory)

    encoded_pdf = base64.b64encode(pdf_buffer.read()).decode()

    attachment = Attachment(
        FileContent(encoded_pdf),
        FileName("inventory.pdf"),
        FileType("application/pdf"),
        Disposition("attachment"),
    )

    message = Mail(
        from_email=os.getenv("EMAIL_FROM"),
        to_emails=to_email,
        subject=DEFAULT_SUBJECT,
        plain_text_content=FOOTER,
    )

    message.attachment = attachment

    sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
    sg.send(message)
