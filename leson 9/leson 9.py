import random

# from leson_8 import leson8
# leson8.func()
#
# my_lst = [random.randint(0,19)for i in range(6)]
# my_lst1 = [i*100 for i in range(6)]
# lst_1 = ['hello']
# lst_1.append('world')
# lst_1.insert(1,'12313')
# lst_1[0] = 'qwe'
# print(lst_1)
ll = [1,'2',3,['11','22'],False]
# del ll[3][0]
# print(ll)
# del ll[0:3]
# print(ll)
# if 2 in ll:
#     ll.append('fire')
# else:
#     print('warning')
# print(ll)

# y =[['misk','zavo', '8'],
#     ['minsk','libknehta','68'],
#     ['nezav','117a']]
# for adr in adresses:
#     if'minsk' in adr:
#         adresses = ''.join(adr)
#     else:
#         adr.insert(0,'minsk')
# print(adresses)


# l1 = [1,2,3]
# l2 = [4,5,6,]
# res = l1+l2
# print(res)
# l1.append(l2)
# print(l1)
# l3 = [7,8,9]
# l2.extend(l3) #расширяет список
# l2.extend() #расширяет список на все эллементы
# print(l2)
#
# a= [1,2,3,4]
# b = a
# print(id(a))
# print(id(b))
# a.append(5)
# b.append(6)
# print(a, id(a))
# print(b, id(b))

# my_l1 = [1,2,3]
# my_l2 = my_l1.copy()
# print()
# import copy
# my_l3 = copy.copy(my_l1)
# my_l4 = copy.deepcopy(my_l1)
# my_l5 = list(my_l1)
# print(my_l3, id(my_l3))
# print(my_l4, id(my_l4))
# print(my_l5, id(my_l5))

#
# o = []
# for pos in [['gr',100],['yab',200],['ap',300]]:
#     o.append(pos[0])
# print(o)
import random
#
# lst = [random.randint(0,100) for _ in range(10)]
# print(lst)
# lst.reverse()
# print(lst)
# print(lst[::-1])

# lst = [random.randint(0,50)for _ in range(50)]
# print(lst)
# ind = lst.index(20)
# lst[ind] = 200
# print(lst)
#
# a = [5,[1,2,],2,'r',4,'ee']
# b = [4,'we','ee',3,[1,2]]
# res = []
# for i in a:
#     if i in b:
#         res.append(i)
# print(res)

a = [4,6,'pу','tell',78]
b = [44,'hello',56,'exept',3]
# a.extend(b)
# print(a)
# a.insert(3,6)
# b.insert(3,6)
# print(a,b)
for i in b:
    if str(i).isalpha():
        b.remove(i)
print(b)
