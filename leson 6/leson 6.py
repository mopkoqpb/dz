# for i in range(10):
#     print(i)
# for i in 'Я учу пайтон':
#     print(i)
# for i in range(15, 0, -1):
#     print(i)

# a = input('введите строку')
# b = input('введиет символ')
# c = ''
# for i in a:
#     if i != b:
#         c += i
# print(c)

# for i in range(100,999,100):
#     # if i // 100:
#     print(i)
# for i in range(94, 351):
#     if i % 5 == 0:
#         print(i)

# for num in range(10):
#     print(num)
#     if num == 7:
#         print
#         break
# print('asdasd')


# for num in range(10):
#     print(num)
#     if num == 7:
#         print
#         continue
# print('asdasd')
# my_str = input('vvesti')
# symb = input('symb')
# new_str =''
# for i in my_str:
#     if i == symb:
#         continue
#     new_str += i
# print(new_str)
import math
#
lst = [1,2,3,4,6,'hello']
chet = []
nechet = []
for n in lst:
    if n % 2 == 0:
        chet.append(1)
    else:
        nechet.append(1)
##
if len(chet)>len(nechet):
    print('chet win:', math.fsum(lst))
else:
    print('nechet win:', lst[0]*lst[2])

# lst = [1,2,3,4,5,6,7]
# pr = 1
# sum = 0
# for n in lst:
#     sum += n
#     pr *= n
# print(pr)
# print(sum)

