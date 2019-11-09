import json
import pickle

fd = open('test.json', 'r', encoding='UTF-8')

data = json.load(fd)

print(data)
fd.close()

fs = open('test2.json', 'r')
data2 = json.load(fs)
print(data2)
fs.close()

