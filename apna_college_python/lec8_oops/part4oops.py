class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Shradha")
print(s1.name)
del s1                  #del keyword is used to delete object properties or the entire object itself

# print(s1.name)


# Private attributes and methods
# Conceptual implementataion in python 
# Private attributes and methods are meant to be used only within the class and are not accessible from outside the class


class Account:
    def __init__(self,acc_no,acc_pwd):
        self.acc_no = acc_no
        #self.acc_pwd = acc_pwd                # this is a sensitive information it should be private
        self.__acc_pwd = acc_pwd                # we use __ to make it private , here it is obj attribute
    def  reset(self):
        print(self.__acc_pwd)
ac1 = Account(9430936981,8433)
#print(ac1.acc_pwd)                              # it will give us an error
print(ac1.reset())

## we see a class attribute private  and a method
class Person:
    __name = "Omprakash Chaudhary"
    def __hello(self):
        print("hello person ")                       # method private   
    
    def welcome(self):
        self.__hello()

p1 = Person()
#print(Person.__name)                              # it will give us an error conseptually private not exactly private



# print(p1.__hello())         
print(p1.welcome())                     

## INHERITANCE
# when one class(child/derived) derives the properties and methods of another class(parent/base)


class Car:                                                       #parent
    color = "Black"
    @staticmethod
    def start():
        print("The car has started")
    @staticmethod
    def stop():
        print("The car has stopped")

class ToyotaCar(Car):                                           #child (single level inheritance) let's see multiple inheritance child == parent 
    def __init__(self,brand):
        self.brand = brand
class Fortuner(ToyotaCar):                                      # Child for ToyotaCar
    def __init__(self,type):
        self.type = type
car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")
car3 = Fortuner("diesel")

print(car1.start())
print(car1.color)

# 3 types of inheritance 
# 1. single level inheritance
# 2. multi-level inheritance
print(car3.start())


# 3.multiple inheritance
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"


c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)