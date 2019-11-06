# encoding: UTF8

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry']

sortedFruits = sorted(fruits, key=lambda word:word[::-1])
# sortedFruits = sorted(fruits)

print(sortedFruits)