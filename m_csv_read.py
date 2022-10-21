import csv

def read_all_data():
    with open('phone_base.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            print(row['first_name'], row['last_name'], row ['telephone_num'], row['discription'])

# print()
# print('version 2:')
# with open('names.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     lst_reader = list(reader)

# print(lst_reader)
