# main.py
# Menu-driven CLI to run: Task, Employee, Client, Timesheet, Billing
# Assumes your project structure like:
#   src/
#     models/ (task.py, employee.py, client.py, address.py, timesheet.py)
#     repositories/ (task_repository.py, employee_repository.py, client_repository.py, timesheet_repository.py)
#     services/ (task_service.py, employee_service.py, client_service.py, timesheet_service.py, billing_service.py)
#   storage/ (tasks.txt, employees.txt, clients.txt, timesheets.txt)
#
# Run from project root:
#   python main.py
#
# If your imports differ, adjust the import lines below accordingly.

import os

# ---------- Imports (adjust if your module paths differ) ----------
from models.address import Address

from repositories.task_repository import TaskRepository
from repositories.employee_repository import EmployeeRepository
from repositories.client_repository import ClientRepository
from repositories.timesheet_repository import TimeSheetRepository

from services.task_service import TaskService
from services.employee_service import EmployeeService
from services.client_service import ClientService
from services.timesheet_service import TimeSheetService
from services.billing_service import BillingService


# ---------- Helpers ----------
def ensure_storage_folder():
    os.makedirs("storage", exist_ok=True)


def input_nonempty(prompt: str) -> str:
    # simple helper to avoid accidental empty input in main menu flows
    value = input(prompt).strip()
    return value

def bulk_import_all(task_service, employee_service, client_service):
    task_service.bulk_import_tasks_from_csv()
    employee_service.bulk_import_employees_from_csv()
    client_service.bulk_import_clients_from_csv()

def create_address_from_user() -> Address:
    """
    Builds an Address object by collecting all required fields.
    Address validates itself in __init__.
    """
    mail_id = input_nonempty("Enter Mail ID: ")
    phone_number = input_nonempty("Enter Phone Number (10 digits or +91XXXXXXXXXX): ")
    house_no = input_nonempty("Enter House No: ")
    building_number = input_nonempty("Enter Building Number: ")
    road_number = input_nonempty("Enter Road Number: ")
    street_name = input_nonempty("Enter Street Name: ")
    land_mark = input_nonempty("Enter Landmark: ")
    city = input_nonempty("Enter City (alphabets only): ")
    state = input_nonempty("Enter State (alphabets only): ")
    zip_code = input_nonempty("Enter Zip Code (digits only): ")

    return Address(
        mail_id=mail_id,
        phone_number=phone_number,
        house_no=house_no,
        building_number=building_number,
        road_number=road_number,
        street_name=street_name,
        land_mark=land_mark,
        city=city,
        state=state,
        zip_code=zip_code,
    )


def pause():
    input("\nPress Enter to continue...")


# ---------- Menus ----------
def task_menu(task_service: TaskService):
    while True:
        print("\n==== TASK MENU ====")
        print("1. Create Task")
        print("2. Search Task")
        print("3. List Tasks")
        print("4. Update Task")
        print("5. Delete Task")
        print("0. Back")

        choice = input("Choose: ").strip()
        if choice == "1":
            task_service.create_task()
            pause()
        elif choice == "2":
            tid = input_nonempty("Enter Task ID (e.g., TSK_000001): ")
            task_service.search_task(tid)
            pause()
        elif choice == "3":
            task_service.list_tasks()
            pause()
        elif choice == "4":
            tid = input_nonempty("Enter Task ID to update: ")
            task_service.update_task(tid)
            pause()
        elif choice == "5":
            tid = input_nonempty("Enter Task ID to delete: ")
            task_service.delete_task(tid)
            pause()
        elif choice == "0":
            return
        else:
            print("Invalid choice.")
            pause()


def employee_menu(employee_service: EmployeeService):
    while True:
        print("\n==== EMPLOYEE MENU ====")
        print("1. Create Employee")
        print("2. Search Employee")
        print("3. List Employees")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("0. Back")

        choice = input("Choose: ").strip()
        if choice == "1":
            try:
                print("\n-- Enter Employee Address Details --")
                addr = create_address_from_user()
                employee_service.create_employee(addr)  # you chose signature create_employee(self, address)
            except ValueError as ve:
                print(f"Error creating employee: {ve}")
            except Exception as e:
                print(f"Unexpected error: {e}")
            pause()
        elif choice == "2":
            eid = input_nonempty("Enter Employee ID (e.g., EMP_000001): ")
            employee_service.search_employee(eid)
            pause()
        elif choice == "3":
            employee_service.list_employees()
            pause()
        elif choice == "4":
            eid = input_nonempty("Enter Employee ID to update: ")
            employee_service.update_employee(eid)
            pause()
        elif choice == "5":
            eid = input_nonempty("Enter Employee ID to delete: ")
            employee_service.delete_employee(eid)
            pause()
        elif choice == "0":
            return
        else:
            print("Invalid choice.")
            pause()


def client_menu(client_service: ClientService):
    while True:
        print("\n==== CLIENT MENU ====")
        print("1. Create Client")
        print("2. Search Client")
        print("3. List Clients")
        print("4. Update Client")
        print("5. Delete Client")
        print("0. Back")

        choice = input("Choose: ").strip()
        if choice == "1":
            try:
                print("\n-- Enter Client Address Details --")
                addr = create_address_from_user()
                client_service.create_client(addr)  # signature create_client(self, address)
            except ValueError as ve:
                print(f"Error creating client: {ve}")
            except Exception as e:
                print(f"Unexpected error: {e}")
            pause()
        elif choice == "2":
            cid = input_nonempty("Enter Client ID (e.g., CLT_000001): ")
            client_service.search_client(cid)
            pause()
        elif choice == "3":
            client_service.list_clients()
            pause()
        elif choice == "4":
            cid = input_nonempty("Enter Client ID to update: ")
            client_service.update_client(cid)
            pause()
        elif choice == "5":
            cid = input_nonempty("Enter Client ID to delete: ")
            client_service.delete_client(cid)
            pause()
        elif choice == "0":
            return
        else:
            print("Invalid choice.")
            pause()


def timesheet_menu(timesheet_service: TimeSheetService):
    while True:
        print("\n==== TIMESHEET MENU ====")
        print("1. Create Timesheet")
        print("2. Search Timesheet")
        print("3. List Timesheets")
        print("4. Update Timesheet")
        print("5. Delete Timesheet (Not Allowed)")
        print("0. Back")

        choice = input("Choose: ").strip()
        if choice == "1":
            timesheet_service.create_timesheet()
            pause()
        elif choice == "2":
            tid = input_nonempty("Enter Timesheet ID (e.g., TMS_000001): ")
            timesheet_service.search_timesheet(tid)
            pause()
        elif choice == "3":
            timesheet_service.list_timesheets()
            pause()
        elif choice == "4":
            tid = input_nonempty("Enter Timesheet ID to update: ")
            timesheet_service.update_timesheet(tid)
            pause()
        elif choice == "5":
            # As per spec: no deletion
            timesheet_service.delete_timesheet("")
            pause()
        elif choice == "0":
            return
        else:
            print("Invalid choice.")
            pause()


def billing_menu(billing_service: BillingService):
    while True:
        print("\n==== BILLING MENU ====")
        print("1. Generate Bill for Employee (TXT)")
        print("2. Generate Bill for Client (TXT)")
        print("0. Back")

        choice = input("Choose: ").strip()
        if choice == "1":
            try:
                eid = input_nonempty("Enter Employee ID: ")
                bill_date = input_nonempty("Enter Bill Date (yyyy/MM/dd): ")
                bill_status = input_nonempty("Bill Status (yes/no or true/false): ")
                billing_service.generate_bill_for_employee(eid, bill_date, bill_status)
            except ValueError as ve:
                print(f"Billing error: {ve}")
            except Exception as e:
                print(f"Unexpected error: {e}")
            pause()
        elif choice == "2":
            try:
                cid = input_nonempty("Enter Client ID: ")
                bill_date = input_nonempty("Enter Bill Date (yyyy/MM/dd): ")
                bill_status = input_nonempty("Bill Status (yes/no or true/false): ")
                billing_service.generate_bill_for_client(cid, bill_date, bill_status)
            except ValueError as ve:
                print(f"Billing error: {ve}")
            except Exception as e:
                print(f"Unexpected error: {e}")
            pause()
        elif choice == "0":
            return
        else:
            print("Invalid choice.")
            pause()


# ---------- Main ----------
def main():
    ensure_storage_folder()

    # Repositories
    task_repo = TaskRepository()
    employee_repo = EmployeeRepository()
    client_repo = ClientRepository()
    timesheet_repo = TimeSheetRepository()

    # Services
    task_service = TaskService(task_repo)
    employee_service = EmployeeService(employee_repo)
    client_service = ClientService(client_repo)

    # Timesheet service needs to verify IDs exist, so pass those repos too
    timesheet_service = TimeSheetService(
        timesheet_repo=timesheet_repo,
        employee_repo=employee_repo,
        client_repo=client_repo,
        task_repo=task_repo,
    )

    # Billing service reads timesheets + employee/client existence
    billing_service = BillingService(
        timesheet_repo=timesheet_repo,
        employee_repo=employee_repo,
        client_repo=client_repo,
    )

    while True:
        print("\n==============================")
        print("     MAIN MENU (Mini Project) ")
        print("==============================")
        print("1. Task Management")
        print("2. Employee Management")
        print("3. Client Management")
        print("4. Timesheet Management")
        print("5. Billing Management")
        print("6. Bulk Import All (CSV)")
        print("0. Exit")

        choice = input("Choose: ").strip()
        if choice == "1":
            task_menu(task_service)
        elif choice == "2":
            employee_menu(employee_service)
        elif choice == "3":
            client_menu(client_service)
        elif choice == "4":
            timesheet_menu(timesheet_service)
        elif choice == "5":
            billing_menu(billing_service)
        elif choice == "6":
            bulk_import_all(task_service, employee_service, client_service)
            pause()
        
        elif choice == "0":
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice. Try again.")
            pause()


if __name__ == "__main__":
    main()
