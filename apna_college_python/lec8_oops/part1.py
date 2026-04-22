# class and objects
# eg class = class object = students 
# eg class = car(blueprint) object = accessories or parts

class Student:                              #S is capital intentionally Intentionally 
    name = "Omprkash chaudhary"
    age = 24
    standard = "BBA 2nd sem"


s1 = Student()
print(s1.name)



#CONSTRUCTOR  == __init__ function it invokes when we create an object 
# All classes have; a funtion called __init__(), which is always 
# executed when the class is being initiated

class Car:
    name = "bmw"
    # default constructor
    def __init__(self):                         # constructor always take in an argument  or a parameter which is 'self' 
                                                    # self is nothing but the object itself which in this case here c1 = Car() 
        print("New car model's blueprint is loading..")
        print(self.name)
c1 = Car()      # this () , when used calls the constructor or __init__ function automatically
 
print(c1.name)


class ram():
    #default constructor
    def __init__(self):
        print("HELLO mister, would you like a cup of tea.")
    #parameterized constructor
    def __init__(self,height,weight):
        self.height = height
        self.weight = weight
        print("Loading...")
h1 = ram()
print(h1)
h = ram(77,103)
print(h.height,h.weight)


class Student():
    def __init__(self,name,marks ):
        self.name = name
        self.marks = marks
    
s1 = Student("Omprakash Chaudhary",34)
s2 = Student("Hemant Kumar Chaudhary",43)

print(s1.name, s2.name)
print(s1.name, s1.marks)
print(s2.name, s2.marks)


import math

# Calculate factorial of 5
result = math.factorial(5)
print(result)  # Output: 120