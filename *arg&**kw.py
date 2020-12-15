"""
what's *args **kwargs

*args: 位置参数
**kwargs(**kw) ：关键字参数
当不知道传参数量时可以使用
"""


# eg
def func1(first, *args, **kw):
    print("Required parameter: ", first)
    for v in args:
        print("Optional parameter: ", v)
    for k, v in kw.items():
        print("Optional argument's key: %s value: %s " % (k, v))


func1(1, 22, 33, 44, k1=55, k2=66)

