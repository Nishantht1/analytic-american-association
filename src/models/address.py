from ast import pattern
import re


class Address:
    def __init__(self, mail_id, phone_number, house_no, building_number, road_number, street_name, land_mark, city, state, zip_code):
        self.mail_id = mail_id
        self.phone_number = phone_number
        self.house_no = house_no
        self.building_number = building_number
        self.road_number = road_number
        self.street_name = street_name
        self.land_mark = land_mark
        self.city = city
        self.state = state
        self.zip_code = zip_code

        self.validate_mail_id()
        self.validate_phone_number()
        self.validate_house_no()            
        self.validate_building_number()
        self.validate_road_number()
        self.validate_street_name()
        self.validate_land_mark()
        self.validate_city()
        self.validate_state()
        self.validate_zip_code()
        


    def validate_mail_id(self):
        mail_id=self.mail_id.strip()
        pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if len(mail_id)==0:
            raise ValueError("Mail ID cannot be empty.")
        elif not re.match(pattern, mail_id):
            raise ValueError("Invalid Mail ID format.")


    def validate_phone_number(self):
        phone_number=str(self.phone_number).strip()
        if len(phone_number)==10 and phone_number.isdigit():
            return
        elif len(phone_number)==13 and phone_number.startswith("+91") and phone_number[3:].isdigit():
            return
        else:
            raise ValueError("Invalid phone number format.")

    def validate_house_no(self):
        house_no=str(self.house_no).strip()
        pattern=r'^[A-Za-z0-9#/\-\s]+$'
        if len(house_no)==0:
            raise ValueError("House number cannot be empty.")
        elif not re.match(pattern, house_no):
            raise ValueError("House number is invalid.")

    def validate_building_number(self):
        building_number=str(self.building_number).strip()
        pattern=r'^[A-Za-z0-9\-\s\_]+$'
        if len(building_number)==0:
            raise ValueError("Building number cannot be empty.")
        elif not re.match(pattern, building_number):
            raise ValueError("Building number is invalid.")

    def validate_road_number(self):
        road_number=str(self.road_number).strip()
        pattern=r'^[A-Za-z0-9\-\s\_]+$'
        if len(road_number)==0:
            raise ValueError("Road number cannot be empty.")
        elif not re.match(pattern, road_number):
            raise ValueError("Road number is invalid.")

    def validate_street_name(self):
        street_name=str(self.street_name).strip()
        pattern=r'^[A-Za-z0-9\-\s\_]+$'
        if len(street_name)==0:
            raise ValueError("Street name cannot be empty.")
        elif not re.match(pattern, street_name):
            raise ValueError("Street name is invalid.")

    def validate_land_mark(self):
        land_mark = str(self.land_mark).strip()

        if len(land_mark) == 0:
            raise ValueError("Land mark cannot be empty.")

        # Allow unicode letters, digits, spaces, and common punctuation
        allowed_extra = "#/.,-"
        for ch in land_mark:
            if not (ch.isalnum() or ch.isspace() or ch in allowed_extra):
                raise ValueError("Land mark is invalid.")

    def validate_city(self):
        if not isinstance(self.city, str):
            raise ValueError("City must be a string.")      
        
        city=self.city.strip()

        if len(city)==0:
            raise ValueError("City cannot be empty.")
        
        pattern = r'^[A-Za-z\s\-]+$'
        if not re.match(pattern, city):
            raise ValueError("City must contain only alphabetic characters.")

    def validate_state(self):
        if not isinstance(self.state, str):
            raise ValueError("State must be a string.") 
        state=self.state.strip()
        if len(state)==0:
            raise ValueError("State cannot be empty.")
        
        pattern = r'^[A-Za-z\s]+$'

        if not re.match(pattern, state):
            raise ValueError("State must contain only alphabetic characters.")


    def validate_zip_code(self):  
        zip_code=str(self.zip_code).strip()
        if len(zip_code)==0:
            raise ValueError("Zip code cannot be empty.")
        if not zip_code.isdigit():
            raise ValueError("Zip code must contain only digits.")

      