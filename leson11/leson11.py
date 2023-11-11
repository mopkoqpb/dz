# def f(l=[]):
#     l.append(1)
#     return l
# print(f([1]))
# print(f([2]))
# print(f([3]))
import random
# a = tuple(random.randint(1,100) for i in range(10))
# # a = (1,23,4,5,6,7,6,54,234,2)
# print(a)
# print(max(a),min(a))

# a = tuple(random.randint(1,100) for i in range(5))
# b = tuple(random.randint(-5,0) for i in range(5))
# print(a)
# print(b)
# c = a + b
# print(c)
# print(c.count(0))
#
# a = ('asd','retgdf','trmvkzxcz')
# print(','.join(a))

# a = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
# b = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
# sum_a = sum(a)
# sum_b = sum(b)
# if sum_a > sum_b:
#     print('сумма больше в:',sum_a)
# else:
#     print('сума больше в:',sum_b)
# print((min(a),a.index(min(a))))
# print(min(b),b.index(min(b)))

# my_set = {1,2,3,4}
# my_list = [1,2,2,2,2,3,3,3,4,5,6,7,0,8,8]
# otig = set(my_list)
# print(my_set)
# print(otig)
# a = ['asd','retgdf','asd', 'trmvkzxcz']
# b = set(a)
# print(b)
# s_a = {1,2,3}
# s_b = {3,4,5}
# print(s_a-s_b)
# print(s_b-s_a)

# a = [1,2,3,4,5,5,6,7,6]
# b = set(a)
#
# print(len(b)==len(a))
#1
a = [1,2,3,4,5,5,6,7,6]
b = set(a)
print(b)
#2
c = frozenset(a)
print(c)
#3
print(b|c)
#4
print(b&c)






