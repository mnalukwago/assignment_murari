"""
# formated string
first = "madrine"
last = "nalukwago"
#full = first + " " + last # concanate
full = f"{len(first)} {last}"
print(full)

course = "python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("pro")) # returns the index of the string
print(course.replace("p", "j"))
print("pro" in course)# checks if the string is part of the main string and prints true or false
print("swift" not in course)

fruit = "apple"
print(fruit[1:-1])
print(bool("false"))

# Loops
for number in range(3):
    #print("Attempt", number)
    print("Attempt", number + 1)

successful = False
for number in range (3):
    print("Attempt")
    if successful:
        print("successful")
        break
    else:
        print("Attempted 3 times and failed")


# nested loops
for x in range (5):
    for y in range(2):
        print(f"{x}, {y}")

def hello():
    name = str(input("Enter your name.\n"))
    if name:
        print ("Hello " + str(name))
    else:
     print("Hello World") 
    return 
  
hello()

def double(x):
  return x*2
"""
def student_details():
    details = int(input("number of entries"))
    student = {input("Enter key: "): input("Enter value") for _ in range(details)}   
    print(student)

student_details()