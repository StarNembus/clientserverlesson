"""
Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров
 — товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""
from datetime import datetime
import json


def myconverter(o):
    if isinstance(o, datetime):
        return "{}-{}-{}".format(o.year, o.month, o.day)


def writer_order_to_json(product=None, quantity=0, price=float, name=None, date=datetime.now()):

    with open('orders.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open('orders.json', 'w', encoding='utf-8') as f_n:
        order_list = data['orders']
        dict_to_json = {
            'item': product,
            'quantity': quantity,
            'price': price,
            'buyer': name,
            'date': date
        }
        order_list.append(dict_to_json)
        json.dump(data, f_n, indent=4, default=myconverter)



writer_order_to_json('kiwi', 10, 5.99, 'Oleg')
writer_order_to_json('apple', 5, 7, 'Jake')
