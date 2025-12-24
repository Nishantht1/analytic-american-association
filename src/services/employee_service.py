from models.employee import Employee
from utils.csv_utils import read_csv_rows
from models.address import Address
import csv


class EmployeeService:
    def __init__(self, repo):
        self.repo= repo

    def bulk_import_employees_from_csv(self, csv_path="storage/csv/employees.csv"):
        
        success = 0
        failed = 0

        with open(csv_path, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)

            for row in reader:
                try:
                    employee_id = self.generate_employee_id()
                    employee_name = row["Employee Name"].strip()
                    srate_raw = (row.get("Standart Bill Rate") or "").strip()
                    rate_clean = srate_raw.replace("$", "").replace(",", "").strip()
                    std_bill_rate = float(rate_clean) if rate_clean else 0.0

                    address = Address(
                        mail_id=row["Mail Id"].strip(),
                        phone_number=row["Phone Number"].strip(),
                        house_no=row["House Number"].strip(),
                        building_number=row["Building Number"].strip(),
                        road_number=row["Road Number"].strip(),
                        street_name=row["Steet Name"].strip(),
                        land_mark=row["Landmark"].strip(),
                        city=row["City"].strip(),
                        state=row["State"].strip(),
                        zip_code=row["Zip Code"].strip(),
                    )

                    emp = Employee(employee_id, employee_name, std_bill_rate, address)
                    self.repo.append(emp)
                    success += 1

                except Exception as e:
                    failed += 1
                    print(f"[EMP CSV ERROR] {e} | Row={row}")

        print(f"Employee CSV Import Done → Success: {success}, Failed: {failed}")


    def generate_employee_id(self):
        employees = self.repo.load_all()
        max_num = max([int(emp.employee_id.split("_")[1]) for emp in employees], default=0)
        next_num=max_num+1
        return f"EMP_{next_num:06d}"

    def create_employee(self,address):
        try:
            employee_id = self.generate_employee_id()
            employee_name = input("Enter Employee Name: ")
            std_bill_rate = float(input("Enter Standard Bill Rate: "))
            employee = Employee(employee_id, employee_name, std_bill_rate, address)
            self.repo.append(employee)
            print(f"Employee created successfully: {employee_id}")
        except ValueError as ve:
            print(f"Error creating employee: {ve}")   
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def search_employee(self, employee_id):
        employee_id = employee_id.strip()
        employees = self.repo.load_all()

        for emp in employees:
            if emp.employee_id == employee_id:
                print("Employee Found:")
                print(f"Employee ID   : {emp.employee_id}")
                print(f"Name          : {emp.employee_name}")
                print(f"Std Bill Rate : {emp.std_bill_rate}")
                print("Address:")
                print(f"  Mail ID      : {emp.address.mail_id}")
                print(f"  Phone        : {emp.address.phone_number}")
                print(f"  House No     : {emp.address.house_no}")
                print(f"  Building No  : {emp.address.building_number}")
                print(f"  Road No      : {emp.address.road_number}")
                print(f"  Street Name  : {emp.address.street_name}")
                print(f"  Landmark     : {emp.address.land_mark}")
                print(f"  City         : {emp.address.city}")
                print(f"  State        : {emp.address.state}")
                print(f"  Zip Code     : {emp.address.zip_code}")
                return emp

        print("Employee not found.")
        return None

        

    def list_employees(self):
        employees = self.repo.load_all()

        if not employees:
            print("No employees are available in the system.")
            return []

        print("Employee List:")
        print("-" * 50)

        for emp in employees:
            print(f"Employee ID   : {emp.employee_id}")
            print(f"Name          : {emp.employee_name}")
            print(f"Std Bill Rate : {emp.std_bill_rate}")
            print("Address:")
            print(f"  Mail ID      : {emp.address.mail_id}")
            print(f"  Phone        : {emp.address.phone_number}")
            print(f"  House No     : {emp.address.house_no}")
            print(f"  Building No  : {emp.address.building_number}")
            print(f"  Road No      : {emp.address.road_number}")
            print(f"  Street Name  : {emp.address.street_name}")
            print(f"  Landmark     : {emp.address.land_mark}")
            print(f"  City         : {emp.address.city}")
            print(f"  State        : {emp.address.state}")
            print(f"  Zip Code     : {emp.address.zip_code}")
            print("-" * 50)

        return employees

        
    def update_employee(self, employee_id):
        employee_id = employee_id.strip()
        employees = self.repo.load_all()

        for emp in employees:
            if emp.employee_id == employee_id:
                print("Current Employee Details:")
                print(f"Employee ID   : {emp.employee_id}")
                print(f"Name          : {emp.employee_name}")
                print(f"Std Bill Rate : {emp.std_bill_rate}")
                print("Address:")
                print(f"  Mail ID      : {emp.address.mail_id}")
                print(f"  Phone        : {emp.address.phone_number}")
                print(f"  House No     : {emp.address.house_no}")
                print(f"  Building No  : {emp.address.building_number}")
                print(f"  Road No      : {emp.address.road_number}")
                print(f"  Street Name  : {emp.address.street_name}")
                print(f"  Landmark     : {emp.address.land_mark}")
                print(f"  City         : {emp.address.city}")
                print(f"  State        : {emp.address.state}")
                print(f"  Zip Code     : {emp.address.zip_code}")

                try:
                    # Update std_bill_rate
                    new_rate = input("Enter new Std Bill Rate (leave blank to keep current): ").strip()
                    if new_rate:
                        emp.std_bill_rate = float(new_rate)
                        emp.validate_std_bill_rate()

                    # Update ALL Address attributes
                    new_mail = input("Enter new Mail ID (leave blank to keep current): ").strip()
                    if new_mail:
                        emp.address.mail_id = new_mail
                        emp.address.validate_mail_id()

                    new_phone = input("Enter new Phone Number (leave blank to keep current): ").strip()
                    if new_phone:
                        emp.address.phone_number = new_phone
                        emp.address.validate_phone_number()

                    new_house = input("Enter new House No (leave blank to keep current): ").strip()
                    if new_house:
                        emp.address.house_no = new_house
                        emp.address.validate_house_no()

                    new_building = input("Enter new Building Number (leave blank to keep current): ").strip()
                    if new_building:
                        emp.address.building_number = new_building
                        emp.address.validate_building_number()

                    new_road = input("Enter new Road Number (leave blank to keep current): ").strip()
                    if new_road:
                        emp.address.road_number = new_road
                        emp.address.validate_road_number()

                    new_street = input("Enter new Street Name (leave blank to keep current): ").strip()
                    if new_street:
                        emp.address.street_name = new_street
                        emp.address.validate_street_name()

                    new_landmark = input("Enter new Landmark (leave blank to keep current): ").strip()
                    if new_landmark:
                        emp.address.land_mark = new_landmark
                        emp.address.validate_land_mark()

                    new_city = input("Enter new City (leave blank to keep current): ").strip()
                    if new_city:
                        emp.address.city = new_city
                        emp.address.validate_city()

                    new_state = input("Enter new State (leave blank to keep current): ").strip()
                    if new_state:
                        emp.address.state = new_state
                        emp.address.validate_state()

                    new_zip = input("Enter new Zip Code (leave blank to keep current): ").strip()
                    if new_zip:
                        emp.address.zip_code = new_zip
                        emp.address.validate_zip_code()

                    self.repo.save_all(employees)
                    print("Employee updated successfully.")

                except ValueError as ve:
                    print(f"Error updating employee: {ve}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

                return

        print("Employee not found.")

        
    def delete_employee(self, employee_id):
        employee_id = employee_id.strip()
        employees = self.repo.load_all()

        for i, emp in enumerate(employees):
            if emp.employee_id == employee_id:
                del employees[i]
                self.repo.save_all(employees)
                print("Employee deleted successfully.")
                return

        print("Employee not found.")

        