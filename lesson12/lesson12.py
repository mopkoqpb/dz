# def my_f(*args, **kwargs):
#     print(args)
#     print(kwargs)
# my_f(0,1,2, name ='andrey', age = 28)


# def factor(x):
#     if x != 0:
#         return x* factor(x-1)
#     else:
#         return 1
# print(factor(x=5))

# def add(a,b):
#     return a+b
# print(add(1,2))
#
# data = add(3,4)
# print(data)
# add_1 = add
# print(add_1,type(add_1))
# add_2 = add
# print(add_2,type(add_2))
# add_3 = add
# print(add_3,type(add_3))


# def sq(x):
#     return x*x
# print(sq(2))
# squa = sq
# print(squa(3))

# def func_1(x):
#     def func_2(y):
#         return x*y
#     return func_2
#
# print(func_1(2)(41))
# func_3 = func_1(5)
# print(func_3(34))

# def razr(a):
#     i = 0
#     while a > 0:
#         a = a //10
#         i += 1
#     return i
# print(razr(264))
# import random
# #
# #
# def mass11():
#     my_list = [random.randint(1, 100) for i in range(10)]
#     polz1 = str(input('введите число: '))
#     pol2 = str(input('введите число: '))
# print(mass11)
# def seco(sec):
#     dni = sec //(24* 3600)
#     sec = sec % (24 * 3600)
#     hours = sec // 3600
#     sec
#     min = sec /60
#     seconds = sec /
#     return [dni,':',hours,':',min,':',seconds]
#
# print(seco())

def stringg(lst):
    glasn = 0
    soglasn = 0
    for y in lst:
        if y == 'a' or y == 'e' or y == 'i' or y == 'u' or y == 'y':
            glasn = glasn + 1
        else:
            soglasn = soglasn+1
    return ('soglasnix: ',glasn,'glasnix',soglasn)
print(stringg('asdfregc'))



