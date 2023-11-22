#dz1
# def imt(rost,ves):
#     rost = float(input('vvesti rost: '))
#     ves = float(input('vvesti ves: '))
#     imt_1 = ves / (rost)**2
#     if imt_1 <= 16:
#         print('дефецит массы')
#     elif imt_1 > 16 and 25 > imt_1:
#         print('норма')
#     elif imt_1 > 25 and 40 > imt_1:
#          print('ожирение')
#
# imt(1.68,56)

#dz2
# def figyra(*figyr):
#       fig = int(input('vvesti kol-vo storon: '))
#       if fig == 3:
#          print('treygolnik')
#       elif fig <= 5:
#          print('pr9moyg')
#       elif fig <=10:
#          print('kryg')
#       else:
#           print('bolwoi diapozon')
# figyra(3)

#dz3
# import datetime
# # def data(year,month,day):
# #
# #
# # print(data)
#dz4
# def shop(a):
#     price = 10.95
#     price_2 = 2.95
#     if a == 1:
#        res = price
#     elif a>= 2:
#         res = price+price_2*2
#     return res
# print(shop(3))

# import fractions
# #dz5
# def drob(a,b):
#     a = int(input(' введите числитель: '))
#     b = int(input(' введите знаменатель: '))
#     res = fractions.Fraction(a,b)
#     return res
# print(drob(6,63))


#dz6
# def dz6(a):
#     print(a[::-1])
#     print(sorted([i for i in a if isinstance(i, str)]))
#     print(sorted([i for i in a if isinstance(i, int)], reverse=True))
#     print(a[2:8])
#     del a[5]
#     print(set(a))
# print(dz6([1,3,5,6,'qesd','qw12',13,14,56,]))

#dz7
# def count_range(lst, a, b):
#     x = 0
#     for i in lst:
#         if a <= i < b:
#             x += 1
#     return x
#
# print(count_range([0, 5, 9, -1, -8.1, 5, -5, -1,-9, 1], -7, 6,))
#dz8
# def list_1(lst):
#     s = 0
#     for i in lst:
#         if type(i) is list:
#             s += 1
#     return s
# print(list_1([1,2.3, [0, 'asdgh'], []]))
#dz9
# def angr(a,b):
#     return sorted(a) == sorted(b)
# print(angr('evil','live'))
def mobile(phrase):
    letters = {'1':'.,?!:','2':'abc', '3':'def','4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs','8':'tuv', '9':'wxyz','0':' '}
    for s in phrase.lower():    # перебор по символам введеной фразы
        for key in letters: # перебор элементов словаря
            if s in letters[key]:    # ищем вхождение символа в элементе
                for x in letters[key]: # перебор по найденному набору символов
                    if x == s:
                        print(key, end='')
                        break
                    else:
                        print(key, end='')
mobile('HHHello world')