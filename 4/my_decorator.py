def my_simple_decorator(function_to_decortor):
    def wrapper_around_our_function():
        return wrapper_around_our_function

def stable_function():
    return 'Hello World!'
print(stable_function())

def decorator_with_arguments(function):
    def wrapper_with_arguments(*args, **kwargs):
        function(*args, **kwargs)
    return wrapper_with_arguments

@decorator_with_arguments
def print_full_name(first_name, last_name):
    print('My name is', first_name, last_name)
print_full_name(u'Alexandra', u'Sadikova')

import time
def my_timer(f):
    def wrap(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        delta_time = time.time() - start_time
        print('Run time function %f' % delta_time)
        return result
    return wrap
@my_timer
def my_favorite_number(x):
    return x
print('My favorite number is', my_favorite_number(5))

