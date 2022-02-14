"""
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
отсутствующим в кодировке ASCII (например, €);

Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style,
а также установить возможность работы с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""
import yaml

data_in = {
    'key_1': ['comp', 'printer'],
    'key_2': 2,
    'key_3': {'comp': '3000€', 'printer': '500€'}
}

with open('file.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(data_in, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

with open('file.yaml', 'r', encoding='utf-8') as f_out:
    data_out = yaml.load(f_out, Loader=yaml.SafeLoader)

print(data_in == data_out)
