class Company:
    """
    Domain entity that represents a company.

    This class contains only business rules and validations,
    independent from persistence or framework concerns.
    """

    def __init__(self, nit: str, name: str, address: str, phone: str):
        """
        Initializes a Company entity.

        Args:
            nit (str): Unique company identifier. Must have at least 5 characters.
            name (str): Company name.
            address (str): Company address.
            phone (str): Company contact phone.

        Raises:
            ValueError: If NIT is invalid or name is missing.
        """

        if not nit or len(nit) < 5:
            raise ValueError("Invalid NIT")
        if not name:
            raise ValueError("Company name is required")

        self.nit = nit
        self.name = name
        self.address = address
        self.phone = phone
