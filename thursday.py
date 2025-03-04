# if's used in decision making
"""
age = 20
if age < 18:
    print("you're minor")
elif age < 21:
    print("you're young adult")
else:
    print("you're an adult")
# 
num = 15
if num % 2 == 0:
    print("the number is even")
elif num % 3 == 0:
    print("the number is divisible by 3")
else:
    print("the number is odd and not divisible by 3")
#
marks = int(input("enter your marks ")) # using the input function 
if marks >= 90:
    print("A")
#elif grade >= 80:
    #print("B")
elif 80 <=  marks < 89:
    print("G")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")
# nested if's
a = 45
if a > 10:
    print("greater than 10")
    if a > 30:
        print("also above 30")
    else:   
        print("less than 30") 
else:
    print("none of the above")
"""

a = 33
b = 200
if b > a:
    print("b is greater a")

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
a = 2
b = 330
print("A") if a > b else print("B")

# logical operator "AND"
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions atre True")

# logical operator "OR"
a = 200
b = 33
c = 500
if a > b or c > a:
    print("Atleast one of the conditions is True")

# logical operator "NOT"
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")

# nested if
x = 41
if x > 10:
    print("Above ten")
    if x > 20:
        print("and also 20!")
    else:
        print("but not above 20.")   

# the pass statement
a = 33
b = 200
if b > a:
    pass 

a = 2
b = 5
print("YES") if a == b else print("NO")