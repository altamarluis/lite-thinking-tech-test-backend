class Product:
    def __init__(self, code: str, name: str, features: str, prices: dict):
        if not code:
            raise ValueError("Product code is required")
        if not name:
            raise ValueError("Product name is required")
        if not prices or not isinstance(prices, dict):
            raise ValueError("Product prices must be a dictionary")

        self.code = code
        self.name = name
        self.features = features
        self.prices = prices  # {"COP": 10000, "USD": 3}
