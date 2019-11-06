import re

string_ = "匹配规则这个字符串是否匹配"

searchObj = re.search(r'配$', string_)

if searchObj:
    # print(searchObj)
    print(searchObj.group())
    # print(searchObj.group(1))
    # print(searchObj.group(2))
else:
    print("No match!")
