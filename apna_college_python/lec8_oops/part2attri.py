# ATTRIBUTES (DATA OR PROPERTIES) Attributes are variables that store data inside a class or object.
# CLASS AND  instance


class A:
    x = 10                                                           #class attribute
    def __init__(self):                                              #Method  **for understanding similar to or same as function 
        self.y  = 5                                                  #Object attribute or instance attr

objects = A()
print(objects.y)
class Student():                                                   
    college_name = "shoolini university"
    name = "Om chaudhary"
    def __init__(self,name,marks):
        self.name = name
        self.marks =int(marks)                                       
    
    def Welcome(self):                                                              #Method   -- does something 
        print("Welcome Student!! ", self.name)
    def get_marks(self):
        return self.marks

s1 = Student("omprakash Chaudhary" , 34)                             
print(Student.college_name)                                        
print(Student.name)
print(s1.marks,s1.name)  

# METHODS 
# Methods are functions that belong to object

s1.Welcome()
print(s1.get_marks())


#QUESTION
# Create student class that takes nameof the student and marks of 3 subjects as argument in constructor
# Then create a method to print the average.

class Student():
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    @staticmethod   # if we use this it will convert the function below into a static method
    #@staticmethod is a decorator 
    
    def hello():
        print("hey everyone , how are you all ")    
    def average(self):
        totalmarks = 0
        for x in self.marks:
            totalmarks += x
        print("Hey!",self.name, " your avg score is ",totalmarks/3)
    
s1 = Student("Shubramaniumswami",[80,78,91])

s1.average()
# we can change attributes value
s1.name = "Gopalcharya Swarma"
s1.average()


## STATIC METHOD
# Methods that don't use the self parameter(work at class level)
s1.hello()
# @staticmethod if we use this it will convert the function below into a static method
    #@staticmethod is a decorator *Decorators - decorators allow us to wrap another function in order to extend the behaviour of the wrappped functionm without permanently modifying it.
# this is just a normal method but when we use decorator staticmethod it just takes the object to a class level
    