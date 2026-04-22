# Important
# 4 pillars of OOP
# ABSTRACTION ENCAPSULATION INHERITANCE POLYMORPHISM
# Abstraction
# Hiding the implementation details of a class and only showing the essential features to the user.
# eg car - driver knows clutch , gear and accelarator he does not know about the actual combustion or piston work etc

class Car():
    def __init__(self):
        self.brk = False
        self.acc = False
        self.clutch = False
    def start(self):
        self.acc = True
        self.clutch = True 
        print("The Car has started...")

car1 = Car()
car1.start()   
# Encapsulation 
# wrapping data and function into single unit(object).

# practice question 
# create Account class with 2 attributes - balance and account number 
#create method for debit , credit and printing the balance.

class Account():
    def __init__(self,bal,acc):
        self.balance = bal 
        self.accoount_number = acc

    #debit method
    def debits(self,debit):
        self.debit = debit
        self.balance -= debit
        print("Rs." , debit , "was debited from you account.")
        print("Remaining balance in your account = ",self.balance)
    
    #credit method
    def credits (self,credit):
        self.credit = credit
        self.balance += credit
        print("Rs." , credit , "was credited into you account.")
        print("Remaining balance in the account = ",self.balance)
    #balance method
    def get_balance(self):
        return self.balance
ac1 = Account(10000,8797996877)
print(ac1.balance)
ac1.credits(56)
ac1.debits(7600)