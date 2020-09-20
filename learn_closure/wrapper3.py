def tag(name):
    def decorator(func):
        def wrapper(text):
            value = func(text)
            return "<{name}>{value}</{name}>".format(name=name, value=value)
        return wrapper
    return decorator


@tag("div")
@tag("p")
def my_upper(text):
    value = text.upper()
    return value

print(my_upper("hello"))
