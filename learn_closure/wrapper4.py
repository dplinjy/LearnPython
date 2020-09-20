import logging
# 以下实现均为为函数foo增加日志打印功能

# 方法一：简单粗糙实现法
# def foo():
#     print("I am foo")
#     logging.info("foo is running.")

# 方式二：在一的基础上升级
# def foo():
#     print("I am foo")
# def use_logging(func):
#     logging.warn("%s is running" % func.__name__)
#     func()
# use_logging(foo)

# 方法三：在二的基础上升级
# def use_logging(func):
#     def wrapper():
#         logging.warn("%s is running" % func.__name__)
#         return func()
#     return wrapper
# def foo():
#     print("I am foo")
# foo = use_logging(foo)
# foo()

# 方法四：在三的基础上升级
# def use_logging(func):
#     def wrapper():
#         logging.warn("%s is running." % func.__name__)
#         return func()
#     return wrapper()
# @use_logging
# def foo():
#     print("i am a foo")
# foo()

# 方法五：在四的基础上为装饰器函数引入参数
def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running" % func.__name__)
            elif level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args)
        return wrapper
    return decorator
@use_logging(level="warn")
def foo(name="foo"):
    print("I am %s" % name)
foo()

