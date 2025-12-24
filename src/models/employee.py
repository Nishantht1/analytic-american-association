import re
from models.address import Address




class Employee:
    def __init__(self, employee_id, employee_name, std_bill_rate, address):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.std_bill_rate = std_bill_rate
        self.address = address

        self.validate_employee_name()
        self.validate_std_bill_rate()       
        self.validate_address()


    

    

    def validate_employee_name(self):
        if isinstance(self.employee_name, str):
            name=self.employee_name.strip()
            pattern=r'^[A-Za-z0-9 _-]+$'
            if len(name)==0:
                raise ValueError("Employee name cannot be empty.")
            elif not re.match(pattern, name):
                raise ValueError("Employee name is invalid.")
        else:
            raise ValueError("Employee name must be a string.")
    
    def validate_std_bill_rate(self):
        if not isinstance(self.std_bill_rate, (int, float)):
            raise ValueError("Standard bill rate must be a number.")
        elif self.std_bill_rate <= 0:
            raise ValueError("Standard bill rate must be greater than 0.")
    
    def validate_address(self):
        if not isinstance(self.address, Address):
            raise ValueError("Address must be an instance of Address class.")
        



                

