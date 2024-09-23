# a = [1,2,3,4,5,6,7,8,9]
# b = len(a)// 2
# print(b)
# c = b
# d = a[:b]
# e = a[b:]
# print(d)
# print(e)
# f = e[::-1]
# print(f)

while True:
    a = int(input("Enter any number : "))
    b = int(input("Enter the 2nd number : "))
    c = input("Enter the operator : ")

    if c == '+':
        print(a + b)
    elif c == '-':
        print(a - b)
    elif c == '*':
        print(a * b)
    elif c == '/':
        print(a/b)
        break