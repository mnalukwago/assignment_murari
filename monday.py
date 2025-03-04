# mapping (data type)- dictionary(key:value)
student_detail = {"name": "madrine", 
                  "track": "python", 
                  "gender": "Female",
                  "Age": 25}
# dictionary stores data value in key: value pairs
# A dictionary is a collection which is ordered, changeable.
# Dictionaries are written with curly brackets, and have keys and values:
# Dictionaries cannot have two items with the same key
print(student_detail["name"])
print(student_detail.keys())
# brings a list of keys[name, track, gender, age]
print(student_detail.values())
cars = {"brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "chasis_No": "AA520000"}
x = cars.items()
print(cars["model"])
print(cars["brand"])
print(len(cars))
print(type(cars))
print(x)
# check if keys exist
if "model" in cars:
        print("Yes")

# updating the dictionary
caars = {"brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "chasis_No": "AA520000"}
cars.update({"year": 1965})
print(cars)

# adding items to dictionary
cars = {"brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "chasis_No": "AA52000"}
cars["color"] = "Blue"
cars.update({"color": "Red"})
print(cars)

# Removing items from the dictionary
cars = {"brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "chasis_No": "AA52000"}
cars.pop("chasis_No")
print(cars)
cars.popitem() # removes the last inserted item in the dictionary
print(cars)
del cars["model"] # removes the item with the specified key name
print(cars)
cars = {"brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "chasis_No": "AA52000"}
cars.clear() # empties the dictionary
print(cars)
 
 # Copying a dictionary
cars = {"brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "chasis_No": "AA52000"}

my_cars = cars.copy()
print(my_cars)

carrs = {"brand": "Ford",
        "model": "Mustang",
        "year": 1964,
        "chasis_No": "AA52000"}
my_carrs = dict(carrs)
print(my_carrs)

# Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
     "age" : 5,
    "year" : 2004},
  "child2" : {
    "name" : "Tobias",
    "age"  :7,
    "year" : 2007},
  "child3" : {
    "name" : "Linus",
    "age"  : 9,
    "year" : 2011}
}
#print(myfamily["child2"]["name"])
for x, obj in myfamily.items():
  print(x)
# set (data type)- store unique values.(no duplicates in the set)
# we use curly brackets for storing our values 
student_id = {101, 105, 103, 104, 102, 101,}
#print(student_id)
# lists, sets and dictionaries are muteable(you can add or remove items fromthem).

