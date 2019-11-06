# encoding: UTF8
import re

pattern = re.compile(r'\d+')
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)


text = "JGod is a handsome boy ,but he is a ider"
print(re.findall(r'\w*o\w*', text))

text2 = 'adfs343kdgh'
print(re.findall(r'[a](.+?)[h]', text2))


regex = re.compile(r'\w*o\w*')
print(regex.findall(text))

