# stastic functions have hard coded values (permanent values)
def add():
    var1 = 10
    var2 = 20
    return var1 + var2 # return allows the value/variable of a function to be exposed out of the function
#print(add())
my_num = add()
#print(my_num)


def sum():
    num1 = 10
    num2 = 30
    return num1 + num2
#print(sum())

def both():
    return sum() + add()
#print(both())
# capture values from the screen
def add1():
     var2 = (int(input("please enter the number.\n"))) # number1 is a global variable(it's outside the function)
     var3 =  (int(input("please enter the number.\n"))) # capture is a local variable (b'se it's inside a function)
     return var2 + var3 

def sub1():
     var2 = (int(input("please enter the number.\n"))) # number1 is a global variable(it's outside the function)
     var3 =  (int(input("please enter the number.\n"))) # capture is a local variable (b'se it's inside a function)
     return var2 - var3 
def both():
    return add1() + sub1()
print(both())
 