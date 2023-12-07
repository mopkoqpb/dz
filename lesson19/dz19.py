def debug(func):
    def wrap(*args,**kwargs):
        print('Имя функции: ', func.__name__, 'ее аргументы',*args,{**kwargs})
        res = func(*args,**kwargs)
        print('Вернул значение', func.__name__, res)
        return res
    return wrap
@debug
def mf(*args):
    x = sum(args)
    return x

mf(1,23,3,5,6)

