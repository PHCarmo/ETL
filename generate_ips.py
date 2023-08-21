from faker import Faker
import os

QUANTITY = 10

file_path = os.path.join(os.path.dirname(__file__), "data", "random_ips.csv")
with open(file_path, "w", encoding="utf-8") as file:
    file.write("IP\n")
    for i in range(0,QUANTITY):
        file.write(f"{Faker().ipv6()}\n")