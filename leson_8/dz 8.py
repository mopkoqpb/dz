import random

# def calcul():
#     # first = float(input('введите первое число: '))
#     # second = float(input('введите второе число: '))
#     # s = input('введите + - * /: ')
#     while True:
#         if s == '':
#          break
#         elif s == '+':
#             rew = first+second
#             break
#         elif s == '-':
#             rew = first-second
#             break
#         elif s == '*':
#             rew = first*second
#             break
#         elif s == '/':
#             if second != 0:
#                 rew = first/second
#                 break
#             else:
#                 rew = 'на ноль делить нельзя!'
#                 break
#     return rew
#
# first = float(input('введите первое число: '))
# second = float(input('введите второе число: '))
# s = input('введите + - * /: ')
# print(calcul())



#dz6
n = 10
a = [random.randint(1,100) for i in range(n)]
def ran(a):
    s = 0
    for i in range(n):
        s += a[i]
    return s / 10
# print(a)
print(ran(a))

# dz 5
# def prost(a):
#     d = 2
#     while a % d != 0:
#         d += 1
#     return d == a
# a = int(input('vvedite chislo: '))
# print(prost(a))
