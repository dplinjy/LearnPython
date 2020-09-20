# -*- encoding: utf-8 -*-
"""
@File    : 73_getPrimeNumber.py
@Time    : 2019/11/17 17:36
@Author  : Ldp
@Email   : dplinjy@163.com
@Software: PyCharm
------------------------------------
题目： 获取 100 以内的质数。
程序分析：质数（prime number）又称素数，有无限个。质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数的数称为质数，
如：2、3、5、7、11、13、17、19。
"""

num = []
i = 2

for i in range(2, 20):
    # j = 2
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        num.append(i)
print(num)

# count = 0
# while count < 5:
#     print(count, "smaller than 5")
#     count += 1
# else:
#     print(count, "bigger than or equals 5")

sites = ["Baidu", "Google", "Runoob", "Taobao"]

for site in sites:
    # print("循环数据：" + site)
    if site == "Runoob":
        print("菜鸟教程")
        break
    print("循环数据：" + site)
else:
    print("没有循环数据")
print("完成循环")
