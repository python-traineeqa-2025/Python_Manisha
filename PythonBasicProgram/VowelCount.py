from re import A

word = input("Enter the string to check the vowels")

count = 0

for i in word.upper():
    if i == 'A' or i == 'E' or i== 'I' or  i=='O' or i=='U':
        count +=1

print("the vowel count is :",count)

















