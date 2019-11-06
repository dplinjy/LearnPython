import re

string_ = "ruby 43224 rube"

searchObj = re.search(r'ruby (.?) rube', string_)

if searchObj:
    print(searchObj.group())
    # print(searchObj.group(1))
    # print(searchObj.group(2))
else:
    print("No match!")
