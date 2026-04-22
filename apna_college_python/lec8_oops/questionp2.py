# Let's practice
# Q1. Definie a Circle class to create a circle with radius r using the constructor. Define an Area() method of the class which calculates the area of the circl.ChildProcessError
# Define a perimeter() method of the class which allows you to create the perimeter of the circle


class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return (22/7*self.radius**2)
    def perimeter(self):
        return (2*22/7*self.radius)

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())


# Q2. Define a Employee class with attributes role, department & salary .This class also has a showDetail() mehtod.
    # Create an Engineer class that inherits properties from employee & has additional attributes name and age.

class Employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department 
        self.salary = salary 

    def showDetails(self):
        print("Role = ",self.role)
        print("Department = ", self.department)
        print("Salary = ",self.salary)

class  Engineer(Employee):
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        super().__init__("Engineer","IT","75000")

Employee1 = Employee("Accountant","Finance","60000")

Employee1.showDetails()

eng1 = Engineer("Omprakash Chaudhary",25)
eng1.showDetails()

# Q3. Create a class called Order which stores item & price.
# Use Dunder funtion __gt__() to convey that:
# order1>order2 if price of order1 is greater than price of order 2


class Order:
    def __init__(self, item , price):
        self.item = item
        self.price = price
    def __gt__(self,ord2):
        ord1price = self.price
        ord2price = ord2.price
        return  ord1price > ord2price

order1 = Order("chips",100)
order2 = Order("Chocolate",50)
print(order1 > order2)