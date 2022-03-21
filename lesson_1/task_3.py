# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
# Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.

word_1 = 'attribute'
word_2 = 'класс'
word_3 = 'функция'
word_4 = 'type'

# print(word_1)
# print(word_2)

# вариант 1 для кириллицы


def error_bytes_function(word):
    for letter in word:
        if ord('А') <= ord(letter) <= ord('я'):
            print('?', end='')
        else:
            print(letter, end='')


error_bytes_function(word_2)


# вариант 2
def error_bytes_function2(word):
    new_str = word.encode('ascii', 'replace')
    print(new_str)


error_bytes_function2(word_4)






