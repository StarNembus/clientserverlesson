import os
import platform
import subprocess
from ipaddress import ip_address


result = {'Доступные': "", "Недоступные": ""}

dnull = open(os.devnull, 'w')


def check_is_ipaddress(value):
    try:
        ipv4 = ip_address(value)
    except ValueError:
        raise Exception('Некорректный ip')
    return ipv4


def host_ping(hosts_list, get_list=False):

    for host in hosts_list:
        try:
            ipv4 = check_is_ipaddress(host)
        except Exception as e:
            print(f'{host} - {e}')
            ipv4 = host

        param = '-n' if platform.system().lower() == 'windows' else '-c'
        response = subprocess.Popen(['ping', param, '1', '-w', '1', str(ipv4)], stdout=subprocess.PIPE)

        if response.wait() == 0:
            result['Доступные'] += f'{ipv4}\n'
            res_string = f'{ipv4} - Узел доступен'
        else:
            result['Недоступные'] += f'{ipv4}\n'
            res_string = f'{ipv4} - Узел недоступен'
        if not get_list:
            print(res_string)
    if get_list:
        return result


if __name__ == '__main__':

    host_list = ['93.186.225.208', '8.8.8.8', '93.186.225.208']

    host_ping(host_list)
