# src/models/client.py

import re
from models.address import Address



class Client:
    def __init__(self, client_id, client_name, client_description, std_bill_rate, address):
        self.client_id = client_id
        self.client_name = client_name
        self.client_description = client_description
        self.std_bill_rate = std_bill_rate
        self.address = address

        self.validate_client_id()
        self.validate_client_name()
        self.validate_client_description()
        self.validate_std_bill_rate()
        self.validate_address()

    def validate_client_id(self):
        if not isinstance(self.client_id, str):
            raise ValueError("Client ID must be a string.")

        cid = self.client_id.strip()
        if len(cid) == 0:
            raise ValueError("Client ID cannot be empty.")

        # Expected format: CLT_###### (6 digits)
        pattern = r"^CLT_\d{6}$"
        if not re.match(pattern, cid):
            raise ValueError("Client ID must be in the format CLT_###### (6 digits).")

        self.client_id = cid

    def validate_client_name(self):
        if not isinstance(self.client_name, str):
            raise ValueError("Client name must be a string.")

        name = self.client_name.strip()
        if len(name) == 0:
            raise ValueError("Client name cannot be empty.")

        # Allowed: alphabets, digits, spaces, '_' and '-'
        pattern = r"^[A-Za-z0-9 _-]+$"
        if not re.match(pattern, name):
            raise ValueError("Client name is invalid (allowed: alphabets, digits, space, '_' and '-').")

        self.client_name = name

    def validate_client_description(self):
        if not isinstance(self.client_description, str):
            raise ValueError("Client description must be a string.")

        desc = self.client_description.strip()
        if len(desc) == 0:
            raise ValueError("Client description cannot be empty.")

        # Allowed: alphabets, digits, spaces, '_' and '-'
        pattern = r"^[A-Za-z0-9 _-]+$"
        if not re.match(pattern, desc):
            raise ValueError("Client description is invalid (allowed: alphabets, digits, space, '_' and '-').")

        self.client_description = desc

    def validate_std_bill_rate(self):
        if not isinstance(self.std_bill_rate, (int, float)):
            raise ValueError("Standard bill rate must be a number.")

        if self.std_bill_rate <= 0:
            raise ValueError("Standard bill rate must be greater than 0.")

    def validate_address(self):
        if not isinstance(self.address, Address):
            raise ValueError("Address must be an instance of Address class.")





