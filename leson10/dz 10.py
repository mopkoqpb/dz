#dz 4
# dict1 = {'n1': 23 , 'n2': 45, 'n3': 67, 'n4': 478}
# res = 1
# for key in dict1:
#     res *= dict1[key]
# print(res)

#dz 5
# l_1 = ['hello', 'name', 'data', 'home']
# l_2 = ['world', 's_name', '02-11-2023','work']
# dict2 = dict(zip(l_1, l_2))
# print(dict2)

#dz6
# a = 'pyythoonist'
# dict3 = {i: a.count(i) for i in a}
# print(dict3)

# #dz
# product = {'meat':[250,300],
#            'chicken':[180,250],
#            'apple':[70,120],
#            'fish':[57,123]}
# for key in product:
#     print(key, '-', product[key][0], '-', product[key][1])
# for items in product:
#     name_product = str(input('введите название продукта: '))
#     kolichestvo = int(input('введите количество товара: '))
#     price = 0
#     ostatok = 0
#     if name_product == 'n' or kolichestvo == 'n':
#         break
#     elif kolichestvo > product[name_product][1]:
#              print('не хватает товара')
#              break
#     elif name_product in product:
#         price = product[name_product][0] * kolichestvo
#         print('цена за ', kolichestvo, name_product, 'равна:', price)
#         if name_product in product:
#             ostatok = product[name_product][1] - kolichestvo
#             print('остаток това на складе: ', ostatok)
#             break
# print('всего доброго!')
















