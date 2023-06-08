import requests
from time import sleep
import random
import json
import sqlalchemy
from sqlalchemy import text


random.seed(100)


class AWSDBConnector:

    def __init__(self):

        self.HOST = "pinterestdbreadonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com"
        self.USER = 'project_user'
        self.PASSWORD = ':t%;yCY3Yjg'
        self.DATABASE = 'pinterest_data'
        self.PORT = 3306
        
    def create_db_connector(self):
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4")
        return engine

class UserPostingEmulation():

    def __init__(self):
        self.random_row = random.randint(0, 11000)

    def pin_post(self, connection):
        pin_string = text(f"SELECT * FROM pinterest_data LIMIT {self.random_row}, 1")
        pin_selected_row = connection.execute(pin_string)
            
        for row in pin_selected_row:
            pin_result = dict(row._mapping)
        self.pin_result = pin_result

    def geo_post(self, connection):
        geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
        geo_selected_row = connection.execute(geo_string)
        
        for row in geo_selected_row:
            geo_result = dict(row._mapping)
        self.geo_result = geo_result

    def user_post(self,connection):
        user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
        user_selected_row = connection.execute(user_string)
        
        for row in user_selected_row:
            user_result = dict(row._mapping)
        self.user_result = user_result
    
new_connector = AWSDBConnector()    
upe = UserPostingEmulation()

def run_infinite_post_data_loop():
    while True:
        sleep(random.randrange(0, 2))
        engine = new_connector.create_db_connector()

        with engine.connect() as connection:

            upe.pin_post(connection)
            upe.geo_post(connection)
            upe.user_post(connection)


            headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
            
            pin_response = requests.request("POST", pin_invoke_url, headers=headers, data=pin_payload)
            geo_response = requests.request("POST", geo_invoke_url, headers=headers, data= geo_payload)
            user_response = requests.request("POST", user_invoke_url, headers=headers, data= user_payload)


            print(pin_response.status_code)
            print(geo_response.status_code)
            print(user_response.status_code)


if __name__ == "__main__":
    run_infinite_post_data_loop()
    print('Working')
    