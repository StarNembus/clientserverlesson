#  Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование»,
#  «сокет», «декоратор». Далее забыть о том, что мы сами только что создали этот файл и исходить из того,
#  что перед нами файл в неизвестной кодировке.
#  Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой кодировке он был создан.

from chardet import detect
# создание файла в необходимой кодировке
f = open('test_file.txt', 'w', encoding='utf-8')
f.write('"сетевое программирование", "сокет", "декоратор"')
f.close()

# узнать кодировку файла
with open('test_file.txt', 'rb') as f:
    content = f.read()
encoding = detect(content)['encoding']
print('encoding: ', encoding)

# открыть файл в известной кодировке
with open('test_file.txt', encoding=encoding) as f_n:
    for element in f_n:
        print(element, end='')
    print()
