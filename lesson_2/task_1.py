"""
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список.
Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
В этой же функции создать главный список для хранения данных отчета
— например, main_data — и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС»,
«Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(),
в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv()
"""
import csv
import re

import chardet


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []

    for item in range(1, 4):
        with open(f'info_{item}.txt', 'rb') as file:
            data_b = file.read()
            result = chardet.detect(data_b)
            data = data_b.decode(result['encoding'])

        prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
        os_prod_list.append(prod_reg.findall(data)[0].split()[2])

        name_reg = re.compile(r'Windows\s\S*')
        os_name_list.append(name_reg.findall(data)[0])

        code_reg = re.compile(r'Код продукта:\s*\S*')
        os_code_list.append(code_reg.findall(data)[0].split()[2])

        type_reg = re.compile(r'Тип системы:\s*\S*')
        t = type_reg.findall(data)
        t = t[0].split()[2]
        os_type_list.append(t)

    words = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data.append(words)

    data_row = [os_prod_list, os_name_list, os_code_list, os_type_list]

    for i in range(len(data_row[0])):
        line = [row[i] for row in data_row]
        main_data.append(line)

    return main_data


def write_to_csv(my_file):
    main_data = get_data()
    with open(my_file, 'w', encoding='utf-8') as f_n:
        writer = csv.writer(f_n)
        for row in main_data:
            writer.writerow(row)


write_to_csv('data_csv.csv')
