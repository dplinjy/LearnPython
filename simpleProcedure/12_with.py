# # encoding: UTF8
# import json
#
# # f = open("../learn_file/demo.txt", "wb")
# f = open(file="demo.txt", mode='a+', encoding='UTF-8')
# try:
#     # d = {"name": "Amy"}
#     # f.write(json.dumps(d))
#     f.write("保护")
# except:
#     pass
# finally:
#     f.close()

# with open(r'../learn_file/file_to_read.txt', encoding='UTF-8', mode='r+') as fb:
#     while True:
#         content = fb.readline().replace('\n', '')
#         # content = fb.readlines()
#         # if not content:
#         #     break
#         if content:
#             print(type(content), content)
#         else:
#             break
#         # print(type(content))
#         # print(type(content), content)
#     print(fb.name)




#
# with open(r'../learn_file/file_to_read.txt', encoding='UTF-8', mode='r+') as fb:
#
#     content = fb.readline().replace('\n', '')
#         # content = fb.readlines()
#         # if not content:
#         #     break
#         # print(type(content))
#     print(content)
#     print(fb.name)


# with open(r'../learn_file/file_to_read.txt', encoding='utf-8', mode='r') as fb:
#     content = fb.read()
#     print(type(content))
#     print(content)

with open(r'../learn_file/file_to_read.txt', encoding='utf-8', mode='r') as fb:
    content = fb.readlines()
    print(type(content))
    for line in content:
        print(type(line), line.replace('\n', ''))
# 输出
# <class 'list'>
# <class 'str'> line 1: Hello, Mike.
# <class 'str'> line 2: Nice to meet you. I'm Nick.
# <class 'str'> line 3: Welcome to Shenzhen.
# <class 'str'> line 4: Thx, it is really a beautiful city. I enjoy my time here.
# <class 'str'> line 5: It is. Shall we go for some coffee this afternoon.
# <class 'str'> line 6：Sure. And I want to discuss some details about the project we're going to work for.

