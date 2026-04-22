import time
# class is like a blueprint for creating objects.
# It defines a set of attributes and methods that the created objects will have.
# An object is an instance of the class.
# It is a special variable that holds the data and functions defined in the class.
from importlib.machinery import NamespaceLoader
from types import MethodDescriptorType

from click import argument


class Student:
    def __init__(self):                      #self is a reference to the current instance of the class, and is used to access variables that belong to the class.
        print("Adding new student to the database....")
        self.name = "Omprakash Chaudhary"
        self.age = 24
s1 = Student()      # creating an object or (instance) of the class Student
# print(s1.name)      # accessing the name attribute of the object s1
# print(s1.age)       # accessing the age attribute of the object s1  
s2 = Student()
# print(s2.name)
# print(s2.age)


class Car:
    brand = "BMW"
    color = "Black"
car1 = Car()
print(car1.brand)
print(car1.color)


# constructor is a special method that is automatically called when an object of a class is created. It is used to initialize the attributes of the class.
#__init__ is a constructor in python. It is called when an object is created from the class and it allows the class to initialize the attributes of the class. 
class Printer():
    Equipments_needed = ["Paper","Ink","Power"]  # class attribute or class variable
    brand = "Not known right now"
    def __init__(self,brand,model):   # ? __init__ is the constructor here. self is the object(instance) which is in this case p1.
        print("Loading printer software...") # ? whenever we create an instance of the Printer class, this message will be printed.
        self.brand = brand #  self.brand is an object attribute(or instance variable) that is being initialized with the value of the 2nd parameter in the constructor, which is brand.
        self.model = model #  self.model is an object attribute(or instance variable) that is being initialized with the value of the 3rd parameter in the constructor, which is model.
p1 = Printer("Canon","LBP3120")  #  when we create an instance it is not required to give brand and model as arguments because they are being passed to the constructor which will initialize the attributes of the class with the values passed as arguments.
p2 = Printer("HP","LaserJet Pro MFP M227fdw") #  when we create an instance it is compulsary to give brand and model as arguments because they are being passed to the constructor which will initialize the attributes of the class with the values passed as arguments.
print(p2.model)  # LaserJet Pro MFP M227fdw
print(p1.brand)  # Canon

print(p1.Equipments_needed)  # ['Paper', 'Ink', 'Power']
print(Printer.Equipments_needed)  # ['Paper', 'Ink', 'Power']  ! we can access class attributes using the class name as well as the object name.
print(p1.brand)  # Canon



# ! Now we are going to learn about functions inside a class which are called methods. Methods are functions that belong to an object. They are used to perform operations on the data that is contained in the object. Methods are defined inside a class and can be called on an object of that class.

class Students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    print("Adding new student to the database..")
    
    def welcome(self):
        print("Welcome to the class!  ",self.name)

    def get_marks(self):
        print("Marks of", self.name, "are:", self.marks)
s5 = Students("Omprakash Chaudhary", 34)
s5.welcome()
s5.get_marks()


# Q1. Create student class that takes name adn marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class Studenti():
    def __init__(self,name,sub1,sub2,sub3):  # passing each subject one by one
        self.name = name 
        self.sub1 = sub1 
        self.sub2 = sub2 
        self.sub3 = sub3
    def average(self):
        avg = (self.sub1 + self.sub2 + self.sub3)/3
        print(f"Hey! {self.name} your average score is {avg}")

s6 = Studenti("Baba Tillu",70,69,68)
s6.average()

class Studentl:
    def __init__(self,name,marks): # passing marks as a list
        self.name = name
        self.marks = marks
    def averagel(self):
        total_marks = 0
        for marks in self.marks:
            total_marks += marks
        avg = total_marks/len(self.marks)
        print(f"Hey! {self.name} your average score is {avg}")

s7 = Studentl("Dogesh Bhai", [70,69,68,67,66,65])
s7.averagel()
s7.name = "Baba Tillu"
print(s7.name)   # Baba Tillu



# ! Static method : Methods that don't use the self parameter(work at class level only won't work with object attributes). They are defined using the @staticmethod decorator.

class Studentstatic:
    def __init__(self):
        print("Adding a new student to the database...")
    
    @staticmethod       # Without this the we will get an error because the method hello() is not taking self as a parameter.
    def hello():
        print("Hey!, How are you all?")
    @staticmethod
    def college():   # we can use this same function above the __init__ function, if don't want to use @staticmethod 
        print("welcome to shoolini university")
    
s8 = Studentstatic()
s8.hello()      # all of these methods are called static methods. class level methods == static methods
s8.college()

#-------------------------------------------------------------------------------------------------------
# ! 4 pillars of oops(python)

# ! Abstraction: Abstraction is the process of hiding the implementation details and showing only the functionality to the user.
# ? In python, we can achieve abstraction by using abstract classes and abstract methods. An abstract class is a class that cannot be instantiated and is meant to be subclassed.
# ? An abstract method is a method that is declared but contains no implementation. It is meant to be overridden in the subclass.

# ! Encapsulation: Hiding the internal state and requiring all interaction to happen through an object's methods. This protects data from accidental corruption.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("The car has started...")

car1 = Car()
car1.start()
#_----------------------------------------------------------------------------------------------
# ? del (delete) keyword it is used to delete object attributes and object itself
class Student():
    def __init__(self,name):
        self.name = name
        print(name)
    
s11 = Student("Dogesh bhai")

s11.name

del s11.name  # deletes the attribute name
s11.name
#------------------------------------------------------------------------------------------------
# Private attributes and Methods  
class Account():
    def __init__(self,ac_num,ac_pass):
        self.ac_num = ac_num
        # self.ac_pass = ac_pass this is considered and is a bad practice
        self.__ac_pass = ac_pass    # Now we can't access this info outside of the class i.e private
        # ? Why do we even have this thing with us ?? 
    def reset_pass(self):
        print(self.__ac_pass)  # it will give the results no problem
ac11 = Account(1234,'abe@123')        
# print(ac11.__ac_pass)  # It will give an error of 'Account' object has no0 attribute '__ac_pass'
ac11.reset_pass()  

# same goes for method . just use __ before the method and it will become like private not exactly private
class Person():
    __name = "anonymous"       #same old attribute private
    def __hello(self):              # method private
        print("hello person ! How are you?")
        # as beginner why is this thing exist in the first place 
    def welcome(self):
        self.__hello()

p11 = Person()
# p11.__hello()    # no method of this name 
p11.welcome()

#  ! Inheritance = when one class(child/derived) derives the property and methods of another class(parent/base)
#  single inheritance   # multi-level inheritance    # multiple inheritance
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started.")
    @staticmethod
    def stop():
        print("car stopped.")
class bmw(Car):                                  # ? this is single inheritance
    def __init__(self,brand):
        self.brand = brand
class two_point_O(bmw):                         # ? this is multilevel inheritance
    def __init__(self,type):
        self.type = type
c11 = bmw(2.0)
c12 = bmw(2.1)
c11.start()
c11.stop()
print(c11.color)
c13 = two_point_O('deisel')
print(c13.type)
c13.start()
c13.stop()
# --------------------------------------------------------------
class A():
    verA = 'welcome to class A'
class B():
    verB = 'welcome to class B' 
class C(A,B):                                               # ! multiple inheritance
    verC = 'welcome to class C'

child = C()
print(child.verA)
print(child.verB)
print(child.verC)

#------------------------------------------------------------------------------------
import time
# ! super method
# super method is used to access methods of the parent class
class Car():
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("Car is starting...")
        time.sleep(2)
        print("car has started")
    @staticmethod
    def stop():
        print("car is stopping....")
        time.sleep(2)
        print("car has stopped")
class Toyota(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        print("Fortuner")
car11 = Toyota("Fortuner",'electric')
car11.start()
car11.stop()
print(car11.type)

# ? next!, we have a new decorator called @classmethod 
# we study the problem then we will see how this classmethod fixes this problem

class Person():
    name = 'anonymous'
    def change_name(self,name):
        self.name = name 
p101 = Person()
p101.change_name('Ironman')
print(p101.name)
print(Person.name)  # anonymous   # ! problem
# A class method is bound to the class and recieves the class as an implicit first argument.
# Note - static method can't access or modify class state and generally for utility.
#-------
class Person():
    name = 'anonymous'
    @classmethod
    def change_name(cls,name):
        cls.name = name

p22 = Person()
print(p22.name)
p22.change_name('ironman')
print(p22.name)


# ! Property decorator
class Student():
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math 
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3) +'%'
    
st1 = Student(98,97,99)
print(st1.percentage)
st1.phy = 89
print(st1.phy)
print(st1.percentage)




#-----------------------------------------------------------------------
# ! Polymorphism
# when the same operator is allowed to have different meaning according to the context 