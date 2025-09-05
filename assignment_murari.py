class Person:
    def __init__(self, name, occupation, organization):
        self.name = name
        self.occupation = occupation
        self.organization = organization
    def describe(self):
        print(f"My name is {self.name}, work as {self.occupation}, at  {self.organization}")

# create an object
person = Person("Malik", "Analyst", "Malik_Foundation")   
person.describe()     


# create other classes