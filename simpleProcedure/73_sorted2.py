foo =  [-5,8,0,4,9,-4,-20,-2,8,2,-4]

a = sorted(foo, key=lambda x:(x<0, abs(x)))
print(a)

s = ['ab', 'abc', 'a', 'djkj']
b = sorted(s, key=lambda x:len(x))
print(b)