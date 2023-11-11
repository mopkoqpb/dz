lst = [15, 48, 'hello', 6, 19, 'world']
summ = 0
res = []
for i in lst:
    if type(i) == str:
        res.append(lst)
        lst.remove(i)
        print(lst)

print(lst)
print(summ)
print(res)



# for y in lst:
#     if y == 'a' or y == 'e' or y == 'i' or y == 'u' or y == 'y':
#         sum = sum + 1




#