
word = str(input("Enter a word that you want to check the palindrome"))
reverse = word[::-1]
print(reverse)

if  str(reverse) == str(word):
    print("Palindrome")
else:
    print("Not palindrome")

#number
print('Enter the number that you want to check palindrome')

number = int(input())
temp = number
rev = 0

while number> 0:
    digit = number % 10
    rev = rev * 10 + digit

    #it will remove the last digit from the number
    number = number // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")





