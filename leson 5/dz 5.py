# first = float(input('введите первое число: '))
# second = float(input('введите второе число: '))
# s = input('введите = - * /: ')
# while True:
#     if s == '':
#         break
#     elif s == '+':
#         print(first+second)
#         break
#     elif s == '-':
#         print(first-second)
#         break
#     elif s == '*':
#         print(first*second)
#         break
#     elif s == '/':
#         if second != 0:
#             print(first/second)
#             break
#         else:
#             print('на ноль делить нельзя!')
#             break

#Casino
import random
print('У вас есть 5 попыток')
i1 = random.randint(1,2)
j2 = (random.randint(1, 2))
if j2 == 1:
    j2 = 'black'
else:
    j2 = 'red'
pop = 0
while pop < 5:
    i = int(input('введите число от 1 до 10: '))
    j = (input('введите (black or red): '))
    if i == i1 and j == j2:
        print('win')
        break
      
    else:
        print('не угадал')
        pop += 1
    print('казино выбрало:', i1, j2)
    print('вы исчерпали все попытки')
















