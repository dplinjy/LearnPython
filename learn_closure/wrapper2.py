def tag(func):
    def wrapper(text):
        value = func(text)
        return "<p>" + value + "</p>"
    return wrapper


def tag2(func):
    def wrapper(text):
        value = func(text)
        return "<p>" + value + "</p>"
    return wrapper

# @tag
def my_upper(text):
    value = text.upper()
    return value

print(my_upper("hello"))

my_upper = tag(my_upper)

print(my_upper("hello"))

@tag2
def my_upper2(text):
    value = text.upper()
    return value

print(my_upper("hello"))