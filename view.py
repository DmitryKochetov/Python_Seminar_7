import sqlite3
import os
import keyboard
import time

db = sqlite3.connect('data_base.db')

cursor = db.cursor()


def preview_base():
    os.system('cls')
    for i in cursor.execute('SELECT * FROM personal;'):
        print(*i)
        
    time.sleep(1)
    print("Для продолжения нажмите Пробел...")
    while True:
        if keyboard.is_pressed(' '):
            break