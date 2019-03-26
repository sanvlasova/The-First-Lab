def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """
 
    func.__invocation_count__ = 0
 
    def wrap(*args, **kwargs):
        func.__invocation_count__ += 1
        res = func(*args, **kwargs)
        print("{0} была вызвана: {1}x".format(func.__name__, func.__invocation_count__))
        return res
    return wrap
@counter
def foo(a, b):
    return a + b
foo(3, 4)
foo(5, 6)
foo(10, 22)
