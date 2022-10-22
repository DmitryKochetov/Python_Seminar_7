
import baseio
import view
import os



def button_click():
    while True:
        os.system('cls')
        print('1 - посмотреть базу: ')
        print('2 - добавить сотрудника: ')
        print('3 - удалить запись')
        print('4 - найти по ФИО')
        print('5 - изменить запись')
        print('q - выход')
        user_choice = input()
        if user_choice == '1':
            view.preview_base()
        elif user_choice == '2':
            baseio.add_record_base()
        elif user_choice == '3':
            baseio.delete_record_base()
        elif user_choice == '4':
            baseio.find_record_base()
        elif user_choice == '5':
            baseio.change_record()
        elif user_choice == 'q':
            print('Выход')
            break
    # value_a = view.get_value()
    # value_b = view.get_value()
    # model.init(value_a, value_b)
    # result = model.do_it()
    # view.view_data(result, "resul")
    # os.system('cls')
    # print('Главное меню:')
    # print('1 - просмотр телефонного справочника')
    # print('2 - внесение новой записи')
    # print('3 - поиск записи')
    # user_choise = int(input('введите номер пункта меню: '))
    # if user_choise == 1:
    #     read.read_all_data()
    # if user_choise == 2:
    #     write.write_data()
    # if user_choise == 3:
    # find.find_data()
    # print(user_choise)
