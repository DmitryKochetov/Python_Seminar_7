import sqlite3
import os
import keyboard
import time

db = sqlite3.connect('data_base.db')
cursor = db.cursor()

def add_record_base():
    os.system('cls')
    id_inp = input('Введите id: ')    
    name_inp = input('Введите имя: ')
    last_name_inp = input('Введите фамилию: ')
    position_inp = input('Введите должность: ')
    salary_inp = input('Введите зарплату: ')
    bonus_inp = input('Введите бонус: ')

    try:
        cursor.execute(f'INSERT INTO personal VALUES({id_inp},"{name_inp}","{last_name_inp}","{position_inp}",{salary_inp},{bonus_inp})')
        db.commit()
    except:
        print('Данные уже есть')


def delete_record_base():
    os.system('cls')
    i = input('Введите id удаляемой записи')
    cursor.execute(f'DELETE from personal WHERE id = {i};')
    db.commit()


def find_record_base():
    os.system('cls')
    column = input('Введите колонку, по которой будем искать (id, name, last_name, position): ')
    i = input('Введите значение для поиска: ')
    cursor.execute(f'select * from personal WHERE {column} Like {i};')
    one = cursor.fetchmany()
    print(*one)
    time.sleep(1)
    print("Для продолжения нажмите Пробел...")
    while True:
        if keyboard.is_pressed(' '):
            break


def change_record():
    os.system('cls')
    id_inp = input('Введите id: ')
    column_inp = input('Введите колонку, которую меняем (name, last_name, position, salary, bonus): ')
    value_inp = input('Введите новое значение: ')
    cursor.execute(f'UPDATE personal SET {column_inp} = "{value_inp}" WHERE id = {id_inp};')
    db.commit()