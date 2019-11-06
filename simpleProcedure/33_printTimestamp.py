import datetime

a = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ' 星期：' + str(datetime.datetime.now().isoweekday())
print(a)