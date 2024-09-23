a = [6,2,8,9,4]
b = [1,3,6,7,2]
c = a+b
print(c)
d = c[0]

for i in c:
    if i>d:
        d = i
print(d)
