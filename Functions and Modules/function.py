#deault argument

def greet(name = "user"):

    print(f"Hello {name}")
greet("ram")

#num le fun banayera square chahi return garne

def cal_sq(a):
    square = a ** 2
    return square
num = int(input("Enter the number:"))
a = cal_sq(num)
print(a)

# #WAF to print the length of a list(list is the parameter)
cities = ['kathmandu', 'bhaktapur', 'dharan']
print(len(cities))
name = ['srk','aryan','manisha','anisha']
def cities_len(list):
    print(len(list))

cities_len(cities)

def name_len(l1):
    print(len(l1))
name_len(name)

# #WAF to print the elements of a list in a single line.(list is the parameter)

name1 = ['manisa','anisa','manish','hari']

def print_listelements(list):
    for item in list:
        print(item,end=" ")
print_listelements(name1)

#WAF to find the factorial of n.(n is the parameter)

def fact(n):
    facto = 1
    for i in range(1, n+1):
        facto *=i
    return facto
num  = int(input("Enter Number:"))
print(fact(num))

#WAF to convert the usd into npr

def usd_conversion(usd_value):
    npr_value = usd_value * 135
    print(usd_value,"USD =",npr_value,"NPR")

usd = int(input("Enter the usd value"))
usd_conversion(usd)

#WAF that takes the number input and if that number is odd then it should return string "ODD" ELSE "EVEN"

def cal_odd_even(a):
    if a % 2 == 0:
        print("EVEN")
    else:
        print("ODD")
num = int(input("Enter the number:"))
cal_odd_even(num)


