def parent(func):
    def inner(*args, **kwargs):
        print("parent")
        return func(*args, **kwargs)
    print(func.__name__, "has been called")
    return inner


@parent
def child():
    print("child", )
    return 12


@parent
def child2():
    print("child2", )
    return 12


@parent
def child3():
    print("child3", )
    return 12


child()
child2()
child3()
