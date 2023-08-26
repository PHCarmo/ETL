import pandas as pd
import os
import requests
from user import User

class Extract:
    def __init__(self, file_name) -> None:
        self.HOST = "http://api.weatherstack.com/current"
        self.ACCESS_KEY = "Insert your API key here"
        self.file_path = os.path.join(os.path.dirname(__file__), "data", file_name)

    def get_file_data(self):
        df = pd.read_csv(self.file_path)
        return df['IP'].tolist()

    def get_users(self, ips):
        users = []
        for ip in ips:
            if (user := self.get_weather_by_ip(ip)):
                users.append(
                    User(
                        user["current"]["weather_descriptions"][0],
                        **user["current"],
                        **user["location"]
                    )
                )
        return users

    def get_weather_by_ip(self, ip):
        params = {
            "access_key": self.ACCESS_KEY,
            "query": ip,
        }
        response = requests.get(f'{self.HOST}', params=params)
        return response.json() if response.status_code == 200 else None