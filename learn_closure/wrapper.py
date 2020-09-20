def outer(func):
    def inner():
        print("记录日志开始")
        func()  # 业务函数
        print("激励日志结束")
    return inner

@outer
def foo():
    print("foo")


foo()