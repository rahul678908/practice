# lists

my_lists = [5,10,15,20]
print(my_lists)

#single dimensional

print(my_lists[0])
print(my_lists[2])

#negative indices

print(my_lists[-1])

#multi dimesional

my_lists2 = [[1,2,3],"ABCD",[4,5,6]]
print(my_lists2)
print(my_lists2[0][0])
print(my_lists2[2])
print(my_lists2[1])

# adding elements to a list

#append()method

languages = ['c','c++','java']
languages.append(['python','javascript'])
print(languages)
languages.append('http')
languages.append('html')
languages.append('ruby')
print(languages)

#insert()method

languages = ['c','c++','java']
languages.insert(0, 'python')
print(languages)

#extend()method

languages = ['c','c++','java']
more_languages = ['python','javascript']
languages.extend(more_languages)
print(languages)

#input()method

name = input('john')
print(name)

#input()method with a message

number = input('Enter a number : ')
print(number)

#typecasting the user input

number = input('Enter your number : ')
print(number)
print(int(number))

