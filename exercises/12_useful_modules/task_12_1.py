# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess


def ping_ip_addresses(ip_address):
    reach = []
    unreach = []
    for ip in ip_address:
        if subprocess.call(['ping', '-c', '3', '-n', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0:
            reach.append(ip)
        else:
            unreach.append(ip)
    return reach, unreach


if __name__ == '__main__':
    print(ping_ip_addresses(["10.1.1.1", "8.8.8.8"]))