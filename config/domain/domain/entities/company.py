class Company:
    def __init__(self, nit: str, name: str, address: str, phone: str):
        if not nit or len(nit) < 5:
            raise ValueError("NIT inválido")
        if not name:
            raise ValueError("Company name is required")

        self.nit = nit
        self.name = name
        self.address = address
        self.phone = phone
