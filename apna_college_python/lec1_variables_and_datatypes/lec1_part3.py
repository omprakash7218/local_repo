#TYPE CONVERSION(AUTOMATICALLY)  AND TYPE CASTING(FORCED CONVERSION OR MANUAL CONVERSION)

a = 2
b = 4.25
sum = a + b # python will automoatically do the conversion since float is superior to int as it can store more values
print(sum)  # 2.0 + 4.25 = 6.25


# Lets see about forced or manual conversion 

c = float("2")
d = 4.34
print(type(c))
print(c)
print('Sum:', c+d)

e = str(3.17)
print(type(e) , e)

# TAKING INPUT FROM THE USERS

name = input("Enter your name:")  # imput function only takes string value. No matter if it is 2.566 or 54 
age = int(input("Please enter your age:"))
print("Welcome! " , name) 
print("Your age is:" , age)