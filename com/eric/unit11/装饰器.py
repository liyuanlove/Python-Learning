import functools

def w1(func):
    def inner():
        print("--正在验证权限")
        func()

    return inner


def myLog(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


def myLog2(text):
    def decorator(func):
        @functools.wraps(func)
        def wapper(*args, **kw):
            print('%s %s():' %(text, func.__name__))
            return func(*args, **kw)
        return wapper
    return decorator


@myLog2("asd ")
def now():
    print("2018-2-26 10:14:13")


def w2(func):
    def inner(userName, passWord):
        print("--正在验证登录" + userName + passWord)
        func()

    return inner


@w1
def f1():
    print("---f1---")


@w2
def f2():
    print("---f2---")


now()
