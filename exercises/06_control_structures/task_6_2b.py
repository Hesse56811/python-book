# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Enter ip address: ')
byte = ip.split('.')
correct = False

while not correct:

    for byt in byte:
        if not len(byte) == 4:
            print('Неправильный IP-адрес')
            ip = input('Enter ip address: ')
            byte = ip.split('.')
            break
        try:
            int(byt)
        except ValueError:
            print('Неправильный IP-адрес')
            ip = input('Enter ip address: ')
            byte = ip.split('.')
            break

        if not (0 <= int(byt) <= 255):
            print('Неправильный IP-адрес')
            ip = input('Enter ip address: ')
            byte = ip.split('.')
            break
    else:
        correct = True

if correct:
    first_byte = int(ip.split('.')[0])

    if 1 <= first_byte <= 223:
        print('unicast')
    elif 224 <= first_byte <= 239:
        print('multicast')
    elif ip == '255.255.255.255':
        print('local broadcast')
    elif ip == '0.0.0.0':
        print('unassigned')
    else:
        print('unused')