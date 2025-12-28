class Product:
    def __init__(self, code: str, name: str, features: str, prices: dict):
        if not code:
            raise ValueError("Product code is required")

        self.code = code
        self.name = name
        self.features = features
        self.prices = prices  # {"COP": 10000, "USD": 3}
