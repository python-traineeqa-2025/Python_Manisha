#Function ko bhitra matra access hune lai local varaiable vancha

def fun(): #local variable
    x = 10
    print(x)

fun()

#global variable: accessible from both inside and outside from the function

x = 5
def global1():
    print(x)
global1()


y = 10
print(y)

def modify():
    global x
    x=90
    print(x)
modify()
print(x)

