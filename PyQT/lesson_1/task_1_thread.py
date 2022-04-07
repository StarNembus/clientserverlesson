import os
import platform
import subprocess
import threading
import time
from ipaddress import ip_address

result = {'Доступные': "", "Недоступные": ""}

dnull = open(os.devnull, 'w')


def check_is_ipaddress(value):
    try:
        ipv4 = ip_address(value)
    except ValueError:
        raise Exception('Некорректный ip')
    return ipv4


def ping(ipv4, result, get_list):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    response = subprocess.Popen(['ping', param, '1', '-w', '1', str(ipv4)], stdout=subprocess.PIPE)

    if response.wait() == 0:
        result['Доступные'] += f'{ipv4}\n'
        res = f'{ipv4} - Узел доступен'
        if not get_list:
            print(res)
        return res
    else:
        result['Недоступные'] += f'{ipv4}\n'
        res = f'{ipv4} - Узел недоступен'
        if not get_list:
            print(res)
        return res

def host_ping(hosts_list, get_list=False):
    threads = []
    for host in hosts_list:
        try:
            ipv4 = check_is_ipaddress(host)
        except Exception as e:
            print(f'{host} - {e}')
            ipv4 = host

        thread = threading.Thread(target=ping, args=(ipv4, result, get_list), daemon=True)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    if get_list:
        return result


if __name__ == '__main__':

    hosts_list = ['93.186.225.208', '8.8.8.8', '93.186.225.208']
    start = time.time()
    host_ping(hosts_list)
    end = time.time()



