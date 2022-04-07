# Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
# Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
# В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
# («Узел доступен», «Узел недоступен»).
# При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().

import ipaddress


from pythonping import ping
import socket

host_list = ['ya.ru', 'mail.ruuu', '93.186.225.208', '8.8.8.8']


def host_ping(hosts):
    for h in hosts:
        try:
            host_ip = socket.gethostbyname(h)
        except socket.gaierror:
            print(f'{h} - Host not found')
            continue
        ipa = ipaddress.ip_address(host_ip)
        responses = ping(ipa.exploded)
        if len(responses) == 0:
            print(f'{h} - Узел недоступен')
        else:
            print(f'{h} - Узел доступен')



host_ping(host_list)

