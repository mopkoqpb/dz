#Задание 1
ann = 2
paul = 5
print('У Анны ' + str(ann) + ' яблока.', 'У Пола ' + str(paul) + ' яблока.')

#Задание 2
v_cube = float(input('введите значение: '))
v = v_cube**3
pl = 6*(v_cube**2)
print('Объем куба равен: ' + str(v))
print('Площадь боковой поверхности равна: ' + str(pl))

#Задание 3
day = 2
night = 1
h = 20
finish = h/(day-night)
print('Улитка проползет за ' + str(finish) + ' дней')


import math
import random
#Творческое задание
roll = random.randint(1, 999)
print('Случайное число: ' + str(roll))
sqr = math.sqrt(roll)
print('Корень случайного числа: ' +str(sqr))

