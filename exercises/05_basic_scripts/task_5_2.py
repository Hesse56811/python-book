# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'

"""
ip = input('Enter ip: ')
print('Network:')
net = (ip.split('/')[0]).split('.')
mask = ip.split('/')[1]

print("{:10}{:10}{:10}{:10}".format(net[0], net[1], net[2], net[3]))
print("{:08b}  {:08b}  {:08b}  {:08b}".format(int(net[0]), int(net[1]), int(net[2]), int(net[3])))

b_mask = '1' * int(mask) + '0' * (32-int(mask))
m = [b_mask[0:8], b_mask[8:16], b_mask[16:24], b_mask[24:]]

print('\nMask:')

print('/' + mask)
print("{:<10}{:<10}{:<10}{:<10}".format(int(m[0], 2), int(m[1], 2), int(m[2], 2), int(m[3], 2)))
print("{:10}{:10}{:10}{:10}".format(m[0], m[1], m[2], m[3]))