# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

new_list = []

vlan = int(input('Enter VLAN number: '))

with open('CAM_table.txt') as f:
    for line in f:
        if 'DYNAMIC' in line:
            x = line.split()
            new_list.append([int(x[0]), x[1], x[3]])

for l in sorted(new_list):
    if l[0] == vlan:
        print('{:<9}{:20}{}'.format(l[0], l[1], l[2]))
