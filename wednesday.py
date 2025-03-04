# code to interpret
num1 = int(input("input your first number"))
num2 = int(input("input your second number"))
#
#operator = input("choose the operator")
#print(num1, operator, num2)
if num1 >= num2:
    print("Error: First number {num1} should be less than second number {num2}")
#
if num1 % num2 ==0:
    print(f"{num1} is divisible by {num2}") # indented by 4 spaces
#
if num1 != 0: #(!= "isnot" doesnt work with integers)
    num2 += num1
    print(num2)
#
