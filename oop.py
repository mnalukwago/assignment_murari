# object-oriented programming
# class, object, properties(atributes, characteristics, features)
# methods, contructors
# principles of object-oriented programming (abstractio, encapsulation, inheritance, polymorphism)
# overloading, overriding

# oop is a programming concept/paradigm that advocates writing software based on real world objects/things

# objects are gotten/ obtained from class
# classes are identified in singular, number of individual objects make it plural
#  class is a blue print of an object
# an object is instance(example) of a class
# classes define the attributes/characteristics/features of the objects
# onion{name, price, color, type, size}
#president{name, country, age, gender, marital status, number of kids, }
# an object should fulfill all/some of the properties of the class
# use a dict to create an object
# example
students = ["madrine", "edrine", "emmie", "nowerine", "majorine"]
students1 = {"name": "madrine", "Gender": "Female", "school": "Refactory academy"}

# steps; use the keyword class and define that class
class Laptop():
    pass
class Food():
    name = ""
    taste = ""
    calories = 0
    price = 0
    value = ""

# creating objects out of the class food
matooke = Food()

matooke.name = "matooke"
matooke.taste = "sweet"
matooke.price = 3000
matooke.value = "carboydrate"

rice = Food()

rice.name= "rice"
rice.taste = "salty"
rice.calories = 0
rice.price = 5000
rice.value = "kilo"

print(rice.name)
print(matooke.price)
