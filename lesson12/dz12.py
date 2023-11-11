# a = ('a', 1,3,4,'daw','qw' ,1)
# b = ['a', 1,3,4,'daw','qw' ,1]
# c = 123141235
# d = 'this is word'


a = ('a',1,3,4,'daw','qw',1)
res = 0
for i in str(a):
    res += str.isalpha(i)
print(res)

b = ['a',1,3,4,'daw','qw',1]
word = 0
num = 0
for i in str(b):
    word += str.isalpha(i)
    num += str.isdigit(i)
print(word, num)


c = 123141235
nechet = 0
for i in str(c):
    if int(i) % 2 != 0:
        nechet += 1
print(nechet)

d = 'thisisword '
kolvo =
for i in str(d):
    kolvo += str.isalpha(d)
print(kolvo)
