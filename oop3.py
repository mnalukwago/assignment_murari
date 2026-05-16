"""
class Animal:
    # a constuctor is defined by two underscores
    # it's used to initialize or give a value of a an object of a class
    # self (is the first parameter) is used to identify the properties of the class
    def __init__(self,name,type,owner, age, weight):
        # init is a dynamic method
        self.animalname = name # animalname is  property but name is value
        self.animaltype = type
        self.animalowner = owner
        self.animalweight = weight
        self.animalage = age

dog = Animal("dog", "blacky", "local", "Eddy", "15kg", "1year")
dog1 = Animal("dog1", "kara", "hybrid", "Emmie", "8kg", "10months")

"""
class Fruit:
    def __init__(madrine, name, color, size, taste, price): # these are parameters (madrine is the identifier property)
        madrine.name = name
        madrine.color = color
        madrine.size = size
        madrine.taste = taste
        madrine.price = price
# self is not a keyword but has been adopted in python
# the memory of a class is expandable(limitless)
        # creating an object

# single and multiple inheritance        
fruit1 = Fruit("Mango", "green", "medium", "yummy", "2000") # these are arguments/properties of the parameter in class Fruit
fruit2 = Fruit("Apple", "red", "small", "sweet", "1500")        
    
class Family:
    def __init__(self, first_name, last_name, age, gender, date_of_birth, contact, village):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.contact = contact
        self.village = village

    def describe(self):
        print(f"Family is blood")

class Grandfather(Family):  
    def builds(self):
        print(f"our grandfathers are the custodian our bloodline in my {self.village} ")          
        

class Father(Grandfather):
    def protects(self):
        print(f"{self.last_name} is my father")

class Son(Father):
    def grooms(self):
        print(f"my go in this world with an open mind, {self.first_name} every thing will sense when you move out of your comfort zones")     

          
class Grandson(Son):
    def obeys(self):
        print(f"my son the sky is the limit")

    def respects(self):
        print(f" that is my contact {self.contact}")  

    def bahaves(self):
        print(f"our behavior says alot about us")     

    def cries(self):
        print(f"{self.first_name} it's okay for you to cry, since it's a pain killer")

    def eats(self):
        print(f"food is like smoothie")   

grandsonie = Grandson("sonia", "Kaata", "19 years", "Male", "10th/07/2006", "+2005-700", "kanos")     

# calling the methods
grandsonie.describe()
grandsonie.builds()
grandsonie.protects()
grandsonie.grooms()

# calling the methods in grandson
grandsonie.obeys()
grandsonie.respects()
grandsonie.bahaves()
grandsonie.cries()
grandsonie.eats()