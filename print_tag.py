def tag(tag):
    def decorator(func):
        def wrap(*args, **kwargs):
            result = func(*args, **kwargs)
            return f'<{tag}>{result}</{tag}>'
        return wrap
    return decorator

@tag('b')
@tag('i')
def hello():
    return 'hello'
hello()
