
# creating a dictionary
details = {"name" : "Edrine",
           "age" : 29,
           "gender" : "male",
           "nationality" : "ugandan",
           "track" : "python"
           }
print(details.keys())
print(details.values())
print(details["track"])
print(len(details)) 
# determines the number of items in the dictioary
print(type(details))

details_1 = {"name": "madrine",
             "age": 20,
             "Track": "python",
             "Track": "java"
             }
print(details_1)
# duplicate values will overwrite the existing values hence the computer will consider the last option
x = details_1.items()
#print(x)
details_1["site"] = "Ground breaker" 
# adding items to the dictionary
details_1["Tutor"] = "Ozzy"
#print(details_1)
details_1.update({"site": "Ground breaker", "Tutor": "Ozzy"}) # 
#print(details_1)
details_1.pop("age") # removing an item from the dictionary
#print(details_1)
del details_1["Tutor"]
print(details_1)

# creating a list
var = ["windows", "linux", "macos"]
#print(var)
# indexing
print(var[0])
print(var[0:2])
print(var[-1])
var.append("Dell") # adding an item in the list
print(var)
var.remove("linux")
print(var)


squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)


# creating a tuple
cars = ("Vitara", "Tundra", "BMW", "cadillac", "Ford")
print(cars)

persona = ("John", 24, "Teacher")
name, age, job = persona
print(f"Name: {name}, Age: {age}, Job: {job}")


# creating a set
var1 = {"windows", "linux", "macos"}
var1.add("Ubuntu")
print(var1)
var1.remove("macos")
print(var1)


# set operations  
set1 = {1, 2, 3, 4}  
set2 = {3, 4, 5, 6}  

# Union of two sets  
union_set = set1 | set2    
print("Union:", union_set)


# Intersection of two sets  
intersection_set = set1 & set2  
print("Intersection:", intersection_set)  

# Difference of two sets  
difference_set = set1 - set2  
print("Difference:", difference_set)  

