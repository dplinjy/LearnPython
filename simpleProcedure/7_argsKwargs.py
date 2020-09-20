def demo(args_f, *args_v):
    print(args_f)
    print(type(args_v))
    for x in args_v:
        print(x)


demo('a', 'b', 'c', 'd', 'e')


def demo2(**args_v):
    for k, v in args_v.items():
        print(k, ": ", v)


demo2(name='sdxbnkjh')


def demo3(args_f, default_v=123,  *args_v, **args_v2):
    print('位置参数：')
    print(args_f)

    print('默认参数')
    print(default_v)
    print('*args参数（即可变参数--被当做元组处理）')

    for x in args_v:
        print(x)

    print('**kwargs参数（被当做字典处理）')

    for k, v in args_v2.items():
        print(k, ": ", v)


print('------------------------------------------------')

demo3(['a', 'a2', 'a3'], 100, 'c', 'd', 'e', name='h', age='h2')


def print_hello(name, sex):
    print('hello %s %s, welcome to python world!' % (name, '先生'))


print_hello('Nick', '先生')
# 输出：hello Nick 先生, welcome to python world!


# # 按照顺序为函数形参传值
# def msg(name, age, sex):
#     print("Hello, your name is %s, age is %s, sex is %s" % (name, age, sex))
# msg('Nick', 23, 'male')
# # 输出：Hello, your name is Nick, age is 23, sex is male
#
# # 有位置参数和关键字参数时，关键字参数在位置参数后面
# msg('Tony', 12, sex='male')
#
# # 参数中有多个关键字参数时，关键字参数不分先后顺序
# msg(sex='female', name='Amy', age=56)


#
# def func(*args):
#     print(type(args))  # 传入的参数会被视作一个元组
#     print(args)
#     for x in args:
#         print(x)
# func(1)
# func(1, 2, 3)
# # 输出：
# # <class 'tuple'>
# # (1,)
# # 1
# # <class 'tuple'>
# # (1, 2, 3)
# # 1
# # 2
# # 3


# def func(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(k, ": ", v)
#
# func(a=1)
# func(a=1, b=2, c=3)
# # 输出：
# # <class 'dict'>
# # {'a': 1}
# # a :  1
# # <class 'dict'>
# # {'a': 1, 'b': 2, 'c': 3}
# # a :  1
# # b :  2
# # c :  3

# def func(name, age, sex=1, *args, **kwargs):
#     print(name, age, sex, args, kwargs)


def func(name, age, sex=1, *args, **kwargs):
    print('位置参数：')
    print(args)

    print('默认参数')
    print(sex)
    print('*args参数（即可变参数--被当做元组处理）')

    for x in args:
        print(x)

    print('**kwargs参数（被当做字典处理）')

    for k, v in kwargs.items():
        print(k, ": ", v)


func('Cate', 14, 0, 'friendly', 'talented', 'easy-going', company='Apache', salary=30000)
# 输出：
# 位置参数：
# ('friendly', 'talented', 'easy-going')
# 默认参数
# 0
# *args参数（即可变参数--被当做元组处理）
# friendly
# talented
# easy-going
# **kwargs参数（被当做字典处理）
# company :  Apache
# salary :  30000