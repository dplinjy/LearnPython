# encoding: UTF8

try:
    open('dfdf.txt', 'r')
    # print()
except FileNotFoundError as errorMsg:
    print('产生错误了：%s' % str(errorMsg))
else:
    print('没有捕获到异常，则执行该语句')


try:
    # num = 100
    # print(num)
    open('3fjkd.txt', 'r')
except FileNotFoundError as errorMsg:
    print('产生错误了： %s' %errorMsg)
finally:
    print('不管有没有捕获异常，都执行该语句')

