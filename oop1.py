"""
class Animal():
    name = ""
    origin = ""
    lifespan = ""
    family = ""
    size = ""
    color = ""
    diet = ""
    common_use = ""
    Trainability = ""

# the dot operator is used to access the properties, x-tics, features of the object
dog = Animal()
dog.name = "German shepherd"
dog.origin = "Germany"
dog.family = "canidae"
dog.lifespan = "9 years"
dog.size = "large"
dog.color = "black"
dog.diet = "carnivorous"
dog.common_use = "security"
dog.Trainability = "highly trainable"
#print(dog.name)
#print(dog.common_use)
print(f"dog: {dog.name}, {dog.family}, {dog.size}, {dog.origin}")
"""
class student():
    name = ""
    age = 0
    test1 = 0
    test2 = 0
# method1
    def average(self, test1, test2):
        aveg = (test1 + test2)/2
        results = print(aveg)
        return results
    

    def exam(self, test1, test2):
        exam = (0.3 * test1 ) + (0.7 * test2)
        result1 = print(exam)
        return result1
    
my_student = student()
my_student.name = "Madrine"
my_student.age = 20
my_student.test1 = 25
my_student.test2 = 65
my_student.average
print(my_student.name+"\n" +str(my_student.age)+"\n")
print(my_student.average(my_student.test1, my_student.test2))

"""
kara = student()
kara.name = "Edrine"
kara.age = 19
kara.test1 = 21
kara.test2 = 50
kara.average

moonia = student()
moonia.name = "nowerine"
moonia.age = 20
moonia.test1 = 21
moonia.test2 = 55
moonia.average

# one of the ways to capture details from the command line
user_input = student()
user_input.name = input("enter your name.\n")
user_input.age = int(input("age "))
user_input.test1 = int(input("test1 "))
user_input.test2 = int(input("test2 edrine"))

"""
class Lake():
    name = ""
    type = ""
    size = ""
    location = ""
    continent = ""
    country = ""
    
