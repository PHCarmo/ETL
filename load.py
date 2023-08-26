import csv
import os

class Load:
    def __init__(self, file_name):
        self.file_path = os.path.join(os.path.dirname(__file__), "data", file_name)

    def export_data(self, users):
        with open(self.file_path, 'w') as f:
            writer = csv.writer(f, lineterminator = '\n')
            writer.writerow(["IP", "Weather Description", "Temperature", "Location", "Things To Do"])
            for user in users:
                writer.writerow([user.ip, user.weather, user.temperature,
                                user.get_location(), user.suggestions])