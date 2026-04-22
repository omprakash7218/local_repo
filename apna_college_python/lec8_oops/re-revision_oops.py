import time
from urllib.robotparser import RobotFileParser
# class Printer:
#     brand = "not known right now"
#     eq_needed = ["ink","paper"]
#     def __init__(self,name,brand):
#         self.brand = brand
#         self.name = name 
#         print("Printer is starting.....!")
#         time.sleep(0.75)
#         print("Started")
#     @staticmethod
#     def test_page():
#         print("Printing the test page.....")
#         time.sleep(3)
#         print("Test page has been printed.")


# p1 = Printer("canon2.1","canon")
# time.sleep(1)
# print(p1.brand)
# time.sleep(1)
# print(p1.name)
# time.sleep(1)
# p1.test_page()
# class Car: 
#     brand = "Om Solves"
#     variant = "LXI 2.0"
#     def __init__(self):
#         self.clutch = False
#         self.brk = False
#         self.acc = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         time.sleep(0.5)
#         print("Car is starting....")
#         time.sleep(1)
#         print("started!")
        
# c1 = Car()
# c1.start()
class Account():
    def __init__(self,acc_number,bal):
        self.acc_number = acc_number
        self.balance = bal
    def credit(self,cr):
        self.balance = self.balance + cr
        print(f"Rs. {cr} was credited to your account. ")
        print("Your account balance: ", self.get_balance())
    def debit(self,dt):
        self.balance = self.balance - dt
        print(f"Rs. {dt} was debted from your account.")
        print("Your account balance: ", self.get_balance())

    def get_balance(self):
        return (self.balance)
    
acc1 = Account(8210216396,10000)
# acc1.credit(150)
acc1.debit(250)
acc1.get_balance()


# Define a circle class to to create a cirlce with radius r using the constructor 
# define an area method which gives the area of the circle and also a perimeter method
class Circle():
    def __init__(self,r):
        self.r = r
    def area(self):
        self.area = (22/7*(self.r)**2)
        return f"Area of the circle is : {self.area}."
    def perimeter(self):
        self.perimeter = 2*22/7*self.r
        return f"Perimeter of the circle is : {self.perimeter}"
    @property
    def perimeter2(self):
        self.perimeter = 2*22/7*self.r
        return f"Perimeter of the circle is : {self.perimeter}"
    @property
    def area2(self):
        self.area = (22/7*(self.r)**2)
        return f"Area of the circle is : {self.area}."        
circle1 = Circle(35)
print(circle1.area())
print(circle1.perimeter())

print(circle1.area2)
print(circle1.perimeter2)

#Q2. Define an Employee class with atributes role,department & salary.This class also has a showDetail method.
# create an engineer class which inherits properties of the Employee class and has additional attributes name & age.


class Employee():
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department 
        self.salary = salary
    def show_details(self):
        print("Role: ",self.role)
        print("Department: ", self.department)
        print("Salary: ",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        super().__init__('Engineer','IT','75,000')

emp1 = Employee('manager','IT',70000)
emp1.show_details() 

eng1 = Engineer ('Ironman',35)
print(eng1.role)