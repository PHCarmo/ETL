import pandas as pd
import os
import requests

class Extract:
    def __init__(self, file_name) -> None:
        self.HOST = "http://api.ipstack.com/"
        self.ACCESS_KEY = "62f0ab8382f8b5508bbf1943bab6e40c"
        self.file_path = os.path.join(os.path.dirname(__file__), "data", file_name)

    def get_file_data(self):
        df = pd.read_csv(self.file_path)
        return df['IP'].tolist()

    def get_users(self, ips):
        return [user for ip in ips if (user := self.get_ip_info(ip))]

    def get_ip_info(self, ip):
        params = { "access_key": self.ACCESS_KEY }
        response = requests.get(f'{self.HOST}{ip}', params=params)
        return response.json() if response.status_code == 200 else None