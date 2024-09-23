i = 4
while i< 10:
    if i == 7:
        i=i+1
        continue
    print(i)
    i += 1
    
# #break

i = 1
while i<6:
    print(i)
    if i == 3:
       break
    i = i+1
    

#continue

i = 0
while i<6:
    i=i+1
    if i == 3:
        continue
    print(i)
    
#else

i = 1
while i<6:
    print(i)
    i=i+1
else:
    print("i is no longer than 6")

for i in a:
    if i > 0:
        print(i)
    elif i < 0:
        print(i)
    elif i == 0:
        print(i)
