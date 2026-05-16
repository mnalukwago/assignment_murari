"""
parent class
class Animal:
    def __init__(self, name, age, breed, size):  # parameters
        # identifying properties of the class animal
        self.name = name
        self.age = age
        self.breed = breed
        self.size = size

    # creating a method
    # a method will always have a word self
    def details(self):
        print(f"animalname: {self.name} the animal breed is: {self.breed}")    

# inheritance; a dog is sharing all the properties of class animal
# child class
class Dog(Animal):
    def sound(self):
        print("dog woofs")

class Bulldog(Dog):
    def greet(self):
        print("Bulldog wags")
bulldog = Bulldog("max", "5_months", "Exotic", "medium")
dog = Dog("Blacky", "7_months", "local", "small")
dog.details() 
dog.sound() 
bulldog.greet()

# Base class
class Animal:
    def __init__(self, name, age, species, color, size, weight, habitat):
        self.name = name
        self.age = age
        self.species = species
        self.color = color
        self.size = size
        self.weight = weight
        self.habitat = habitat

    def details(self):
        print(f"{self.name} is a {self.age}-year-old {self.species} with {self.color} color.")

# Class inheriting from Animal
class Mammal(Animal):
    def __init__(self, name, age, species, color, size, weight, habitat, has_fur):
        super().__init__(name, age, species, color, size, weight, habitat)
        self.has_fur = has_fur

    def warm_blooded(self):
        print(f"{self.name} is warm-blooded.")

# Class inheriting from Mammal
class Dog(Mammal):
    def __init__(self, name, age, species, color, size, weight, habitat, has_fur, breed):
        super().__init__(name, age, species, color, size, weight, habitat, has_fur)
        self.breed = breed

    def sound(self):
        print(f"{self.name} barks loudly!")

# Class inheriting from Dog
class Bulldog(Dog):
    def __init__(self, name, age, species, color, size, weight, habitat, has_fur, breed, strength):
        super().__init__(name, age, species, color, size, weight, habitat, has_fur, breed)
        self.strength = strength

    def greet(self):
        print(f"{self.name} wags its tail excitedly!")

# 5th Class with at least 5 methods
class PetBulldog(Bulldog):
    def __init__(self, name, age, species, color, size, weight, habitat, has_fur, breed, strength, owner_name):
        super().__init__(name, age, species, color, size, weight, habitat, has_fur, breed, strength)
        self.owner_name = owner_name

    def fetch(self):
        print(f"{self.name} runs to fetch the ball!")

    def sit(self):
        print(f"{self.name} sits on command.")

    def roll_over(self):
        print(f"{self.name} rolls over playfully.")

    def guard(self):
        print(f"{self.name} stands guard to protect {self.owner_name}.")

    def eat(self):
        print(f"{self.name} is eating its favorite meal.")

# Creating an instance of PetBulldog
pet_bulldog = PetBulldog("Max", 3, "Bulldog", "Brown", "Medium", "50 lbs", "Home", True, "English Bulldog", "Strong", "John")

# Calling methods
pet_bulldog.details()
pet_bulldog.warm_blooded()
pet_bulldog.sound()
pet_bulldog.greet()

# Calling the 5 methods from PetBulldog
pet_bulldog.fetch()
pet_bulldog.sit()
pet_bulldog.roll_over()
pet_bulldog.guard()
pet_bulldog.eat()

""""
# Parent Class
class Food:
    def __init__(self, name, taste, color, is_healthy, origin, price, calories):
        self.name = name
        self.taste = taste
        self.color = color
        self.is_healthy = is_healthy  # Boolean: True/False
        self.origin = origin  # Plant-based or Animal-based
        self.price = price  # Price per unit
        self.calories = calories  # Energy value

    def describe(self):
        return f"{self.name} is {self.color}, tastes {self.taste}, and contains {self.calories} kcal. Origin: {self.origin}. Healthy: {self.is_healthy}. Price: ${self.price}"

# Child Classes
class Protein(Food):
    def __init__(self, name, taste, color, is_healthy, origin, price, calories, source):
        super().__init__(name, taste, color, is_healthy, origin, price, calories)
        self.source = source  # Animal-based or Plant-based

    def describe(self):
        return super().describe() + f" This is a {self.source} protein."

class Carbohydrate(Food):
    def __init__(self, name, taste, color, is_healthy, origin, price, calories, energy_level):
        super().__init__(name, taste, color, is_healthy, origin, price, calories)
        self.energy_level = energy_level  # High or Low

    def describe(self):
        return super().describe() + f" It has a {self.energy_level} energy level."

class Fat(Food):
    def __init__(self, name, taste, color, is_healthy, origin, price, calories, fat_type):
        super().__init__(name, taste, color, is_healthy, origin, price, calories)
        self.fat_type = fat_type  # Saturated or Unsaturated

    def describe(self):
        return super().describe() + f" This is a {self.fat_type} fat."

class Fruit(Food):
    def __init__(self, name, taste, color, is_healthy, origin, price, calories, season):
        super().__init__(name, taste, color, is_healthy, origin, price, calories)
        self.season = season  # Season when it's available

    def describe(self):
        return super().describe() + f" It is mostly available in {self.season}."

# 5th Class with At Least 5 Methods
class Vegetable(Food):
    def __init__(self, name, taste, color, is_healthy, origin, price, calories, vitamins):
        super().__init__(name, taste, color, is_healthy, origin, price, calories)
        self.vitamins = vitamins  # List of vitamins in the vegetable

    def describe(self):
        return super().describe() + f" It contains vitamins: {', '.join(self.vitamins)}."

    def is_expensive(self):
        return "Expensive" if self.price > 5 else "Affordable"

    def is_low_calorie(self):
        return self.calories < 50  # Returns True if it has low calories

    def is_good_for_skin(self):
        return "Yes" if "Vitamin A" in self.vitamins or "Vitamin E" in self.vitamins else "No"

    def can_be_eaten_raw(self):
        raw_veggies = ["Carrot", "Lettuce", "Cucumber", "Tomato"]
        return "Yes" if self.name in raw_veggies else "No"

# Creating Objects
chicken = Protein("Chicken", "Savory", "White", True, "Animal-based", 4.5, 165, "Animal-based")
rice = Carbohydrate("Rice", "Mild", "White", True, "Plant-based", 1.2, 130, "High")
butter = Fat("Butter", "Creamy", "Yellow", False, "Animal-based", 3.0, 717, "Saturated")
apple = Fruit("Apple", "Sweet", "Red", True, "Plant-based", 1.5, 95, "Autumn")
carrot = Vegetable("Carrot", "Crunchy", "Orange", True, "Plant-based", 0.8, 25, ["Vitamin A", "Vitamin K"])

# Displaying Descriptions
print(chicken.describe())
print(rice.describe())
print(butter.describe())
print(apple.describe())
print(carrot.describe())

# Testing Vegetable Methods
print(f"Is {carrot.name} expensive? {carrot.is_expensive()}")
print(f"Is {carrot.name} low in calories? {'Yes' if carrot.is_low_calorie() else 'No'}")
print(f"Is {carrot.name} good for skin? {carrot.is_good_for_skin()}")
print(f"Can {carrot.name} be eaten raw? {carrot.can_be_eaten_raw()}")
