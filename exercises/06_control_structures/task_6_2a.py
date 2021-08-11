# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Enter ip address: ')
byte = ip.split('.')

for byt in byte:
    if not len(byte) == 4:
        print('Неправильный IP-адрес')
        break
    try:
        int(byt)
    except ValueError:
        print('Неправильный IP-адрес')
        break
    if not (0 <= int(byt) <= 255):
        print('Неправильный IP-адрес')
        break
else: 
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
