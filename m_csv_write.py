import csv


def write_data():
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    telephone_num = input('Введите номер телефона: ')
    discription = input('Введите описание: ')

    with open('phone_base.csv', 'a', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'telephone_num', 'discription']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'first_name': first_name, 'last_name': last_name, 'telephone_num': telephone_num, 'discription': discription})

    # with open('phone_base.csv', 'w', newline='') as csvfile:
    #     fieldnames = ['first_name', 'last_name', 'telephone_num', 'description']
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # writer.writeheader()
    # writer.writerow({'first_name': first_name, 'last_name': last_name, 'telephone_num': telephone_num, 'discription': discription})