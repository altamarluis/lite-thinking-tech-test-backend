import os
from huggingface_hub import InferenceClient
from core.models import InventoryItemModel

def generate_inventory_summary():
    """
    Genera un resumen del inventario utilizando DeepSeek-V3 a través de Hugging Face.
    """
    try:
        # Obtener datos del inventario
        inventory = InventoryItemModel.objects.select_related("company", "product")
        
        if not inventory.exists():
            return "The inventory is currently empty."
        
        # Construir texto del inventario
        text = "\n".join(
            f"Company: {item.company.name}, "
            f"Product: {item.product.name}, "
            f"Prices: {', '.join(f'{k}: ${v}' for k, v in item.product.prices.items())}"
            for item in inventory
        )
        
        # Crear prompt
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
        
        # Inicializar cliente
        client = InferenceClient(
            api_key = os.environ.get("HF_API_KEY")
        )
        
        # Hacer la petición
        completion = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3.2:novita",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=200,
            temperature=0.7
        )
        
        # Extraer y devolver el resumen
        return completion.choices[0].message.content.strip()
        
    except Exception as e:
        return f"Error generating summary: {str(e)}"