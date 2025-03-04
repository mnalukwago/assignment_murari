#For loop
fruits = ["apple", "mangoes", "jackfruit", "banana", "berry"]
#for item in fruits:
    #print(item)
#
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
def evens():
    for item in numbers:
        if item % 2 == 0:
            print(item)
# a named block of code is called a function
# a function is a named block of code that performs a specific task
def fruit():
    for item in fruits:
        print(item)
fruit() # fruit is a function
#print()
#type()
#evens()

digits = [0, 1, 5]
for i in digits:
    print(i)
else:
    print("No items left")    

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

animals = ("cat", "dog", "cow", "pig", "goat")
for item in animals:
   print(item)
   if item == "dog":
      print(item)
      break
      