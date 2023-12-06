def debug(func):
    def wrap(*args,**kwargs):
        print('Name func: ', func.__name__, 'call',*args,**kwargs)
        res = func(*args,**kwargs)
        print(res)
        return res
    return wrap
@debug
def mf(x):
    return x
mf(1)

