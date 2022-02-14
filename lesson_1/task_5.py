# Выполнить пинг веб-ресурсов yandex.ru, youtube.com
# и преобразовать результаты из байтовового в строковый тип на кириллице.

import chardet
import subprocess
import platform
import locale

# param = '-n' if platform.system().lower() == 'windows' else '-c'
# args = ['ping', param, '2', 'yandex.ru']
# result = subprocess.Popen(args, stdout=subprocess.PIPE)
# for line in result.stdout:
#     result = chardet.detect(line)
#     print('result = ', result)
#     line = line.decode(result['encoding']).encode('utf-8')
#     print(line.decode('utf-8'))

param = '-n' if platform.system().lower() == 'windows' else '-c'
args = ['ping', param, '2', 'youtube.com']
result = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in result.stdout:
    result = chardet.detect(line)
    print('result = ', result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

# default_encoding = locale.getpreferredencoding()
# print(default_encoding)
