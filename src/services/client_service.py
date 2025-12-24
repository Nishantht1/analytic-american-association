import csv
from models.client import Client
from utils.csv_utils import read_csv_rows
from models.address import Address





    
class ClientService:
    def __init__(self, repo):
        self.repo = repo

    def bulk_import_clients_from_csv(self, csv_path="storage/csv/clients.csv"):
        

        success = 0
        failed = 0

        with open(csv_path, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)

            for row in reader:
                try:
                    client_id = self.generate_client_id()
                    client_name = row["Client Name"].strip()
                    client_description = row["Descrioption"].strip()
                    rate_raw = (row.get("Standart Bill Rate") or "").strip()
                    rate_clean = rate_raw.replace("$", "").replace(",", "").strip()
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

                    client = Client(client_id, client_name, client_description, std_bill_rate, address)
                    self.repo.append(client)
                    success += 1

                except Exception as e:
                    failed += 1
                    print(f"[CLIENT CSV ERROR] {e} | Row={row}")

        print(f"Client CSV Import Done → Success: {success}, Failed: {failed}")

    def generate_client_id(self):
        clients = self.repo.load_all()
        max_num = max([int(c.client_id.split("_")[1]) for c in clients], default=0)
        next_num = max_num + 1
        return f"CLT_{next_num:06d}"

    def create_client(self, address):
        try:
            client_id = self.generate_client_id()
            client_name = input("Enter Client Name: ")
            client_description = input("Enter Client Description: ")
            std_bill_rate = float(input("Enter Standard Bill Rate: "))

            client = Client(client_id, client_name, client_description, std_bill_rate, address)
            self.repo.append(client)

            print(f"Client created successfully: {client_id}")

        except ValueError as ve:
            print(f"Error creating client: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def search_client(self, client_id):
        client_id = client_id.strip()
        clients = self.repo.load_all()

        for c in clients:
            if c.client_id == client_id:
                print("Client Found:")
                print(f"Client ID     : {c.client_id}")
                print(f"Name          : {c.client_name}")
                print(f"Description   : {c.client_description}")
                print(f"Std Bill Rate : {c.std_bill_rate}")
                print("Address:")
                print(f"  Mail ID      : {c.address.mail_id}")
                print(f"  Phone        : {c.address.phone_number}")
                print(f"  House No     : {c.address.house_no}")
                print(f"  Building No  : {c.address.building_number}")
                print(f"  Road No      : {c.address.road_number}")
                print(f"  Street Name  : {c.address.street_name}")
                print(f"  Landmark     : {c.address.land_mark}")
                print(f"  City         : {c.address.city}")
                print(f"  State        : {c.address.state}")
                print(f"  Zip Code     : {c.address.zip_code}")
                return c

        print("Client not found.")
        return None

    def list_clients(self):
        clients = self.repo.load_all()

        if not clients:
            print("No clients are available in the system.")
            return []

        print("Client List:")
        print("-" * 50)

        for c in clients:
            print(f"Client ID     : {c.client_id}")
            print(f"Name          : {c.client_name}")
            print(f"Description   : {c.client_description}")
            print(f"Std Bill Rate : {c.std_bill_rate}")
            print("Address:")
            print(f"  Mail ID      : {c.address.mail_id}")
            print(f"  Phone        : {c.address.phone_number}")
            print(f"  House No     : {c.address.house_no}")
            print(f"  Building No  : {c.address.building_number}")
            print(f"  Road No      : {c.address.road_number}")
            print(f"  Street Name  : {c.address.street_name}")
            print(f"  Landmark     : {c.address.land_mark}")
            print(f"  City         : {c.address.city}")
            print(f"  State        : {c.address.state}")
            print(f"  Zip Code     : {c.address.zip_code}")
            print("-" * 50)

        return clients

    def update_client(self, client_id):
        client_id = client_id.strip()
        clients = self.repo.load_all()

        for c in clients:
            if c.client_id == client_id:
                print("Current Client Details:")
                print(f"Client ID     : {c.client_id}")
                print(f"Name          : {c.client_name}")
                print(f"Description   : {c.client_description}")
                print(f"Std Bill Rate : {c.std_bill_rate}")
                print("Address:")
                print(f"  Mail ID      : {c.address.mail_id}")
                print(f"  Phone        : {c.address.phone_number}")
                print(f"  House No     : {c.address.house_no}")
                print(f"  Building No  : {c.address.building_number}")
                print(f"  Road No      : {c.address.road_number}")
                print(f"  Street Name  : {c.address.street_name}")
                print(f"  Landmark     : {c.address.land_mark}")
                print(f"  City         : {c.address.city}")
                print(f"  State        : {c.address.state}")
                print(f"  Zip Code     : {c.address.zip_code}")

                try:
                    # Update client_description + std_bill_rate (PDF)
                    new_desc = input("Enter new Client Description (leave blank to keep current): ").strip()
                    if new_desc:
                        c.client_description = new_desc
                        c.validate_client_description()

                    new_rate = input("Enter new Std Bill Rate (leave blank to keep current): ").strip()
                    if new_rate:
                        c.std_bill_rate = float(new_rate)
                        c.validate_std_bill_rate()

                    # Update ALL Address fields (PDF)
                    new_mail = input("Enter new Mail ID (leave blank to keep current): ").strip()
                    if new_mail:
                        c.address.mail_id = new_mail
                        c.address.validate_mail_id()

                    new_phone = input("Enter new Phone Number (leave blank to keep current): ").strip()
                    if new_phone:
                        c.address.phone_number = new_phone
                        c.address.validate_phone_number()

                    new_house = input("Enter new House No (leave blank to keep current): ").strip()
                    if new_house:
                        c.address.house_no = new_house
                        c.address.validate_house_no()

                    new_building = input("Enter new Building Number (leave blank to keep current): ").strip()
                    if new_building:
                        c.address.building_number = new_building
                        c.address.validate_building_number()

                    new_road = input("Enter new Road Number (leave blank to keep current): ").strip()
                    if new_road:
                        c.address.road_number = new_road
                        c.address.validate_road_number()

                    new_street = input("Enter new Street Name (leave blank to keep current): ").strip()
                    if new_street:
                        c.address.street_name = new_street
                        c.address.validate_street_name()

                    new_landmark = input("Enter new Landmark (leave blank to keep current): ").strip()
                    if new_landmark:
                        c.address.land_mark = new_landmark
                        c.address.validate_land_mark()

                    new_city = input("Enter new City (leave blank to keep current): ").strip()
                    if new_city:
                        c.address.city = new_city
                        c.address.validate_city()

                    new_state = input("Enter new State (leave blank to keep current): ").strip()
                    if new_state:
                        c.address.state = new_state
                        c.address.validate_state()

                    new_zip = input("Enter new Zip Code (leave blank to keep current): ").strip()
                    if new_zip:
                        c.address.zip_code = new_zip
                        c.address.validate_zip_code()

                    self.repo.save_all(clients)
                    print("Client updated successfully.")

                except ValueError as ve:
                    print(f"Error updating client: {ve}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

                return

        print("Client not found.")

    def delete_client(self, client_id):
        client_id = client_id.strip()
        clients = self.repo.load_all()

        for i, c in enumerate(clients):
            if c.client_id == client_id:
                del clients[i]
                self.repo.save_all(clients)
                print("Client deleted successfully.")
                return

        print("Client not found.")