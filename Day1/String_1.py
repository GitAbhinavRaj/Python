#Anything inside "" or'' or ''' '''  is string
language = "Python Java C++"
print(type(language))

language2 = 'Hello Python'
print(language2)

language3 = '''Hi 
How Are
You! '''
print(language3)

#String Slicing
str1 = "Hello World"   #length is : 11
print(str1)
print(str1[:])
print(str1[:5])
print(str1[6:])
print(str1[1:7])

#negative slicing
print(str1[::-1]) #reverse whole string
print(str1[-5:])
print(str1[-5:-2])   # len(str1)-5 : len(str1)-2   = 11-5 : 11-2 = 6:9  (Wor)


