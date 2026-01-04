class Product:
    """
    Domain entity that represents a product owned by a company.

    Handles basic validation rules related to product identity and pricing.
    """

    def __init__(self, code: str, name: str, features: str, prices: dict):
        """
        Initializes a Product entity.

        Args:
            code (str): Unique product code.
            name (str): Product name.
            features (str): Product characteristics or description.
            prices (dict): Prices by currency (e.g. {"COP": 10000, "USD": 3}).

        Raises:
            ValueError: If required fields are missing or prices are invalid.
        """

        if not code:
            raise ValueError("Product code is required")
        if not name:
            raise ValueError("Product name is required")
        if not prices or not isinstance(prices, dict):
            raise ValueError("Product must have prices by currency")

        for currency, price in prices.items():
            if price < 0:
                raise ValueError(f"Price for {currency} cannot be negative")
            
        self.code = code
        self.name = name
        self.features = features
        self.prices = prices
