# principles of OOP
# 1. abstraction; sth that is not clear, helps in naming and identifying classes
#class names are always singular
# 2. encapsulation ability to hide or control some of the internal functionality of it's data
# details of encapsulation; private, public, protected, capsules can be in a tin 
# you mind about details with limitations
# 3. polymorphism ; (poly-many, morphism-forms) ability to take on different form
# classes/object takes on different forms
# 4. inheritance ability of a sub-class/derived-class/child-class to take one or more attributes of a superclass/base-class/ parent-class
# both the child-class and parent class are independent of each other

"""
class Animal():
    # properties/attributes/features/x-tics
    name = ""
    type = ""
    owner = ""
    weight = ""
# a function within a class is called a method
# the statements you write in a method are called behavior
    def sound(self): # sound is a method
        print("i bark")

dog = Animal()
dog.sound()
#dog.name =


# creating a class
class Dog:
# creating a constructor    
    def __init__(self, name, age):
        self.name = name
        self.age = age
# he __str__() function controls what should be returned when the class object is represented as a string.
    def __str__ (self):
        return f"{self.name}({self.age})"    
dog1 = Dog("blacky", 2) 
print(dog1)
#print(dog1.name)
#print(dog1.age)       
# defining a method(behavior) in a class
        #def bark(self):
           # print("bark!")

# object method
class Person:
    def __int__(self, name, age):
        self.name = name
        self.age = age

    def myfun(self):
        return f"Hello! my name is  + {self.name} and am {self.age} years"

person1 = Person("Eddy", 1)
print(person1.name)
print(person1.age)  
print(person1.myfun())          



class Phone:
    def __init__(self, model, color, price, battery_life):
        # instantiating the object
        self.battery_life = battery_life
        self.color = color
        self.price = price
        self.model = model

    def ring(self):
        ringtone = "ring ring ani ono" 
        call = print(ringtone)
        return call

my_phone = Phone('samsung', "gold", 500,00)       
print(my_phone.model)
my_phone.ring()


class Phone:
    def __init__(self, model, color, price, battery_life):
        # instantiating the object
        self.battery_life = battery_life
        self.color = color
        self.price = price
        self.model = model  # ✅ Fixed typo ('sel' → 'self')

    def ring(self):
        ringtone = "ring ring ani ono"
        print(ringtone)  # ✅ Just print, no need to assign to a variable
        return ringtone  # ✅ Return the ringtone instead of None

# ✅ Fixed incorrect number format
my_phone = Phone('samsung', "gold", 500.00, 24)  

# ✅ Now this works correctly
print(my_phone.model)  # Output: samsung

# ✅ Calling the ring method
my_phone.ring()  # Output: ring ring ani ono


class Car:
    def __init__(self, brand, color, price, model, fuel_type):
        self.brand = brand
        self.color = color
        self.price = price
        self.model = model
        self.fuel_type = fuel_type

    def drive(self):
        monster = "I love to drive powerful"   
        print(monster)
        return monster 
my_car = Car("Toyota", "grey", "1,000,000", "Tundra", "Petrol")
print(my_car.model)  
my_car.drive()  

class Dog:
    def __init__(self,name,type,owner, age, weight):
        self.name = name
        self.type = type
        self.owner = owner
        self.age = age
        self.weight = weight

    def bark(self):
        kara = "kara barks every night, to scarce away people"    
        print(kara)
        return kara
my_dog = Dog("Blacky", "local_breed", "Edmoore", "5-months", "7kgs")
print(f"Hello!, my dog is called {my_dog.name}, weighs  {my_dog.weight} a very sensitive puppy")    
my_dog.bark()

"""
class Person:
    def __init__(self, name, age, gender, contact, village, district):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact
        self.village = village
        self.district = district
# defining a method
    def reside(self):
        residence = "a place of affluents"    
        print(residence)
        return residence
person1 = Person("Edmoore", "27", "Male", "+201-20004000", "Zirombwe", "Wakiso")
print(f"My is {person1.name} aged {person1.age} residing in {person1.village} located in {person1.district} district")
print(f"{person1.contact} {person1.gender}")  
# calling a function 
person1.reside()
        


