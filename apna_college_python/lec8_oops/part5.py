# SUPERMETHODS


class Car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("Car started....")
    @staticmethod
    def stop():
        print("Car stopped....")
    
class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        super().start()


c1 = ToyotaCar("pruis","electric")
print(c1.type)


##CLASS METHOD @classmethod  
# A class method is bound to the class & receives the class as an implicit first argument.
# Note- static method can't access or modify class state

class Person:
    name = "anonymous"
    def change_name(self,name):   # it is an instance any change will not affect the class attributes
        self.name = name
    
    @classmethod       #decorator 2              # THIS WILL DIRECTLY AFFECT THE CLASS ATTRIBUTE 'name'
    def chnge_name(cls,name):
        cls.name = name


p1 = Person()
p1.chnge_name("OM")
print(p1.name)
print(Person.name)
# 1.static method (with no arg)
# 2.class method (with cls as arg)
# 3.instance method or normal method ~ fnct (self)

# Property decorator  3
# we use @property decorator on any method in the class to use the method as a property
class Student:
    def __init__(self,phy,chem,maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        self.percentage = str((phy + chem + maths)/3) + " %"
    def cal_percentage(self):                                    # doing this in a better and easier way using @property decorator
        print(str((self.phy+self.chem+self.maths)/3) + "%")
    
    @property
    def calci_percentage(self):
        return str((self.phy+self.chem+self.maths)/3) + "%"

s1 = Student(98,97,99)
print(s1.calci_percentage)
print(s1.percentage)

s1.phy = 86
print(s1.percentage)                 # it won't change
print(s1.calci_percentage)           # minor change in the way we call it we donot need () but a method needs to be called using ()
print(s1.phy)


# Home work
# @getter   &    @setter  decorators to be studied on my own 