from extract import Extract

if __name__ == '__main__':
    e = Extract("public_ips.csv")
    ips = e.get_file_data()
    users = e.get_users(ips)