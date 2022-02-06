# Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и
# содержание соответствующих переменных.
# Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и также проверить тип и
# содержимое переменных.

development_1 = 'разработка'
development_2 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
print(type(development_1))
print(type(development_2))
print(development_1 == development_2)

socket_1 = 'сокет'
socket_2 = '\u0441\u043e\u043a\u0435\u0442'
my_letter = '\u043e'
print(type(socket_1))
print(type(socket_2))
print(my_letter)

decorator_1 = 'декоратор'
decorator_2 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
for items in decorator_2:
    print(items)
print(type(decorator_1))
print(type(decorator_2))
