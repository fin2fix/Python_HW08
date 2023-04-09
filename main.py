"""
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
"""

import csv
from os import system


def GetNumber():
    while True:
        try:
            resultNumber = int(input("Укажите комманду вводом соответствующей цифры:   "))
            print()
            if 0 < resultNumber < 8:
                return resultNumber
            else:
                print("Ввели не число или не корректное число. Повторите ввод!")
        except:
            print("Ввели не число или не корректное число. Повторите ввод!")


def printed(elem):
    print(f'Фамилия: {elem[0]}\nимя: {elem[1]}\nномер телефона: {elem[2]}\nкомментарий: {elem[3]}\n')


def del_contact():
    with open(r'telsprav\phonebook.csv', 'r', encoding='utf-8') as file:
        search_data = input("Введите фамилию для удаления контакта:  ")
        data = list(csv.reader(file))
        old_data = list(filter(lambda x: x and x[0] == search_data, data))
        print(*old_data)
        if len(old_data) > 0 and (input("Для подтверждения удаления напишите YES: ").lower() == "yes"):
            data.remove(old_data[0])
            file.close()
            with open(r'telsprav\phonebook.csv', 'w', encoding='utf-8') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(data)
                print("Контакт удален")
        else:
            print(f"Пользователь с фамилией {search_data} не найден или удаление не подтверждено")


def change_contact():
    with open(r'telsprav\phonebook.csv', 'r+', encoding='utf-8') as file:
        search_data = input("Введите фамилию для изменения контакта:  ")
        data = list(csv.reader(file))
        old_user = list(filter(lambda x: x and x[0] == search_data, data))
        print(*old_user)
        if len(old_user) > 0:
            new_user = input(
                'Введите данные абонента через запятую: ').split(",")
            data.remove(old_user[0])
            file.seek(0)
            writer = csv.writer(file)
            writer.writerows(data)
            writer.writerow(new_user)
            print("Данные контакта отредактированы")
        else:
            print(f"Пользователь с фамилией {search_data} не найден")


def display_all_records():
    with open(r'telsprav\phonebook.csv', 'r', encoding='utf-8') as file:
        reader = list(csv.reader(file))
        for row in reader:
            if row:
                printed(row)


def find_last_name():
    with open(r'telsprav\phonebook.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        last_name = input('Введите фамилию для поиска контакта: ')
        print()
        for elem in filter(lambda x: x and x[0] == last_name, reader):
            printed(elem)


def find_phone_number():
    with open(r'telsprav\phonebook.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        phone = input('Введите номер телефона для поиска контакта: ')
        print()
        for elem in filter(lambda x: x and x[2] == phone, reader):
            printed(elem)


def add_abonent():
    with open(r'telsprav\phonebook.csv', 'a', encoding='utf-8', newline='') as file:
        new_contact = input(
            'Введите данные абонента через запятую: ').split(",")
        csv.writer(file).writerow(new_contact)


while True:
    temp = input("Нажмите Enter для продолжения...")
    command = 0
    system('CLS')
    print("Телефонный справочник\n 1 - добавить новый контакт \n 2 - найти контакт в справочнике по фамилии")
    print(" 3 - найти контакт в справочнике по номеру телефона\n 4 - изменить контакт\n 5 - удалить контакт")
    print(" 6 - распечатать весь справочник\n 7 - выйти из справочника\n")
    command = GetNumber()
    if command == 1:
        add_abonent()
    elif command == 2:
        find_last_name()
    elif command == 3:
        find_phone_number()
    elif command == 4:
        change_contact()
    elif command == 5:
        del_contact()
    elif command == 6:
        display_all_records()
    elif command == 7:
        break
