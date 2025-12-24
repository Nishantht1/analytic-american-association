import re
from models.address import Address
from models.client import Client
CLIENT_FILE_PATH = "storage/clients.txt"




class ClientRepository:
    def append(self, client):
        with open(CLIENT_FILE_PATH, "a", encoding="utf-8") as file:
            file.write(
                f"{client.client_id}|{client.client_name}|{client.client_description}|{client.std_bill_rate}|"
                f"{client.address.mail_id}|{client.address.phone_number}|"
                f"{client.address.house_no}|{client.address.building_number}|"
                f"{client.address.road_number}|{client.address.street_name}|"
                f"{client.address.land_mark}|{client.address.city}|"
                f"{client.address.state}|{client.address.zip_code}\n"
            )

    def load_all(self):
        clients = []
        try:
            with open(CLIENT_FILE_PATH, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue

                    parts = line.split("|")
                    if len(parts) != 14:
                        continue  # skip malformed lines safely

                    client_id = parts[0]
                    client_name = parts[1]
                    client_description = parts[2]
                    std_bill_rate = float(parts[3])

                    address = Address(
                        mail_id=parts[4],
                        phone_number=parts[5],
                        house_no=parts[6],
                        building_number=parts[7],
                        road_number=parts[8],
                        street_name=parts[9],
                        land_mark=parts[10],
                        city=parts[11],
                        state=parts[12],
                        zip_code=parts[13],
                    )

                    client = Client(client_id, client_name, client_description, std_bill_rate, address)
                    clients.append(client)

        except FileNotFoundError:
            pass

        return clients

    def save_all(self, clients):
        with open(CLIENT_FILE_PATH, "w", encoding="utf-8") as file:
            for client in clients:
                file.write(
                    f"{client.client_id}|{client.client_name}|{client.client_description}|{client.std_bill_rate}|"
                    f"{client.address.mail_id}|{client.address.phone_number}|"
                    f"{client.address.house_no}|{client.address.building_number}|"
                    f"{client.address.road_number}|{client.address.street_name}|"
                    f"{client.address.land_mark}|{client.address.city}|"
                    f"{client.address.state}|{client.address.zip_code}\n"
                )
