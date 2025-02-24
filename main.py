#keyword

import keyword

print(keyword.kwlist)

snake_case = [] #varaible ko name set garda use garcha
camel_case = []  #Class set garda use garcha.

#Datatypes
#INT, float, string, boolean, list, tuple, set and dictionary

#input
a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))

cal = int(input("option1:add option2: Subtract option3:Multiplication"))

if cal == 1:
    print(a+b)
elif cal == 2:
    print(a-b)
else:
    print(a*b)
