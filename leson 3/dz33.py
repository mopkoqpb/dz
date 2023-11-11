#Задание 7
# a = str(input('введите 1 сторону: '))
# b = str(input('введите 2 сторону: '))
# c = str(input('введите 3 сторону: '))
# if a+b>c and a+c>b and b+c>a
#     print('est')
# else:
#     print('net')

#Задание 8
# first = float(input('введите число: '))
# dei = input('введите один из действие: ')
# second = float(input('введите число: '))
# if dei == '+':
#     print(first+second)
# elif dei == '-':
#     print(first-second)
# elif dei == '*':
#     print(first*second)
# elif dei == '/':
#     print(first/second)
# else:
#     print('net deistvyi')

#Задание 9
# string = input('enter string:')
# is_mister = (string == 'Mister')
# print(is_mister)

#Задание 10
# armor = input('введите цвет доспехов(red, yellow, black):')
# shield = input('введите цвет щита(red, yellow, black):')
# is_knight = (armor != 'red' and shield == 'black')
# print(is_knight)

import random

#Задание 1
# igrok = int(input('введите случайное число от 1 до 100:'))
# result = random.randint(1, 100)
# print('случайное число: ' +str(result))
# if igrok == result:
#     print('победа!')
# else:
#     print('пройгрыш(')

#Задание 2
# day = int(input('Введите день: '))
# month = int(input('Введите месяц: '))
#
# if (month == 3 and day >= 21) or (month == 4 and day <= 20):
#     print('Овен')
# elif (month == 4 and day >= 21) or (month == 5 and day <= 21):
#         print('Телец')
# elif (month == 5 and day >= 22) or (month == 6 and day <= 21):
#         print('Близнецы')
# elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
#         print('Рак')
# elif (month == 7 and day >= 23) or (month == 8 and day <= 21):
#         print('Лев')
# elif (month == 8 and day >= 22) or (month == 9 and day <= 23):
#         print('Дева')
# elif (month == 9 and day >= 24) or (month == 10 and day <= 23):
#         print('Весы')
# elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
#         print('Скорпион')
# elif (month == 11 and day >= 23) or (month == 12 and day <= 22):
#         print('Стрелец')
# elif (month == 12 and day >= 23) or (month == 1 and day <= 20):
#         print('Козерог')
# elif (month == 1 and day >= 21) or (month == 2 and day <= 19):
#         print('Водолей')
# else:
#     print('Рыбы')

#Творческое задание
#
# x = int(input('введите число: '))
#
# if x<= 10 or 10<=x<= 50:
#     print('small')
# elif x<= 100:
#     print('med')
# else:
#     print('large')