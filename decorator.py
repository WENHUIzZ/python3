import time

"""
装饰器 decorator
"""


def time_logger(flag=0):  # 对原有的装饰器进行了进一步的封装，并返回了一个有参数的装饰器。
    def showtime(func):  # 原有的装饰器
        def wrapper(a, b):  # 被装饰的函数
            start_time = time.time()
            func(a, b)
            end_time = time.time()
            print('spend is {}'.format(end_time - start_time))

            if flag == 0:
                print("writing...")

        return wrapper

    return showtime


@time_logger()
def foo(a, b):
    print('foo..')
    print(a + b)
    time.sleep(3)


@time_logger(2)
def doo(a, b):
    print("doo.....")
    print(a + b)
    time.sleep(5)


# foo = showtime(foo)  # 先传入 showtime 这个函数
foo(1, 2)  # 再运行本身函数
doo(4, 5)


class Foo:
    """类装饰器"""
    def __init__(self, func):
        self.func = func

    def __call__(self):
        start_time = time.time()
        self.func()
        end_time = time.time()
        print('spend is {}'.format(end_time - start_time))


@Foo
def bar():
    print("bar...")
    time.sleep(2)


# bar()
