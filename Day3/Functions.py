num1 = 10
num2 = 5

#defining functions
def addition ():
    add = num1+num2
    print('Addition value =',add)

def subtract ():
    sub = num1-num2
    print('Subtract value =',sub)

def multiply ():
    mul = num1*num2
    print('multiply value =',mul)

#Invoking functions
addition()
subtract()
multiply()


######################## Making functions modular

def addition (num1,num2):
    add = num1+num2
    return add

def subtract (num1,num2):
    sub = num1-num2
    return sub

def multiply (num1,num2):
    mul = num1*num2
    return mul


print('addtion value=', addition(6,1))
print(subtract(6,1))
print(multiply(6,1))

