lis = [[1,2],[3,4],[5,6]]
for i in lis:
    print(i)

x = [j for i in lis for j in i]
print(x)