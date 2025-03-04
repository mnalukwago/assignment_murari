# steps taken to created a function
def add():
    a,b = 20, 40
    print(a + b)
#add()
#
def add1():
    a = int(input("please enter your first number:\n"))
    b = int(input("please enter your second number:\n"))
    print(a + b)
#add1()

def add2():
    a = int(input("please enter your first number:\n"))
    b = int(input("please enter your second number:\n"))
    if a % b == 0:
        print(f"{a} doesnt give remainder")
    else:
        print(f"{a} does give remainder")
    
#add2()
# creating a function
def my_function():
    print("hello from a function")

# calling a function
# To call a function, use the function name followed by parenthesis:
#my_function()


#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the value that is sent to the function when it is called.

def my_function(fname, lname):
    print(fname + ""  +  lname)

#my_function("Edrine", "Mugisha")
#my_function("Edrine")

def my_function(*kids):
  print("The youngest child is " + kids[2])

#my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

#my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

#my_function(fruits)

cars = ["Toyata_Tundra", "Ipsum", "Ford", "Toyota_high lander"]
def car():
   for item in cars:
      print(cars)

car()
   