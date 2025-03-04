# code
import keyword

#print(keyword.kwlist)
""""
# execute for loop
for i in range(1, 11):
    
    # print the value of i
    print(i)
    
    # check the value of i is less than 5
    # if i lessthan 5 then continue loop
    if i < 5:  
        continue
        
    # if i greater than 5 then break loop
    else:  
        break

# run for loop
for t in range(1, 5):
  # print one of t ==1
    if t == 1:
        print('One')
   # print two if t ==2
    elif t == 2:
        print('Two')
    else:
        print('else block execute')

# check var is odd or not
def edrine():
    var = 20
    if var % 2 == 0:
        print("The given number is even")
    else:
        print("The given number is odd")
# call the function
edrine()        

def fun():
    a = 5
    return a
#print(fun())

# use of a del keyword
num = ["a", "b", "c", "d", "e"]
# print list before using del keyword
print(num)
del num[2]
# print list after using del keyword
print(num)

def fun():
    name = "edrine"
    age = 12
    gender = "male"
    country = "Uganda"
    return name, age, gender, country
#print(fun())
name, age, gender, country = fun()
print(name)
print(age)
print(gender)
print(country)
"""""
# find the maximum of 3 numbers
def max_2(x, y):
    if x > y:
        return var1, var2
def max_3(x, y, z):
    return max_2(x, max_2(y, z))
print(max_3(10, -15, 17))