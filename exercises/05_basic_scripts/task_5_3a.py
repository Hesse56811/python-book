# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
mode = input('Enter a mode of interface (access/trunk): ')
questions = {'access': 'Введите номер VLAN:', 'trunk': 'Введите разрешенные VLANы:'}
number_interface = input('Enter a number of interface: ')
number_vlan = input(questions[mode])

mode_interf = {'access': access_template, 'trunk': trunk_template}
print('interface ' + number_interface)
print(('\n'.join(mode_interf[mode])).format(number_vlan))