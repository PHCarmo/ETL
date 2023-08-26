from extract import Extract
from transform import Transform

if __name__ == '__main__':
    e = Extract("public_ips.csv")
    ips = e.get_file_data()
    users = e.get_users(ips)

    t = Transform()
    t.set_suggestions(users)