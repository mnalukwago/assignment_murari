# Encapsulation
# Restricts direct access to some of the object's components, 
#which can prevent the accidental modification

# Achieved by prefixing names of attributes or methods with a single underscore (weakly private) or double underscore (strongly private) to suggest or enforce that they are meant to be private


"""
class Computer:
    def __init__(self, price, size, memory):
        self._price = price # (private attribute)
        self.size = size
        self.memory = memory

        def sell_computer(self):
            print(f"selling price: {self.__price}")


comp = Computer("ugshs.500,000", "medium", "100Hz")
print(comp._price)
comp.sell_computer()
"""

# Parent Class: Person
class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

# Child Class: Employee
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber)  # Using super() to call Person's __init__()
# super() function is used inside the __init__ method of employee to call the constructor of person and initialize the inherted attributes (name, and idnumer)        
# this ensures that the parent class functionality is reused without needing to rewrite the code in the child class      
        self.salary = salary
        self.post = post
emp = Employee("eddy", "201-100", "ug shs. 200/=", "dean")
emp.display()

# Types of Python Inheritance

"""
1. Single Inheritance: A child class inherits from one parent class.
2. Multiple Inheritance: A child class inherits from more than one parent class.
3. Multilevel Inheritance: A class is derived from a class which is also derived from another class.
4. Hierarchical Inheritance: Multiple classes inherit from a single parent class.
5. Hybrid Inheritance: A combination of more than one type of inheritance.


# 1. Single Inheritance
class Person:                                   # 1st parent
    def __init__(self, name):
        self.name = name

# Employee inherits from Person
class Employee(Person): 
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

# 2. Multiple Inheritance
class Job:                                      # 2nd parent
    def __init__(self, salary):
        self.salary = salary

# Inherits from both Employee and Job
class EmployeePersonJob(Employee, Job):  
    def __init__(self, name, salary):
        Employee.__init__(self, name, salary)  # Initialize Employee
        Job.__init__(self, salary)            # Initialize Job

# 3. Multilevel Inheritance
class Manager(EmployeePersonJob):  # Inherits from EmployeePersonJob
    def __init__(self, name, salary, department):
        EmployeePersonJob.__init__(self, name, salary)  # Explicitly initialize EmployeePersonJob
        self.department = department

# 4. Hierarchical Inheritance
class AssistantManager(EmployeePersonJob):  # Inherits from EmployeePersonJob
    def __init__(self, name, salary, team_size):
        EmployeePersonJob.__init__(self, name, salary)  # Explicitly initialize EmployeePersonJob
        self.team_size = team_size

# 5. Hybrid Inheritance (Multiple + Multilevel)
class SeniorManager(Manager, AssistantManager):  # Inherits from both Manager and AssistantManager
    def __init__(self, name, salary, department, team_size):
        Manager.__init__(self, name, salary, department)        # Initialize Manager
        AssistantManager.__init__(self, name, salary, team_size)  # Initialize AssistantManager

# Creating objects to show inheritance

# Single Inheritance
emp = Employee("John", 40000)
print(emp.name, emp.salary)

# Multiple Inheritance
emp2 = EmployeePersonJob("Alice", 50000)
print(emp2.name, emp2.salary)

# Multilevel Inheritance
mgr = Manager("Bob", 60000, "HR")
print(mgr.name, mgr.salary, mgr.department)

# Hierarchical Inheritance
asst_mgr = AssistantManager("Charlie", 45000, 10)
print(asst_mgr.name, asst_mgr.salary, asst_mgr.team_size)

# Hybrid Inheritance
sen_mgr = SeniorManager("David", 70000, "Finance", 20)
print(sen_mgr.name, sen_mgr.salary, sen_mgr.department, sen_mgr.team_size)

"""
# Multiple Inheritance
# Python program to demonstrate
# multiple inheritance

# Base class 1
class Mother:
    def __init__(self, name):
        self.mothername = name  # Fixes attribute assignment

    def mother(self):
        print("Mother:", self.mothername)

# Base class 2
class Father:
    def __init__(self, name):
        self.fathername = name  # Fixes attribute assignment

    def father(self):
        print("Father:", self.fathername)

# Derived class (inherits from both Mother and Father)
class Son(Mother, Father):
    def __init__(self, mother_name, father_name):
        Mother.__init__(self, mother_name)  # Initialize Mother
        Father.__init__(self, father_name)  # Initialize Father

    def parents(self):
        print("Father:", self.fathername)
        print("Mother:", self.mothername)

# Object instantiation with required arguments
s1 = Son("Tebi", "Taaka")  # Provide names when creating Son object
s1.parents()  # Correctly prints parent names


class Protein:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def builds(self):
        print(f"{self.name} is a body building food")

class Carbohydrate:
    def __init__(self, name, price):
        self.name = name
        self.price = price

        print("carbohydrate provide us with energy: ", self.name)

class Chicken(Protein, Carbohydrate):
    def __init__(self, name, price):
        super().__init__(name, price)

    def both(self):
        print("Protein: ", self.name)
        print("Carbohydrate: ", self.price)

# instantiaing the object
chick = Chicken("buddie", "ugshs.9000/=")  
chick.both()          


# multilevel inheritance
# Python program to demonstrate
# multilevel inheritance

# Base class
class Grandfather:
     def __init__(self, grandfathername):
          self.grandfathername = grandfathername

# Intermediate class
class Father(Grandfather):
     def __init__(self, fathername, grandfathername):
        self.fathername = fathername

# invoking constructor of Grandfather class
        Grandfather.__init__(self, grandfathername)

# Derived class
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname

# invoking constructor of Father class
        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)


# Driver code
son = Son('Mugisha', 'Kamugisha', 'Ainomugisha')
print(son.grandfathername)
son.print_name()
                    
# Python program to demonstrate
# hybrid inheritance


class School:
	def func1(self):
		print("This function is in school.")


class Student1(School):
	def func2(self):
		print("This function is in student 1. ")


class Student2(School):
	def func3(self):
		print("This function is in student 2.")


class Student3(Student1, School):
	def func4(self):
		print("This function is in student 3.")


# Driver's code
object = Student3()
object.func1()
object.func2()


# Abstract Principle 
from abc import ABC, abstractmethod

# Define an abstract class
class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass  # This is an abstract method, no implementation here.

# Concrete subclass of Animal
class Dog(Animal):
    
    def sound(self):
        return "Bark"  # Providing the implementation of the abstract method

# Create an instance of Dog
dog = Dog()
print(dog.sound())  # Output: Bark
