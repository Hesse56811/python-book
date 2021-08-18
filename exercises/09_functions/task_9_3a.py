# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    access = {}
    trunk = dict()
    a = False
    with open(config_filename) as f:
        for line in f:
            if 'Fast' in line:
                port = line.rstrip().split(' ')[1]
                a = True
            if 'trunk allowed' in line:
                ls = []
                for i in line.rstrip().split(' ')[5:]:
                    for v in i.split(','):
                        ls.append(int(v))
                a = False
                trunk[port] = ls
            if 'access vlan' in line:
                a = False
                access[port] = int(line.rstrip().split(' ')[4])
            elif 'duplex auto' in line and a:
                access[port] = 1

    result = (access, trunk)
    return result
