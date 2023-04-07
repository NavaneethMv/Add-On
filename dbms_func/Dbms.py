from dotenv import load_dotenv
import os
from definitions import ROOT_DIR
import mysql.connector as database

class Dbms_tools:
    def __init__(self) -> None:
        self.check()
        self.username = os.environ.get("DB_USER")
        self.password = os.environ.get("DB_PASS")
        self.connection = self.connect() 

    def clean(self):
        pass

    def save_all(self, name, address, phone_no, type):
        try:
            cursor = self.connection.cursor()
            statement = f'INSERT INTO DonorDetails(name, address, phone_no, type) VALUES("{name}", "{address}", "{phone_no}", "{type}")'
            cursor.execute(statement)
            print("its done")
            return 0
        except database.Error as e:
            print(f"Error saving entry from database: {e}")
            return 1


    def check(self):
        if (os.environ.get("DB_TYPE") == None):
            load_dotenv(os.path.join(ROOT_DIR, 'config', '.env'))


    def connect(self) -> object:
        connection = database.connect(
                user=self.username,
                password=self.password,
                host=os.environ.get("DB_HOST"),
                database=os.environ.get("DB_NAME"))
        return connection
    

    def get_basic(self):
        try:
            cursor = self.connection.cursor()
            data = []
            statement = "SELECT id, name, type, date, address FROM DonorDetails"
            cursor.execute(statement)
            for (id, name, type, date, address) in cursor:
                data.append({'id': id,
                             'name': name,
                             'type': type,
                             'date': date,
                             'address': address})
            return data
        except database.Error as e:
            print(f"Error retrieving entry from database: {e}")
            return []

    
