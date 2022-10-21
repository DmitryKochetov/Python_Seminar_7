import csv

def find_data():
    find_last_name = input('Введите фамилию: ')
    with open('phone_base.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['last_name'] == find_last_name:
                print(row)
                print(row['first_name'], row['last_name'], row ['telephone_num'], row['discription'])