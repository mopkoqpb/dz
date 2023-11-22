# with open('zadanie_4.txt','r') as f:
#     line = 0
#     for i in f:
#         line += 1
#         print(i.strip(),len(i.strip()))
#         print(line)
# f.close()
#
import csv

# my_f = open('example_csv', encoding='utf-8')
# my_reader = csv.reader(my_f, delimiter=',')
# data = list(my_reader)
# print(data)
# print(data[0][0])
# for i in data:
#     # for x in i:
#     #     print(x)
#     print(i[0])

# f = open('data.csv','w', encoding='utf-8', newline='')
# data_writer = csv.writer(f,delimiter=';')
# my_data = [['20.11', ' python', ' 15'], ['21.11', ' c++', ' 5'], ['22.11', ' django', ' 10']]
# for row in my_data:
#     data_writer.writerow(row)
# f.close()

import json
# import demjson

# my_str = '{"id":1, "name": "andrey", "age": 28}'
# data = json.loads(my_str)
# print(type(data))
# print(data['age'])
# print(data['id'])

# with open('data_1.json', encoding='utf-8') as f:
#     data_1 = json.load(f)
# print(data_1['id'])

# my_dict = {"id": 11, "phone": 123, "addr": 'минск'}
# my_s = json.dumps(my_dict)
# print(my_s)
# my_s = json.dumps(my_dict,ensure_ascii=False)
# print(my_s)

# my_dict = {"id": 11, "phone": 123, "addr": 'минск', "name": 'andrey' }
# with open('data_my_dict.json','w',encoding='utf-8') as f:
#     json.dump(my_dict,f)

# my_dict = {"id": 11, "phone": 123, "addr": 'минск', "name": 'andrey' }
# with open('data_my_dict.json','w',encoding='utf-8') as f:
#     json.dump(my_dict,f,ensure_ascii=False)


# with open('dz_15.json','w',encoding='utf-8') as f:
data = {}
product = []
price = []
while True:
    name_product = input('enter name product: ')
    if name_product == 'stop':
        break
    price_product = int(input('enter price product: '))
    product.append(name_product)
    price.append(price_product)
    data = dict(zip(product,price))
    print(data)
with open('dz_15.json','w',encoding='utf-8') as f:
    json.dump(data,f)

with open('dz_15',encoding='utf-8') as f:
    dz_15 = json.load(f)
price_product = 0
for i in price:
    price_product += i
    print(price_product)
