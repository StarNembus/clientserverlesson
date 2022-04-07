# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования
# в последовательность кодов (не используя методы encode и decode) и определить тип,
# содержимое и длину соответствующих переменных.

bytes_1 = b'\u0063\u006c\u0061\u0073\u0073'  # class
bytes_2 = b'\u0066\u0075\u006e\u0063\u0074\u0069\u006f\u006e'  # function
bytes_3 = b'\u006d\u0065\u0074\u0068\u006f\u0064'  # method


my_list = [bytes_1, bytes_2, bytes_3]

for item in my_list:
    print(type(item), len(item), item)
