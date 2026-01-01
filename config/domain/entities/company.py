class Company:
    def __init__(self, nit: str, name: str, address: str, phone: str):
        if not nit:
            raise ValueError("NIT is required")
        if not name:
            raise ValueError("Company name is required")

        self.nit = nit
        self.name = name
        self.address = address
        self.phone = phone
