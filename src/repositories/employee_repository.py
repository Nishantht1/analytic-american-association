import re
from models.address import Address
from models.employee import Employee

EMPLOYEE_FILE_PATH = "storage/employees.txt"




class  EmployeeRepository:
    

    def append(self, employee):
        with open(EMPLOYEE_FILE_PATH, 'a', encoding='utf-8') as file:
            file.write(f"{employee.employee_id}|{employee.employee_name}|{employee.std_bill_rate}|"
                       f"{employee.address.mail_id}|{employee.address.phone_number}|"
                       f"{employee.address.house_no}|{employee.address.building_number}|"
                       f"{employee.address.road_number}|{employee.address.street_name}|"
                       f"{employee.address.land_mark}|{employee.address.city}|"
                       f"{employee.address.state}|{employee.address.zip_code}\n")

    def load_all(self):
        try:
            employees = []
            with open(EMPLOYEE_FILE_PATH, 'r', encoding='utf-8') as file:
                for line in file:
                    parts = line.strip().split('|')
                    if len(parts) != 13:
                        continue  # Skip malformed lines
                    employee_id = parts[0]
                    employee_name = parts[1]
                    std_bill_rate = float(parts[2])
                    address = Address(
                        mail_id=parts[3],
                        phone_number=parts[4],
                        house_no=parts[5],
                        building_number=parts[6],
                        road_number=parts[7],
                        street_name=parts[8],
                        land_mark=parts[9],
                        city=parts[10],
                        state=parts[11],
                        zip_code=parts[12]
                    )
                    employee = Employee(employee_id, employee_name, std_bill_rate, address)
                    employees.append(employee)
            
        except FileNotFoundError:
            pass
        return employees
    
    def save_all(self, employees):
        with open(EMPLOYEE_FILE_PATH, 'w', encoding='utf-8') as file:
            for employee in employees:
                file.write(f"{employee.employee_id}|{employee.employee_name}|{employee.std_bill_rate}|"
                           f"{employee.address.mail_id}|{employee.address.phone_number}|"
                           f"{employee.address.house_no}|{employee.address.building_number}|"
                           f"{employee.address.road_number}|{employee.address.street_name}|"
                           f"{employee.address.land_mark}|{employee.address.city}|"
                           f"{employee.address.state}|{employee.address.zip_code}\n")