# s_1 = 'hello '
# s_2 = 'world'
# s_res = s_1+s_2
# print(s_res)

# n_1 = 1
# n_2 = 2
# print(n_1+n_2)
#
# n_3 = ' 1'
# n_4 = '3'
# print(n_3 + n_4)
# s_1 = 'hello '
# s_2 = 'world'
# s_res = s_1+s_2
# print(s_res)
#
# s_1 = 'hello '
# print(len(s_1))
#
# n_1 = input('Как вас зовут: ')
# print('hello  '+ n_1)
# print(n_1*3)


# s_1 = 'helo'
# print(len(s_1))
# print(s_1 [1], s_1[0], s_1[-1], s_1[len(s_1)-1])
#
# s = 'hello'
# print(s[1:4], s[0:5]) #не включаем конечный индекс
# print(s[1:3])
# print('0123456'[0:7:2]) #do 7   num
# print('0123456'[2:5:3]) # do 5 num
# print('0123456'[::-1]) #в обратном не пишем "0"

# s11 = s[2:4]
#print(s11)
# import random
# n1 = random.randint(100, 999)
# print(n1)
# n1 = str(n1)
# print(int(n1[0])+int(n1[1])+int(n1[2]))

# s = '0123456'
# print(s[:6:2])
#
s = 'hello world'
# print(s.capitalize())
# print(s.title())
# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(s.isupper())
# print(s.islower())
# print(s.istitle())
# print(s.isalpha())   #только буквы
# print(s.isdigit())    #только цифры

# #
# data = input('data')
# if data.isdigit() and len(data) == 2:
#     print(int(data[0])+int(data[1]))
# else:
#     print('byw')
# #
# s = input('vvedite stroky: ')
# # print(s[::3])
# # print(s[0]+s[-1])
# # print(s.upper())
# print(s[::-1])
# print(s.isdigit())

# print('h'.join('llo'))# резделяем join

# print('hello world'.split('world'))(''.join('hello'))#из строки в список int
# print('hello'.startswith('f'))   #с данного символа
# print('hello'.endswith('o'))
# print('hello'.find('o'))
# print('helleo'.rfind('e')) #последнию
# print('hello'.replace('e', 'k'))






# s = 'hello1 world'
# s1 = s.split('world')
# s2 = s.split('hello1')
# s3 = ' '.join(s2+s1)
# print(s3)

#dz4-4
# s = input('hello world: ')
# s = s.split(' ')
# s = ''.join(s)
# print(s)

# s = input('введите строку: ')
# s1 = ''.join(s.split(' '))
# print(s1)

# number = 1
# while number < 5:
#     print('number = 5')
#     number += 1
# print("Работа программы завершена")

# i = 1
# j = 1
# while i < 10:
#     while j < 10:
#         print(i * j, end="\t")
#         j += 1
#     print("\n")
#     j = 1
#     i += 1

