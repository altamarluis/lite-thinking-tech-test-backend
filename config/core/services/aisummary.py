import os
from typing import Iterable
from huggingface_hub import InferenceClient
from core.models import InventoryItemModel

def generate_inventory_summary() -> str:
    """
    Generates a concise natural-language summary of the inventory using an AI model.

    Inventory data is transformed into a plain-text prompt and sent to a
    Hugging Face-hosted LLM (DeepSeek). The model is instructed to strictly
    summarize provided data without hallucinating information.

    Returns:
        str: AI-generated inventory summary or a user-friendly fallback message.
    """

    try:
        inventory = InventoryItemModel.objects.select_related("company", "product")
        
        if not inventory.exists():
            return "The inventory is currently empty."
        
        text = "\n".join(
            f"Company: {item.company.name}, "
            f"Product: {item.product.name}, "
            f"Prices: {', '.join(f'{k}: ${v}' for k, v in item.product.prices.items())}"
            for item in inventory
        )
        
        prompt = (
            "You are summarizing inventory data.\n"
            "Rules:\n"
            "- Do not invent information\n"
            "- Do not mention platforms, quantities, or sales channels\n"
            "- Only use the data provided\n"
            "- Provide a concise summary in 2-3 sentences\n\n"
            "Inventory data:\n"
            f"{text}\n\n"
            "Summary:"
        )

        api_key = os.getenv("HF_API_KEY")
        if not api_key:
            return "AI summary service is not configured."
        
        client = InferenceClient(api_key=api_key)
        
        completion = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3.2:novita",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.7
        )
        
        return completion.choices[0].message.content.strip()
        
    except Exception as e:
        # Fail gracefully: AI feature must never break core functionality
        return f"Error generating summary: {str(e)}"