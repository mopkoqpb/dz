import json
spisok_pokypok = {}
spisok_pokypok['name_product'] = []
spisok_pokypok['price product'] = []
while True:
    name_product = input('enter name product: ')
    if name_product == 'stop':
        break
    price_product = int(input('enter price product: '))
    spisok_pokypok['name_product'].append(name_product)
    spisok_pokypok['price product'].append(price_product)

    print(spisok_pokypok)
with open('dz_15.json','w',encoding='utf-8') as f:
    json.dump(spisok_pokypok,f)

with open('dz_15',encoding='utf-8') as f:
    dz_15 = json.load(f)
price_product = 0
for i in spisok_pokypok['price product']:
    price_product += i
    print('purchases per day: ',price_product)