# from statistics import mode
# from calc.view import view_data
import m_csv_read as read
import m_csv_write as write
import m_csv_find as find
# import view
import os


def button_click():
    # value_a = view.get_value()
    # value_b = view.get_value()
    # model.init(value_a, value_b)
    # result = model.do_it()
    # view.view_data(result, "resul")
    os.system('cls')
    print('Главное меню:')
    print('1 - просмотр телефонного справочника')
    print('2 - внесение новой записи')
    print('3 - поиск записи')
    user_choise = int(input('введите номер пункта меню: '))
    if user_choise == 1:
        read.read_all_data()
    if user_choise == 2:
        write.write_data()
    if user_choise == 3:
        find.find_data()
    # print(user_choise)
