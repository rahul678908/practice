a = [10,-5,0,7,-3]
positive = []
negative = []
zero = []

for i in a:
    if i>0:
        positive.append(i)
        print('positive number:', positive)
    elif i<0:
        negative.append(i)
        print('negative number:', negative)
    elif i==0:
        zero.append(i)
        print('zero:', zero)


# print('negative number:', negative)
# print('zero:', zero)
        



# a = [10,-5,0,7,-3]

# positive = [i for i in a if i>0]
# negative = [i for i in a if i<0]
# zero = [i for i in a if i==0]

# print("positive", positive )
# print("negative", negative)
# print("zero", zero)
