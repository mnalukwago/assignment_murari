# you declared a variable called some_string and assigned a string to it 
some_string = 'Python is fun' 

# declaring different variables and assigning them different values in a single line
a, b, c = 5, 3.2, 'Hello'


print(a)  # the ouput is 5
print(b)  # the output is 3.2
print(c)  # the output is Hello

#declaring a variable called num1 and assigning an integer value to it 
num1 = 5

#printing out the type of num1; <class 'int'>
print(num1, 'is of type', type(num1))


#declaring a variable called num1 and assigning an integer value to it
num2 = 2.0
#printing out the type of num2; <class 'float'>
print(num2, 'is of type', type(num2))


#declaring a variable called num1 and assigning an integer value to it
num3 = 1+2j
#printing out the type of num3 <class 'complex'>
print(num3, 'is of type', type(num3))


# creating a list and call it languages. denoted by square brackets
languages = ["Swift", "Java", "Python"]

# accessing items from the list at position 0
print(languages[0])   # the output is swift

# accessing items from the list at position 2
print(languages[2])   # the output is pyton

# creating a tuple called product, denoted by paranthesis/open brackets  
product = ('Microsoft', 'Xbox', 499.99)

# accessing an item from the tuple 
print(product[0])   # Microsoft is the output using index 0

# accessig an item from the tuple 
print(product[1])   # Xbox is the output using index 1


#creatig a dictionary called capital_city, denoted by curly brackets and key-value pairs
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}

#printing items in the dictionary
print(capital_city)


# creating a set called student_id, denoted by curly brackets 
student_id = {112, 114, 116, 118, 115}

# printing out items in the set
print(student_id)

# printing out the type of student_id, <class 'set' >
print(type(student_id))

# creating a list called fruits
fruits = ["apple", "mango", "orange"] 

#printing out items in the list fruits
print(fruits)

# creating a tuple called numbers
numbers = (1, 2, 3) 

#printing out items in the numbers
print(numbers)

# creating a dictionary called alphabets
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} 

#printing out items in alphabets
print(alphabets)

# creating a set of vowels
vowels = {'a', 'e', 'i' , 'o', 'u'} 
print(vowels) 


# creating a st of student_ids'
student_id = {112, 114, 116, 118, 115}

# printing out items in student_id
print(student_id)

# display type of student_id <class 'set'>
print(type(student_id))


# creating a tuple called product
product = ('Microsoft', 'Xbox', 499.99)

#accessing an item from product using index 0
print(product[0])   # the output is Microsoft

# accessing an item from product using index 1
print(product[1])   # Xbox is the output 




# (arithmetic operators) declaring two variables (a,b) and assign them different values(7, 2)
a = 7
b = 2

# printing the addition operator; output = 9
print ('Sum: ', a + b)  

# printing the subtraction operator; output = 5
print ('Subtraction: ', a - b)   

# printing the multiplication operator; output = 14
print ('Multiplication: ', a * b)  

# printing the division operator; output = 3.5
print ('Division: ', a / b) 

# printing the floor division operator; output = 3
print ('Floor Division: ', a // b)

# printing the modulo operator; output = 1
print ('Modulo: ', a % b)  

#printing the power operator; output = 49 
print ('Power: ', a ** b)   


# declaring a variable (a) and assign it a value
a = 10

# declaring a variable (b) and assign it a value
b = 5 

# get variable b add it to variable a
a += b      #a = a + b(assignment operator)
print(a)
# Output: 15


# checks if a is equal to b; prints False
print('a == b =', a == b)

#checks if a is not equal to b; prints True
print('a != b =', a != b)

# checks if a is greater than b; prints True
print('a > b =', a > b)

# prints True if a is greater than b; else prints False if a is less than b
print('a < b =', a < b)

# checks if a is greater than or equal to b; prints True 
print('a >= b =', a >= b)

# checks if a is less than or equal to b; prints True
print('a <= b =', a <= b)

#checks whether both the conditions are true but b greater than or equal to 6 is false; prints False
print((a > 2) and (b >= 6)) 

# boolean operators
print(True and True)     # True, since both the values are true
print(True and False)    # False , since one of the values is false

# checks if atleast one value is true; prints True
print(True or False)     # the ouput is True

# prints false if the value is not true
print(not True)          # the output is false

#Identity operator
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# 'is not' checks if they are not the same object. Since they are the same,
print(x1 is not y1)  # the output is false, because x1 and y1 have the same memory location


#strings are  immutable and have the same memory location
print(x2 is y2)  # the output is True


# lists are mutable and have separate memory location
print(x3 is y3)  # the output is false


#assigning a string to a variable
message = 'Hello world'

#creating a dictionary
dict1 = {1:'a', 2:'b'}

# checks if H is present in the string
print('H' in message)  # The output is True

# checks if hello is not a string
print('hello' not in message)  # the output is false

# in checks keys in a dictionary
print(1 in dict1)  # the output is True

# a is a value not a key
print('a' in dict1)  # the output is False

















