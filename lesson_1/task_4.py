# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
# и выполнить обратное преобразование (используя методы encode и decode).

word_1 = 'разработка'
word_2 = 'администрирование'
word_3 = 'protocol'
word_4 = 'standard'

my_list = [word_1, word_2, word_3, word_4]

for item in my_list:
    item_1 = item.encode('utf-8')
    print(item_1)
    item_2 = item_1.decode('utf-8')
    print(item_2)
    print('-------------------------------------')

