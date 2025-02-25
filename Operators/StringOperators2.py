a = 'car'
b = 'apple'

c= 'Hello my name is manisha'
print(c.split(' ')) #split into the list
print('.'.join(c))  #join with the separator

print(a.startswith(c)) #check if starts with c or not
print(a.endswith(b)) #checks if ends with b or not


print(a.isalpha()) #returns true if it is alphabets
print(a.isdigit()) #returns true if it is digit
print("123".isdigit()) #true
print("race12".isalnum()) #returns true since it is (alphanumeric)


#string formating
name = "mansia"
age = 23

print(f"my name is {name} ans age is {age}") #formating string
print("my name is {} and age is {}".format(name, age)) #.format
print("My name is %s and i am %s years old"%(name,age)) #% formating


#finding substrings
print(b.find("mnaisha")) #index of substring (-1 if not found)
print(b.index("name")) #similar to find( but raises if not found
print(a.count('r')) #count the no of 'r' present in the string


#escpae character
print("hello\nmanisha") #newline
print('hello\t manisha') #tab space
print('herlloooo \\ manisa') #backslash
print("he said \"hello\"") #escape quotes

#checking Case Condition
print("hellp".isupper())
print("hello".islower())

#Reversing the string without slicing by using joins
print(''.join(reversed(a)))


#String Multiplication with nextline
print('hello\n'*3)