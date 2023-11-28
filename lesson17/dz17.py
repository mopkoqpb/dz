class Dz_17():
    def __init__(self,a):
        self.a = a
    def func(self):
        glasn = 0
        soglasn = 0
        summ = 0
        if type(self.a) is str:
            for y in self.a:
                if y == 'a' or y == 'e' or y == 'i' or y == 'u' or y == 'y':
                    glasn = glasn + 1
                else:
                    soglasn = soglasn + 1

            if glasn * soglasn <= len(str(self.a)):
                return glasn
            else:
                return soglasn


        elif type(self.a) is int:
            for i in str(self.a):
                if int(i) % 2 == 0:
                    summ += int(i)
            return summ * len(str(self.a))
    def func_2(self):
        return len(str(self.a))


dz17 = Dz_17('aaaaaaa')
print(dz17.func())
print(dz17.func_2())