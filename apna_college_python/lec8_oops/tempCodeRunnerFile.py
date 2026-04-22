
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